from core.llm import ZhipuLLM
from core.memory_manager import MemoryManager
from core.prompt_manager import PromptManager
from utils.logger import logger


class ChatApplication:
    """
    聊天应用核心类


    功能:

    1. 多session聊天
    2. Redis Memory
    3. Prompt管理
    4. Role角色系统
    5. LLM调用

    """

    def __init__(self):

        logger.info("初始化聊天应用")

        # Prompt管理

        self.prompt_manager = PromptManager()

        # LLM

        self.llm = ZhipuLLM()

        # Memory管理

        self.memory_manager = MemoryManager()

        logger.info("聊天应用初始化完成")

    def get_memory(self, session_id, role="default"):
        """
        获取Session Memory
        """

        memory = self.memory_manager.get_memory(session_id)

        self._init_system_prompt(session_id, memory, role)

        return memory

    def _init_system_prompt(self, session_id, memory, role="default"):
        """
        初始化系统Prompt

        只执行一次

        """

        messages = memory.get_messages()

        if messages:

            return

        # =====================
        # 基础系统Prompt
        # =====================

        system_prompt = self.prompt_manager.render("chat")

        memory.add_message("system", system_prompt)

        # =====================
        # 用户角色Prompt
        # =====================

        if role != "default":

            try:

                role_prompt = self.prompt_manager.get_role_prompt(role)

                memory.add_message("system", role_prompt)

                logger.info(f"角色Prompt加载成功:{role}")

            except Exception as e:

                logger.warning(f"角色Prompt加载失败:{e}")

        # 初始化后保存Redis

        self.memory_manager.save_memory(session_id, memory.get_messages())

    def chat(
        self, session_id, message=None, question=None, role="default", user_role=None
    ):
        """
        聊天入口


        兼容:

        message

        question

        role

        user_role


        """

        # =====================
        # 参数兼容
        # =====================

        if message is None:

            message = question

        if message is None:

            raise ValueError("消息不能为空")

        if user_role:

            role = user_role

        logger.info(f"开始聊天 session={session_id} role={role}")

        # =====================
        # 获取Memory
        # =====================

        memory = self.get_memory(session_id, role)

        # =====================
        # 用户消息
        # =====================

        memory.add_message("user", message)

        self.memory_manager.save_memory(session_id, memory.get_messages())

        # =====================
        # 调用LLM
        # =====================

        messages = memory.get_messages()

        answer = self.llm.chat(messages)

        # =====================
        # AI回复
        # =====================

        memory.add_message("assistant", answer)

        self.memory_manager.save_memory(session_id, memory.get_messages())

        logger.info(f"聊天完成 session={session_id}")

        return answer
