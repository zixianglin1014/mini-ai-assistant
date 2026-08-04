from locust import HttpUser, between, task


class RAGCacheUser(HttpUser):

    wait_time = between(1, 2)

    @task
    def rag_cache_test(self):

        self.client.post("/api/rag", json={"question": "什么是人工智能"})
