# Technical Details


# 1. RAG Pipeline设计


## 文档处理

支持：

- PDF
- DOCX
- TXT


流程：

Document Loader

↓

Text Splitter

↓

Embedding

↓

Vector Database


---

# 2. Retrieval设计


采用 Hybrid Search:

Vector Search

+

Keyword Search


原因：

向量检索擅长语义理解

关键词检索擅长精确匹配


结合提升召回率。


---

# 3. Rerank设计


初始Retriever返回Top-K文档。

随后使用Reranker重新排序：

Query

↓

Candidate Documents

↓

Cross Encoder

↓

Relevant Documents


提升上下文质量。


---

# 4. Memory设计


Memory分层：

短期：

Conversation History


长期：

User Profile


存储：

JSON

Redis


---

# 5. Prompt设计


Prompt模块化：

System Prompt

Chat Prompt

QA Prompt

Summary Prompt


实现业务逻辑和Prompt解耦。


---

# 6. 服务架构


Backend:

FastAPI


Model:

GLM


Storage:

Redis

Vector Database


Deployment:

Docker Compose
