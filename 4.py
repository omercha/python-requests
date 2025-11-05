import requests

def getUsernamesWithCertainSubmissionCount(threshold):

    url = 'https://jsonmock.hackerrank.com/api/article_users'
    current_page = 1
    total_pages = 1
    users_with_certain_submission_count = []

    while current_page <= total_pages:

        params = {
            "page": current_page
        }

        response = requests.get(url, params=params)
        json_data = response.json()

        total_pages = json_data["total_pages"]

        for item in json_data["data"]:
            if item["submission_count"] > threshold:
                users_with_certain_submission_count.append(item["username"])

        current_page += 1

    return users_with_certain_submission_count

print((getUsernamesWithCertainSubmissionCount(1000)))
