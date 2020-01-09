from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def runtimes(self):
        self.client.get("/node12", name="node12")
        self.client.get("/python3.8", name="python3.8")
        self.client.get("/ruby2.5", name="ruby2.5")
        self.client.get("/golang", name="golang")
        self.client.get("/java11", name="java11")
        self.client.get("/dotnet2.1", name="dotnet2.1")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior