from core.loaders.txt_loader import TxtLoader

loader = TxtLoader()


text = loader.load("data/test.txt")


print(text)
