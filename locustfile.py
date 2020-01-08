from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def node(self):
        self.client.get("/node12", name="node12")

    @task(1)
    def python(self):
        self.client.get("/python3.8", name="python3.8")

    @task(1)
    def ruby(self):
        self.client.get("/ruby2.5", name="ruby2.5")

    @task(1)
    def golang(self):
        self.client.get("/golang", name="golang")

    @task(1)
    def java(self):
        self.client.get("/java11", name="java11")

    @task(1)
    def dotnet(self):
        self.client.get("/dotnet2.1", name="dotnet2.1")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior