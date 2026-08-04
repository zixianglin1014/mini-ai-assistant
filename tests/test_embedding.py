from core.embedding import EmbeddingClient

embedding = EmbeddingClient()


text = "大语言模型可以帮助软件开发者提高效率"


vector = embedding.embed_text(text)


print("向量长度:", len(vector))


print("前10个向量:", vector[:10])
