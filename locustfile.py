
from locust import HttpUser, task, between


class DjangoTaskUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def health_check(self):
        self.client.get("/health/", name="Health Check")

    @task(2)
    def task_list(self):
        self.client.get("/", name="Task List")
