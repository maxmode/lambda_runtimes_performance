from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def node12(self):
        self.client.get("/node12", name="node12")

    @task(1)
    def python3(self):
        self.client.get("/python3.8", name="python3.8")

    @task(1)
    def ruby2(self):
        self.client.get("/ruby2.5", name="ruby2.5")

    @task(1)
    def golang(self):
        self.client.get("/golang", name="golang")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior