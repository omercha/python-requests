import requests

def longestUsername():

    current_page = 1
    total_pages = 1
    longest_username = ""
    params = {}

    while current_page <= total_pages:

        params["page"] = current_page
        response = requests.get("https://jsonmock.hackerrank.com/api/article_users", params=params)

        json_data = response.json()

        total_pages = json_data["total_pages"]

        for item in json_data["data"]:
            if len(item["username"]) > len(longest_username):
                longest_username = item["username"]

        current_page += 1

        return longest_username

print(longestUsername()+" "+str(len(longestUsername())))
