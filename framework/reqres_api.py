import requests
from framework.models import PostCreateResponse

class ReqresAPI:
    def __init__(self, host):
        self.host = host
        self.session = requests.Session()

    def get_users(self, page):
        url = f'{self.host}/api/users?page={page}'
        response = self.session.get(url)
        users_data = response.json() if response.ok else None
        return response.status_code, users_data

    def get_users_with_per_page(self, page, per_page):
        url = f'{self.host}/api/users?page={page}&per_page={per_page}'
        response = self.session.get(url)
        users_data = response.json() if response.ok else None
        return response.status_code, users_data


    def create_user(self, name, job):
        url = f'{self.host}/api/users'
        body = {
        "name": name,
        "job": job
    }
        response = self.session.post(url, body)
        users_data = response.json() if response.ok else None
        return response.status_code, users_data

