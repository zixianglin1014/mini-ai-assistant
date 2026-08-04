from core.embedding import EmbeddingClient
from core.file_loader import FileLoader
from core.text_splitter import TextSplitter
from core.vector_store import VectorStore

loader = FileLoader("data/test.txt")


text = loader.load()


splitter = TextSplitter()


chunks = splitter.split(text)


embedding = EmbeddingClient()


vectors = embedding.embed_documents(chunks)


sources = ["data/test.txt" for _ in chunks]


db = VectorStore()


db.add_documents(chunks, vectors, sources)


print("知识库重新构建完成")
