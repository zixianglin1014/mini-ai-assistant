import argparse

from application.chat_app import ChatApplication
from application.rag_app import RAGApplication
from utils.logger import logger


def chat_mode():

    app = ChatApplication()

    print("\n====== Mini AI Assistant ======")
    print("输入 exit 或 quit 退出\n")

    while True:

        question = input("用户：")

        if question.lower() in ["exit", "quit"]:

            print("退出聊天")

            break

        try:

            answer = app.chat(question)

            print("\nAI：")

            print(answer)

            print()

        except Exception as e:

            logger.error(e)

            print(f"回答失败:{e}")


def rag_mode():

    app = RAGApplication()

    print("\n====== RAG知识库模式 ======")

    print("输入 exit 或 quit 退出\n")

    while True:

        question = input("用户：")

        if question.lower() in ["exit", "quit"]:

            break

        try:

            answer = app.ask(question)

            print("\nAI：")

            print(answer)

            print()

        except Exception as e:

            logger.error(e)

            print(f"回答失败:{e}")


def main():

    parser = argparse.ArgumentParser(description="Mini AI Assistant")

    parser.add_argument("--chat", action="store_true", help="聊天模式")

    parser.add_argument("--rag", action="store_true", help="知识库模式")

    args = parser.parse_args()

    if args.chat:

        logger.info("进入聊天模式")

        chat_mode()

    elif args.rag:

        logger.info("进入RAG知识库模式")

        rag_mode()

    else:

        print("""
Mini AI Assistant

使用:

python main.py --chat

聊天模式


python main.py --rag

知识库模式

""")


if __name__ == "__main__":

    main()
