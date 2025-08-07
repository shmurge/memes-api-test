import os
from dotenv import load_dotenv


class Headers:

    def __init__(self):
        load_dotenv()

    base_headers = {'Content-Type': 'application/json'}

    @staticmethod
    def headers_with_auth():

        return {
             'Content-Type': 'application/json',
             'Authorization': os.getenv('API-TOKEN')
        }
