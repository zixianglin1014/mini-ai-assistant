from application.rag_app import RAGApplication


def main():

    app = RAGApplication()

    answer = app.ask("人工智能如何提高软件开发效率")

    print("\n======回答======")
    print(answer)


if __name__ == "__main__":
    main()
