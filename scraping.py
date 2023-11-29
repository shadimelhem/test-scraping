import requests
from bs4 import BeautifulSoup
import csv


def scrape_weather(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    country = soup.find('h1',{"class":"country-name"})
    print(country)
    # .text.strip()
    country_high = soup.find('span', class_='high').text.strip()
    country_low = soup.find('span', class_='low').text.strip()
    max_wind = soup.find('span', class_='maxwind').text.strip()

    return country, country_high, country_low, max_wind


def scrape_time_zone(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    country = soup.find('h1', class_='country-name').text.strip()
    long_name = soup.find('dd', class_='long-name').text.strip()
    abbreviations = soup.find('dd', class_='abbreviations').text.strip()
    capital = soup.find('dd', class_='capital').text.strip()
    time_zones = soup.find('dd', class_='time-zones').text.strip()
    dial_code = soup.find('dd', class_='dial-code').text.strip()

    return country, long_name, abbreviations, capital, time_zones, dial_code


def save_data(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Value'])
        writer.writerows(data)


def main():
    country = "Jordan"
    weather_url = 'https://www.timeanddate.com/weather/jordan'
    time_zone_url = 'https://www.timeanddate.com/time/zone/jordan'

    weather_data = scrape_weather(weather_url)
    time_zone_data = scrape_time_zone(time_zone_url)

    data = [
        ['Country', country],
        ['Country High', weather_data[1]],
        ['Country Low', weather_data[2]],
        ['Max Wind', weather_data[3]],
        ['Country Capital', time_zone_data[3]],
        ['Weather', 'N/A'],
        ['Feels Like', 'N/A'],
        ['Forecast', 'N/A'],
        ['Wind', 'N/A'],
        ['Long Name', time_zone_data[1]],
        ['Abbreviations', time_zone_data[2]],
        ['Time Zones', time_zone_data[4]],
        ['Dial Code', time_zone_data[5]]
    ]

    file_path = f'{country}.csv'
    save_data(file_path, data)
    print(f"Data saved to {file_path}")


if __name__ == '__main__':
    main()