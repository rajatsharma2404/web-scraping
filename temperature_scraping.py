import requests
import selectorlib
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com/"

def scrape(url):
    response = requests.get(URL)
    source = response.text

    extractor = selectorlib.Extractor.from_yaml_file("extract1.yaml")
    value = extractor.extract(source)["temperature"]
    return value

def write(temperature, filename):
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"{date_time}, {temperature} \n")


if __name__ == "__main__":
    temperature = scrape(URL)
    write(temperature, "temperature.txt")