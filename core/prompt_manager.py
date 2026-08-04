from core.prompt_schema import PromptConfig
from core.prompts.chat import CHAT_SYSTEM_PROMPT
from core.prompts.qa import QA_PROMPT
from core.prompts.roles import DEVELOPER_PROMPT, EXPERT_PROMPT, STUDENT_PROMPT
from core.prompts.summary import SUMMARY_PROMPT
from core.prompts.title import TITLE_PROMPT
from utils.logger import logger


class PromptManager:
    """
    Prompt统一管理器


    功能：

    1. Prompt注册
    2. Prompt获取
    3. Prompt模板渲染
    4. Prompt版本管理

    """

    def __init__(self):

        self.prompts = {}

        self.register(
            PromptConfig(
                name="qa",
                role="rag_qa",
                version="v1",
                description="知识库问答Prompt",
                template=QA_PROMPT,
            )
        )

        self.register(
            PromptConfig(
                name="chat",
                role="assistant",
                version="v1",
                description="聊天助手Prompt",
                template=CHAT_SYSTEM_PROMPT,
            )
        )

        self.register(
            PromptConfig(
                name="summary",
                role="summarizer",
                version="v1",
                description="文本总结Prompt",
                template=SUMMARY_PROMPT,
            )
        )

        self.register(
            PromptConfig(
                name="title",
                role="title_generator",
                version="v1",
                description="标题生成Prompt",
                template=TITLE_PROMPT,
            )
        )

        self.roles = {
            "student": STUDENT_PROMPT,
            "developer": DEVELOPER_PROMPT,
            "expert": EXPERT_PROMPT,
        }

        logger.info("Prompt管理器初始化完成")

    def register(self, config: PromptConfig):
        """
        注册Prompt
        """

        key = (config.name, config.version)

        self.prompts[key] = config

    def get(self, name, version="v1"):

        key = (name, version)

        if key not in self.prompts:

            raise ValueError(f"Prompt不存在:{name}-{version}")

        return self.prompts[key]

    def render(self, name, version="v1", **kwargs):
        """
        渲染Prompt模板
        """

        prompt = self.get(name, version)

        return prompt.template.format(**kwargs)

    def list_prompts(self):

        return [
            {
                "name": config.name,
                "role": config.role,
                "version": config.version,
                "description": config.description,
            }
            for config in self.prompts.values()
        ]

    def get_role_prompt(self, role):
        """
        获取用户角色Prompt
        """

        if role not in self.roles:

            raise ValueError(f"角色不存在:{role}")

        return self.roles[role]
