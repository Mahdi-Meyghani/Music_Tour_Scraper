import requests
import selectorlib
import smtplib
import ssl
import os
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


class Tour:
    def scrape(self, url):
        """Scraps a web page"""
        response = requests.get(url, headers=HEADERS)
        source = response.text

        return source

    def extract(self, source):
        """Extract a particular part from web page"""
        extractor = selectorlib.Extractor.from_yaml_file("tours.yaml")
        value = extractor.extract(source)["tours"]

        return value


class Email:
    def send(self, message):
        """Send an email alarm when new event is find """
        host = "smtp.gmail.com"
        port = 465

        username = "mahdimeyghani02@gmail.com"
        password = os.getenv("MusicEventPassword")
        receiver = "mahdimeyghani02@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)

        print("Email was sent successfully!")


class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def store_tours(self, tour_text):
        """Save the tours info into a file"""
        with open(self.filepath, "a") as tours_file:
            tours_file.write(tour_text + "\n")

    def read_tours(self):
        """Read the tours info from a file and return it as a string"""
        with open(self.filepath, "r") as tours_file:
            tours_text = tours_file.read()

        return tours_text


class Database:
    def __init__(self, dbpath):
        self.dbpath = dbpath
        self.CONN = sqlite3.connect(dbpath)

    def store_tours(self, tours_text):
        """Save the tours info into a database"""
        values = tours_text.split(", ")

        cursor = self.CONN.cursor()
        cursor.execute("INSERT INTO events VALUES (?, ?, ?)", values)
        self.CONN.commit()

    def read_tours(self, tour_text):
        """Read the tours info from database and return it as a list of tuples"""
        row = tour_text.split(", ")
        bandName, city, date = row

        cursor = self.CONN.cursor()
        cursor.execute("SELECT * FROM events WHERE bandName = ? AND city = ? AND date = ?",
                       (bandName, city, date))
        exists = cursor.fetchall()

        return exists


if __name__ == "__main__":
    while True:
        tour = Tour()
        source_text = tour.scrape(URL)
        tours = tour.extract(source_text)
        print(tours)

        # file = File(filepath="tours.txt")
        # all_tours = file.read_tours()

        if tours != "No upcoming tours":
            database = Database(dbpath="tours.db")
            exist = database.read_tours(tour_text=tours)
            print(exist)
            if not exist:
                # file.store_tours(tour_text=tours)

                database.store_tours(tours_text=tours)
                email = Email()
                email.send(f"Subject: Music Tour\n\nHey, new event was found on:\n{tours}")

        time.sleep(2)
