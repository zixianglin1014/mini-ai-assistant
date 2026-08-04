from core.embedding import EmbeddingClient
from core.vector_store import VectorStore

# 用户问题

question = "AI如何帮助程序员开发软件？"


# 问题向量化

embedding = EmbeddingClient()


query_vector = embedding.embed_text(question)


# 搜索

db = VectorStore()


result = db.search(query_vector, top_k=3)


print("\n====== 搜索结果 ======\n")


for doc in result["documents"][0]:

    print(doc)

    print("----------------")
