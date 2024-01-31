Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.cardekho.com/used-cars+in+bangalore'

# Add headers to the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.cardekho.com/',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Send a GET request to the URL with headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print the entire HTML content
    print(soup.prettify())

    # Continue with the rest of the code...
    # Extract car information (replace this with the actual structure of the website)
    car_elements = soup.find_all('div', class_='gsc_col-xs-12')

    # Open a CSV file for writing
    with open('used_cars_bangalore.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer
        csv_writer = csv.writer(csvfile)

        # Write header row
        csv_writer.writerow(['Car Name', 'Price', 'Year', 'Kilometers', 'Fuel Type', 'Transmission', 'Owner Type'])

        # Write data rows
        for car_element in car_elements:
            try:
                car_name_element = car_element.find('a', class_='gsc_col-sm-7 gsc_col-md-8 gsc_col-xs-12 gsc_col-md-6 car-title')
                car_name = car_name_element.text.strip() if car_name_element else 'N/A'

                car_price_element = car_element.find('div', class_='price gsc_col-sm-5 gsc_col-md-4 gsc_col-xs-12 gsc_col-md-6')
                car_price = car_price_element.text.strip() if car_price_element else 'N/A'

                car_year_element = car_element.find('div', class_='gsc_col-sm-2 gsc_col-xs-3 gsc_col-md-2')
                car_year = car_year_element.text.strip() if car_year_element else 'N/A'

                car_kilometers_element = car_element.find('div', class_='gsc_col-xs-3 gsc_col-sm-2 gsc_col-md-2 gsc_col-md-2')
                car_kilometers = car_kilometers_element.text.strip() if car_kilometers_element else 'N/A'

                car_fuel_type_element = car_element.find('div', class_='gsc_col-xs-5 gsc_col-sm-3 gsc_col-md-2 gsc_col-md-2')
                car_fuel_type = car_fuel_type_element.text.strip() if car_fuel_type_element else 'N/A'

                car_transmission_element = car_element.find('div', class_='gsc_col-xs-4 gsc_col-sm-2 gsc_col-md-2 gsc_col-md-2')
                car_transmission = car_transmission_element.text.strip() if car_transmission_element else 'N/A'

                car_owner_type_element = car_element.find('div', class_='gsc_col-xs-4 gsc_col-sm-3 gsc_col-md-2 gsc_col-md-2')
                car_owner_type = car_owner_type_element.text.strip() if car_owner_type_element else 'N/A'

                # Write the data to the CSV file
                csv_writer.writerow([car_name, car_price, car_year, car_kilometers, car_fuel_type, car_transmission, car_owner_type])

            except Exception as e:
                print(f"An error occurred: {e}")

    print("Data has been successfully scraped and saved to 'used_cars_bangalore.csv'.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
