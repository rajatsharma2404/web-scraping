import time
import sqlite3
import requests
import selectorlib
from emailing import send_email

URL = "https://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect("data.db")

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def write(data):
    row = extracted.split(',')
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)",row)
    connection.commit()


def read(data):
    row = data.split(',')
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE Band = ? AND City = ? AND Date = ?",(row[0], row[1], row[2]))
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        if extracted != "No upcoming tours":
            content = read(extracted)
            if not content:
                write(extracted)
                send_email(message = f"Hey, we have a tour for {extracted}!")

        time.sleep(10)