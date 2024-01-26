from docx import Document
from scraper import Scraper


def get_user_input():
    def get_valid_zipcode():
        while True:
            zipcode = input("Please enter a zip code: ")
            if len(zipcode) == 5 and zipcode.isdigit():
                return zipcode
            print("Error: Invalid zip code. Please enter a 5-digit zip code.")

    def get_time_period_option():
        time_period_options = {
            '1': '1wk', '2': '1mo', '3': '3mo', '4': '6mo',
            '5': '1yr', '6': '2yr', '7': '3yr', '8': '5yr',
        }
        options_message = "\n".join(
            [f"{number}. {time}" for number, time in time_period_options.items()])
        print(f"Get the addresses sold from the past:\n{options_message}")

        while True:
            choice = input("Enter the number of your choice: ")
            if choice in time_period_options:
                return time_period_options[choice]
            print("Error: Invalid option. Please enter a number from 1 to 8.")

    zipcode = get_valid_zipcode()
    time_period = get_time_period_option()
    return zipcode, time_period


def write_addresses_to_doc(addresses, template, output):
    doc = Document(template)
    table = doc.tables[0]  # assuming the first table in the document

    for row, address in zip(table.rows, addresses):
        for cell in row.cells:
            if 'ADDRESS_PLACEHOLDER' in cell.text:
                cell.text = cell.text.replace('ADDRESS_PLACEHOLDER', address or '')

    doc.save(output)


if __name__ == "__main__":
    zipcode, time_period = get_user_input()
    scraper = Scraper(zipcode, time_period)
    addresses = scraper.scrape()
    print(f"Number of addresses fetched: {len(addresses)}")
    write_addresses_to_doc(addresses, 'temp.docx', 'output.docx')
