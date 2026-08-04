from core.loaders.document_loader import DocumentLoader

loader = DocumentLoader("data")


documents = loader.load_all()


print("\n====== 文档数量 ======")


print(len(documents))


for doc in documents:

    print("\n====== 来源 ======")

    print(doc["metadata"]["source"])

    print("\n内容预览:")

    print(doc["content"][:100])
