import random

from locust import HttpUser, between, task


class AIUser(HttpUser):
    """
    AI助手压力测试用户
    """

    wait_time = between(1, 3)

    questions = [
        "什么是人工智能？",
        "介绍一下RAG技术",
        "大语言模型是什么？",
        "如何优化向量数据库？",
        "什么是Embedding模型？",
    ]

    @task
    def chat(self):

        question = random.choice(self.questions)

        self.client.post("/chat", json={"question": question}, name="/chat")

    @task(3)
    def health(self):

        self.client.get("/health", name="/health")
