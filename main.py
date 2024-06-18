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


if __name__ == "__main__":
    source_text = scrape_tours(URL)
    tours = extract_tours(source_text)
    print(tours)
