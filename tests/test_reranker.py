from core.reranker import Reranker

reranker = Reranker()


docs = [
    "人工智能可以帮助软件开发，提高代码生成效率",
    "今天的天气很好",
    "大语言模型可以辅助程序员完成代码分析",
]


result = reranker.rerank("人工智能如何提高软件开发效率", docs)


for item in result:

    print(item)
