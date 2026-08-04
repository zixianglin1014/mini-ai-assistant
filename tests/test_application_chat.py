from application.chat_app import ChatApplication


def main():

    app = ChatApplication()

    while True:

        question = input("用户：")

        if question in ["exit", "quit"]:
            break

        answer = app.chat(question)

        print("\nAI:", answer)


if __name__ == "__main__":

    main()
