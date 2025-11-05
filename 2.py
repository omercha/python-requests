import requests

def findHighestLaptopPrice():
    url = 'https://api.practice-challenge.com/products'
    current_page = 1
    total_pages = 1
    highest_laptop_price = 0

    params = {
        "category": "Laptops"
    }

    while current_page <= total_pages:

        params["page"] = current_page

        response = requests.get(url, params=params)
        data = response.json()

        total_pages = data["total_pages"]

        for item in data["items"]:

            try:
                cleaned_price = float(item["price"].replace('$', '').replace(',', ''))
                if cleaned_price > highest_laptop_price:
                    highest_laptop_price = cleaned_price
            except:
                continue

        current_page += 1

    return highest_laptop_price