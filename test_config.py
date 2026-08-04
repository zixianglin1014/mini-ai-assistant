from core.config import get_api_key, get_value

print("模型:", get_value("llm.model"))


print("Embedding:", get_value("embedding.model"))


print("向量库:", get_value("paths.vector_db"))


print("API:", get_api_key())
