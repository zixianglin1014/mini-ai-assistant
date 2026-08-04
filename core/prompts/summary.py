from .base import PromptTemplate

SUMMARY_PROMPT = PromptTemplate("""
你是一名专业文章分析助手。


请总结下面文本：

{text}


要求：

1. 输出100字以内总结

2. 提取3个关键词

3. 使用中文回答

""")
