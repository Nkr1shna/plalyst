from locust import HttpLocust, TaskSet

def login(l):
    response = l.client.get('http://localhost:8000/login/')
    csrftoken = response.cookies['csrftoken']
    l.client.post('http://localhost:8000/login/',
                     {'username': 'kr1shna', 'password': '40OZlike'},
                     headers={'X-CSRFToken': csrftoken})

def gp(l):
    l.client.get("/generate/1")



class UserBehavior(TaskSet):
    tasks = {login: 2, gp:2}

    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
