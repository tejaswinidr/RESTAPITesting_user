import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/config.ini')
    return config


def get_headers(token=None):
    headers = {'Content-Type': 'application/json'}
    if token is not None:
        headers.update({'Authorization': 'Bearer ' + token})
    return headers
