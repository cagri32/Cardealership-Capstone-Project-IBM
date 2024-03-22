# Uncomment the imports below before you add the function code
# import requests
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):


def get_request(endpoint, **kwargs):
    params = "&".join(
        [f"{key}={value}" for key, value in kwargs.items()]) if kwargs else ""
    request_url = backend_url + endpoint + "?" + params

    print("GET request to: {}".format(request_url))

    try:
        # Make the GET request
        response = requests.get(request_url)

        # Print response status code and content
        print("Response status code:", response.status_code)
        print("Response content:", response.content)

        # Check if response is successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            return response.json()
        else:
            # If response is not successful, raise an exception
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Handle any exceptions (e.g., network errors, invalid response)
        print("Error occurred:", e)


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
