import time

import requests
import selectorlib
from emailing import send_email

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def write(extracted, filename):
    with open(filename, "a") as file:
        file.write(extracted + "\n")

def read(filename):
    with open(filename, "r") as file:
        content = file.read()

    return content



if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read("data.txt")

        if extracted != "No upcoming tours":
            if extracted not in content:
                write(extracted, "data.txt")
                send_email(message = f"Hey, we have a tour for {extracted}!")

        time.sleep(10)