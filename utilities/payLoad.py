import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def get_user_payload():
    email = "test_" + generate_random_string(8) + "@gmail.com"
    user = {
        "name": "Tejaswini walake",
        "email": email,
        "password": "123456",
        "confirmPassword": "123456"
    }
    return user


def put_user_payload():
    name = "test_" + generate_random_string(5)
    body = {
        "attributesToBeUpdated": ["name"],
        "name": name,
        "password": "adsfsdf",
        "confirmPassword": "adsfsdf"
    }
    return body
