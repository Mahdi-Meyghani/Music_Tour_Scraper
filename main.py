import requests
import selectorlib

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


def send_email():
    print("Email was sent successfully!")


def store_tours(tour_text):
    with open("tours.txt", "a") as tours_file:
        tours_file.write(tour_text + "\n")


def read_tours():
    with open("tours.txt", "r") as tours_file:
        tours_text = tours_file.read()

    return tours_text


if __name__ == "__main__":
    source_text = scrape_tours(URL)
    tours = extract_tours(source_text)
    print(tours)
    store_tours(tours)
    if tours != "No upcoming tours" and tours not in (list or str):
        send_email()
