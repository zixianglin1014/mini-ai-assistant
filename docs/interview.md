# Interview


# 项目一句话介绍

我设计并实现了一套基于 LLM + RAG 的企业级智能 AI 助手系统，
支持知识库问答、多轮对话、Memory管理以及Docker部署。


---

# 为什么设计RAG？


大模型存在：

1. 知识截止问题

2. 私有数据无法访问

3. 幻觉问题


RAG通过：

检索外部知识

+

上下文增强

+

LLM生成


提升回答准确性。


---

# RAG流程是什么？


用户问题

↓

Query处理

↓

Retriever召回

↓

Vector Search

+

Keyword Search

↓

Reranker排序

↓

Context拼接

↓

LLM生成


---

# 为什么使用Hybrid Search？


单纯向量搜索：

优点：

语义理解强


缺点：

精确关键词匹配不足


关键词搜索：

优点：

精准


缺点：

无法理解语义


所以结合两者。


---

# 为什么加入Reranker？


Retriever目标：

提高召回率。


Reranker目标：

提高准确率。


两者目标不同。


---

# 项目难点


## 1. RAG效果优化

解决：

- 文档切分
- Top-K选择
- Rerank


## 2. Memory管理

解决：

- 用户隔离
- Session管理
- Redis持久化


## 3. 工程部署

解决：

- Docker
- 环境配置
- 服务启动


---

# 如果继续优化


未来：

- Agent Tool Calling
- Streaming Response
- 用户权限系统
- 多知识库管理
- 监控系统
- Kubernetes部署
