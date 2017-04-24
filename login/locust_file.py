# locustfile.py
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    def login(self):
        # GET login page to get csrftoken from it
        response = self.client.get('http://localhost:8000/login/')
        csrftoken = response.cookies['csrftoken']
        # POST to login page with csrftoken
        self.client.post('http://localhost:8000/login/',
                         {'username': 'gouthu123', 'password': 'gouthu123'},
                         headers={'X-CSRFToken': csrftoken})

    @task(1)
    def index(self):
        self.client.get('/')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
