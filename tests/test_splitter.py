from core.file_loader import FileLoader
from core.text_splitter import TextSplitter

loader = FileLoader("data/test.txt")


text = loader.load()


splitter = TextSplitter()


chunks = splitter.split(text)


for i, chunk in enumerate(chunks):

    print(f"\n====== Chunk {i + 1} ======\n")

    print(chunk)
