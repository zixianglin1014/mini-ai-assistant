from core.prompt_manager import PromptManager


def main():

    manager = PromptManager()

    print("已有Prompt:")

    print(manager.list_prompts())

    print("\nQA Prompt:")

    print(manager.get("qa"))


if __name__ == "__main__":

    main()
