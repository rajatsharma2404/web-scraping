import time

import requests
import selectorlib
from datetime import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"
connection = sqlite3.connect("temperature.db")

def create_table():
    cursor = connection.cursor()
    cursor.execute(" CREATE TABLE IF NOT EXISTS temperature(date_time TEXT, temperature TEXT)")
    connection.commit()

def scrape(url):
    response = requests.get(URL)
    source = response.text

    extractor = selectorlib.Extractor.from_yaml_file("extract1.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def write(temperature):
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES (?, ?)",(date_time, temperature))
    connection.commit()


if __name__ == "__main__":
    while True:
        temperature = scrape(URL)
        create_table()
        write(temperature)
        time.sleep(10)