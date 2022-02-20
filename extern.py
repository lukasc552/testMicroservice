import requests

externAPI = "https://jsonplaceholder.typicode.com"
users_url = externAPI + "/users"


def validate_user(user_id):
    response = requests.get(users_url + f'/{user_id}')
    return response.json()

