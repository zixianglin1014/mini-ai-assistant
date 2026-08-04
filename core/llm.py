from openai import OpenAI

from configs.settings import (BASE_URL, MAX_TOKENS, MODEL_NAME, TEMPERATURE,
                              ZHIPU_API_KEY, settings)
from utils.logger import logger


class ZhipuLLM:
    """
    智谱LLM客户端
    """

    def __init__(self):

        if not ZHIPU_API_KEY:

            raise ValueError("未读取到 ZHIPU_API_KEY，请检查配置文件")

        self.client = OpenAI(api_key=settings.ZHIPU_API_KEY, base_url=BASE_URL)

        self.model = MODEL_NAME

        logger.info("智谱LLM客户端初始化成功")

    def chat(self, prompt, system_prompt=None):
        """
        调用智谱模型
        """

        logger.info("正在请求智谱模型")

        try:

            if isinstance(prompt, list):

                messages = prompt

            else:

                messages = []

                if system_prompt:

                    messages.append({"role": "system", "content": system_prompt})

                messages.append({"role": "user", "content": prompt})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
            )

            answer = response.choices[0].message.content

            logger.info("模型返回成功")

            return answer

        except Exception as e:

            logger.error(f"智谱模型调用失败:{e}")

            raise e
