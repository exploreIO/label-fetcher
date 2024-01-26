import requests
from bs4 import BeautifulSoup


class Property:
    def __init__(self, address):
        self.address = address


class Scraper:
    def __init__(self, zipcode, time_period):
        self.zipcode = zipcode
        self.time_period = time_period
        self.base_url = f'https://www.redfin.com/zipcode/{self.zipcode}/filter/include=sold-{self.time_period}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def get_page_addresses(self, url):
        with requests.Session() as s:
            s.headers.update(self.headers)
            response = s.get(url)
            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                return []
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.find_all('div', class_='link-and-anchor')

    def scrape(self):
        addresses = set()
        page_number = 1
        while True:
            url = f"{self.base_url}/page-{page_number}"
            page_addresses = self.get_page_addresses(url)
            if not page_addresses:
                break
            for page in page_addresses:
                address = page.text.strip()
                if self.zipcode in address:
                    addresses.add(address)
            self.print_addresses(addresses)
            page_number += 1
        return list(addresses)

    def print_addresses(self, addresses):
        properties = [Property(address) for address in addresses]
        for property in properties:
            print(property.address)