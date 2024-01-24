import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


class Property:
    def __init__(self, address):
        self.address = address


class Scraper:
    def __init__(self, target_zipcode):
        self.target_zipcode = target_zipcode
        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(days=90)
        self.url = f'https://www.redfin.com/zipcode/{self.target_zipcode}/filter/include=sold-3mo'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def scrape(self):
        with requests.Session() as s:
            s.headers.update(self.headers)
            try:
                response = s.get(self.url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    addresses = soup.find_all('div', class_=['homeAddressV2', 'bp-Homecard__Address'])
                    properties = [Property(address.text.strip()) for address in addresses]
                    for property in properties:
                        print(property.address)
                else:
                    print(f"Error: {response.status_code}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    scraper = Scraper('92626')
    scraper.scrape()
