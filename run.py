from docx import Document

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


def write_addresses_to_doc(addresses, template, output):
    doc = Document(template)
    table = doc.tables[0]  # assuming the table is the first one in the document
    for i, row in enumerate(table.rows):
        if i >= len(addresses):  # If i is not less than the length of addresses, break the loop
            break
        for cell in row.cells:
            if 'ADDRESS_PLACEHOLDER' in cell.text:
                address = str(addresses[i].get_text()) if addresses[i] else ''
                cell.text = cell.text.replace('ADDRESS_PLACEHOLDER', address)
    doc.save(output)


if __name__ == "__main__":
    zipcode, time_period = get_user_input()
    scraper = Scraper(zipcode, time_period)
    addresses = scraper.scrape()
    print(f"Number of addresses fetched: {len(addresses)}")
    write_addresses_to_doc(addresses, 'temp.docx', 'output.docx')
