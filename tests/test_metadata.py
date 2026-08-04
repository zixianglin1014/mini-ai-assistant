from core.loaders.document_loader import DocumentLoader

loader = DocumentLoader("data")


docs = loader.load_all()


for doc in docs:

    print("================")

    print("内容:")

    print(doc["content"][:50])

    print("Metadata:")

    print(doc["metadata"])
