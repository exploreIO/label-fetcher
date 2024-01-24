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

    def scrape(self):
        addresses = []
        page_number = 1
        with requests.Session() as s:
            s.headers.update(self.headers)
            while True:
                url = f"{self.base_url}/page-{page_number}"
                try:
                    response = s.get(url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        page_addresses = soup.find_all('div', class_='link-and-anchor')
                        if not page_addresses:
                            break
                        addresses.extend(page_addresses)
                        properties = [Property(address.text.strip()) for address in page_addresses]
                        for property in properties:
                            print(property.address)
                        page_number += 1
                    else:
                        print(f"Error: {response.status_code}")
                        break
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    break
        return addresses