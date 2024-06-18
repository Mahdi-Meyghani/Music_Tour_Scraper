import requests
import selectorlib
import smtplib
import ssl
import os
import time

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def scrape_tours(url):
    """Scraps a web page"""
    response = requests.get(url, headers=HEADERS)
    source = response.text

    return source


def extract_tours(source):
    """Extract a particular part from web page"""
    extractor = selectorlib.Extractor.from_yaml_file("tours.yaml")
    value = extractor.extract(source)["tours"]

    return value


def send_email(message):
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


def store_tours(tour_text):
    """Save the tours info into a file"""
    with open("tours.txt", "a") as tours_file:
        tours_file.write(tour_text + "\n")


def read_tours():
    """Read the tours info from a file and return it as a string"""
    with open("tours.txt", "r") as tours_file:
        tours_text = tours_file.read()

    return tours_text


if __name__ == "__main__":
    while True:
        source_text = scrape_tours(URL)
        tours = extract_tours(source_text)
        print(tours)

        all_tours = read_tours()

        if tours != "No upcoming tours" and tours not in all_tours:
            store_tours(tours)
            send_email(f"Subject: Music Tour\n\nHey, new event was found on:\n{tours}")

        time.sleep(2)
