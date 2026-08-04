from .base import PromptTemplate

TITLE_PROMPT = PromptTemplate("""
你是一名内容运营专家。


请根据下面文章生成5个标题：

{text}


要求：

1. 标题吸引用户点击

2. 每个标题不超过20字

3. 输出中文

""")
