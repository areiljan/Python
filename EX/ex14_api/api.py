"""API exercise."""
from typing import Any
import requests
import requests.exceptions
from requests import RequestException, Response


def get_request(url: str) -> int:
    """
    Send an HTTP GET request to the specified URL.

    Return the resulting response object status code.

    :param url: The URL to which the GET request will be sent.
    :return: Server's response to the request.
    """
    response = requests.get(url)
    return response.status_code


def get_request_error_handling(url: str) -> int | requests.RequestException:
    """
    Send an HTTP GET request to the specified URL with error handling.

    Handle any exceptions that may occur during the request.

    :param url: The URL to which the GET request will be sent.
    :return: Server's response object or the exception object if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.status_code
    except requests.RequestException as exception:
        return exception


def post_request(url: str, data: dict) -> Response:
    """
    Send an HTTP POST request with JSON data to the specified URL.

    Handle any exceptions that may occur during the request.

    :param url: The URL to which the POST request will be sent.
    :param data: Dictionary to be sent along with the POST request.
    :return: Server's response json object or the exception object if an error occurs.
    """
    try:
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise Exception(f"Error: Request failed with status code {response.status_code}")
        return response
    except requests.RequestException:
        return RequestException


def delete_request(url: str) -> int | requests.RequestException:
    """
    Send an HTTP DELETE request to the specified URL.

    Handle any exceptions that may occur during the request.

    :param url: The URL to which the DELETE request will be sent.
    :return: Server's response status code or the exception object if an error occurs.
    """
    try:
        response = requests.delete(url)
        return response.status_code
    except requests.RequestException:
        return RequestException


def stream_request(url: str) -> str:
    """
    Send an HTTP GET request to the specified URL and stream the response.

    More information:
    https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests

    Return a string containing the streamed content.

    :param url: The URL to send the GET request to.
    :return: A string containing the streamed content.
    """
    r = requests.get(url, stream=True)
    string_to_return = ""
    if r.encoding is None:
        r.encoding = 'utf-8'
    for line in r.iter_lines(decode_unicode=True):
        if line:
            string_to_return += str(line)
    return string_to_return


def get_authenticated_request(url: str, auth_token: str) -> Any | requests.RequestException:
    """
    Send an authenticated HTTP GET request using the provided token.

    Note: Do not push your auth token into GIT.

    :param url: The URL to which the GET request will be sent.
    :param auth_token: The authentication token for the request.
    :return: Server's response json object or the exception object if an error occurs.
    """
    try:
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise Exception("Unauthorized request")
        else:
            raise Exception(f"Error: Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        return e


def advanced_user_filter(url, min_followers: int, min_posts: int, min_following: int) -> list:
    """
    Fetch user data from a URL and filter based on specified criteria.

    Return specific fields for users meeting the follower, post, and following thresholds.
    Each user in the returned list has to include their username, full_name, followers, following, and posts.

    :param url: URL for user data.
    :param min_followers: Minimum followers required.
    :param min_posts: Minimum posts required.
    :param min_following: Minimum following required.
    :return: List of user data dictionaries.
    """
    filtered_users = []
    response = requests.get(url)
    user_data = response.json()
    for user in user_data:
        if (user["followers"] >= min_followers
                and user["posts"] >= min_posts
                and user["following"] >= min_following):
            criteria = {'username': user['username'],
                        'full_name': user['full_name'],
                        'followers': user['followers'],
                        'following': user['following'],
                        'posts': user['posts']}
            filtered_users.append(criteria)
    return filtered_users


def fetch_aggregate_data(url: str) -> dict:
    """
    Process a list of JSON objects to aggregate specific data points.

    Aggregate such as the total and average number of followers,
    posts, and following for all users.

    https://cs.taltech.ee/services/ex14/json-data

    The dictionary should have the following information:
    - 'average_followers'
    - 'average_following'
    - 'average_posts'
    - 'total_followers'
    - 'total_following'
    - 'total_posts'

    :param url: URL from which to fetch user data.
    :return: Aggregated data including total and average values.
    """
    user_count = 0
    total_followers = 0
    total_following = 0
    total_posts = 0

    response = requests.get(url)
    user_data = response.json()
    for user in user_data:
        if user['username']:
            user_count += 1
        total_followers += user['followers']
        total_following += user['following']
        total_posts += user['posts']

    average_followers = total_followers / user_count
    average_following = total_following / user_count
    average_posts = total_posts / user_count
    return {'average_followers': average_followers,
            'average_following': average_following,
            'average_posts': average_posts,
            'total_followers': total_followers,
            'total_following': total_following,
            'total_posts': total_posts}


if __name__ == '__main__':
    print(get_request("https://www.google.com"))  # 200
    print(advanced_user_filter(
        "https://cs.taltech.ee/services/ex14/json-data",
        750000, 900, 2500))
    print(fetch_aggregate_data(
        "https://cs.taltech.ee/services/ex14/json-data"))
