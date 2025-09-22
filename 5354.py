import requests
from bs4 import BeautifulSoup


def get_component_info(part_number):
    url = f"https://www.mouser.com/Search/Refine?Keyword={part_number}"

    response = requests.get(url)

    if response.status_code != 200:
        return "Ne rabotaet site"

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        product_category = soup.find('span', {'class': 'mouser-results-prodcat'}).text.strip()
        stock = soup.find('span', {'class': 'mouser-results-quantity'}).text.strip()
        factory_lead_time = soup.find('span', {'class': 'mouser-results-leadtime'}).text.strip()
        unit_price = soup.find('span', {'class': 'mouser-results-price'}).text.strip()
        description = soup.find('span', {'class': 'mouser-results-description'}).text.strip()

        result = f"""
        Product Category: {product_category}
        Stock: {stock}
        Factory Lead Time: {factory_lead_time}
        Unit Price (1): {unit_price}
        Description: {description}
        """

        return result
    except AttributeError:
        return "ne rabotaet"


part_number = input("Enter part: ")

info = get_component_info(part_number)

print(info)
