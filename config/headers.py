import os
from dotenv import load_dotenv

load_dotenv()


class Headers:
    base_headers = {'Content-Type': 'application/json'}

    headers_with_auth = {
        'Content-Type': 'application/json',
        'Authorization': os.getenv('API-TOKEN')
    }
