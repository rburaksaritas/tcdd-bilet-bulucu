import requests
import config

headers = {
    'Authorization': 'Basic ZGl0cmF2b3llYnNwOmRpdHJhMzQhdm8u'
}

def post_request(url, body):
    return requests.post(url, json=body, headers=headers)
