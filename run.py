from scraper import Scraper


def get_user_input():
    while True:
        zipcode = input("Please enter a zip code: ")
        if len(zipcode) != 5 or not zipcode.isdigit():
            print("Error: Invalid zip code. Please enter a 5-digit zip code.")
            continue
        else:
            time_period_options = {
                '1': '1wk',
                '2': '1mo',
                '3': '3mo',
                '4': '6mo',
                '5': '1yr',
                '6': '2yr',
                '7': '3yr',
                '8': '5yr',
            }
            while True:
                print("Get the addresses sold from the past:")
                print("1. 1 week")
                print("2. 1 month")
                print("3. 3 months")
                print("4. 6 months")
                print("5. 1 year")
                print("6. 2 year")
                print("7. 3 year")
                print("8. 5 year")
                time_period_option = input("Enter the number of your choice: ")
                if time_period_option in time_period_options:
                    return zipcode, time_period_options[time_period_option]
                else:
                    print("Error: Invalid option. Please enter a number from 1 to 8.")



if __name__ == "__main__":
    zipcode, time_period = get_user_input()
    scraper = Scraper(zipcode, time_period)
    addresses = scraper.scrape()
    print(f"Number of addresses fetched: {len(addresses)}")
