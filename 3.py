import requests

def getHighestSubmissionCount():

    url = 'https://jsonmock.hackerrank.com/api/article_users'
    current_page = 1
    total_pages = 1
    highest_submission_count = 0

    while current_page <= total_pages:

        params = {
            "page": current_page
        }

        response = requests.get(url, params=params)
        json_data = response.json()

        total_pages = json_data["total_pages"]

        for item in json_data["data"]:
            if item["submission_count"] > highest_submission_count:
                highest_submission_count = item["submission_count"]

        current_page += 1

    return highest_submission_count

print((getHighestSubmissionCount()))
