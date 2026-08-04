from dataclasses import dataclass


@dataclass
class PromptConfig:
    """
    Prompt配置对象
    """

    name: str

    role: str

    version: str

    description: str

    template: str
