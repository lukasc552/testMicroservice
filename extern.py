import requests

externAPI = "https://jsonplaceholder.typicode.com"
users_url = externAPI + "/users"
posts_url = externAPI + "/posts"


def validate_user(user_id):
    response = requests.get(users_url + f'/{user_id}')
    return response.json()


def find_post_by_id(post_id):
    response = requests.get(posts_url + f'/{post_id}')
    return response.json()

