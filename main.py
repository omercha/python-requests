import requests

# goal: calculate total population in a country by parsing over data from each city
def getTotalPopulation(countryName):

    # initial variables
    url = 'https://api.example.com/cities'
    current_page = 1
    total_pages = 1
    total_population = 0

    # pagination setup
    while current_page <= total_pages:

        params = {
            "country": countryName
            "page": current_page
        }

        # perform a GET request
        response = requests.get(url, params=params)
        data = response.json()

        # update total_pages to actual total_pages value
        total_pages = data["total_pages"]

        # parse over each city in the current page and add the population to our total
        for city in data["data"]:
            total_population += city["population"]

        # move onto next page
        current_page += 1

    return total_population
