import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def scrape_zillow():
    # Set target zip code and date range
    target_zipcode = '78258'
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)

    # Construct URL
    url = f'https://www.redfin.com/zipcode/{target_zipcode}/filter/include=sold-3mo'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    with requests.Session() as s:
        s.headers.update(headers)
        try:

            response = s.get(url)

            if response.status_code == 200:

                soup = BeautifulSoup(response.text, 'html.parser')
                addresses = soup.find_all('div', class_='homeAddressV2')

                for address in addresses:
                    print(address.text.strip())
            else:
                print(f"Error: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    scrape_zillow()
