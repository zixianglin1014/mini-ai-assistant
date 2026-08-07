# Mini AI Assistant

基于 **LLM + RAG + Memory + Redis + FastAPI + Docker** 架构实现的企业级智能 AI 助手系统。

本项目模拟真实生产环境中的 **AI Agent / 智能客服 / 企业知识库问答系统**，实现完整的 AI 应用链路：

```
用户请求
    |
    v
FastAPI 服务
    |
    v
业务应用层
    |
    +----------------+
    |                |
    v                v
 对话系统          RAG系统
    |                |
    v                v
 Memory        文档检索 Pipeline
                     |
                     v
             Hybrid Search
                     |
                     v
              Reranker排序
                     |
                     v
              Prompt构建
                     |
                     v
                  LLM
                     |
                     v
               最终回答
```


---

# 项目亮点

- 基于大语言模型构建智能对话系统
- 完整实现 RAG（Retrieval-Augmented Generation）知识增强流程
- 支持 PDF / DOCX / TXT 文档解析
- 支持文本切分与 Embedding 向量化
- 支持 Chroma 向量数据库
- 支持 Vector Search + Keyword Search 混合检索
- 集成 BGE Reranker 提升检索准确率
- 支持多轮上下文 Memory
- 支持 Redis 持久化存储
- Prompt 模块化管理
- FastAPI 服务化部署
- Docker 容器化部署
- Pytest 自动化测试


---

# 技术架构


```
                    User Request

                         |
                         v

                  FastAPI Server

                         |
                         v

              Application Layer

          +--------------+--------------+

          |                             |

          v                             v

 Chat Application              RAG Application


          |                             |

          v                             v

      Memory                 Retrieval Pipeline


                                        |

                +-----------------------+------------------+

                |                       |                  |

                v                       v                  v

          Document Loader        Vector Search      Keyword Search


                                        |

                                        v

                                  Hybrid Retrieval


                                        |

                                        v

                                   Reranker


                                        |

                                        v

                              Context Construction


                                        |

                                        v

                                      LLM


                                        |

                                        v

                                Final Response

```


---

# 核心功能


# 1. LLM 对话系统


封装大语言模型调用能力，实现统一模型接口。


功能：

- 模型调用封装
- 参数统一管理
- Temperature控制
- Token限制
- Prompt管理


当前支持：

- 智谱 GLM 系列模型


---

# 2. RAG 知识库增强问答


完整实现 Retrieval-Augmented Generation Pipeline：


```
Document

    |

    v

Document Loader

    |

    v

Text Splitter

    |

    v

Embedding

    |

    v

Vector Database

    |

    v

Retriever

    |

    v

Reranker

    |

    v

LLM Generation

```


支持：

- TXT 文档加载
- PDF 文档加载
- DOCX 文档加载
- 文档切片
- Embedding生成
- Chroma向量存储
- Top-K召回
- Context构建


---

# 3. Hybrid Search 混合检索


为了提升 RAG 检索效果，实现：

## Vector Search


基于语义向量相似度：

优势：

- 理解用户语义
- 支持自然语言查询


---

## Keyword Search


基于关键词匹配：

优势：

- 提升精准关键词命中
- 补充向量检索不足


---

整体流程：

```
                 Query

                   |

        +----------+----------+

        |                     |

        v                     v


 Vector Retrieval       Keyword Retrieval


        |                     |

        +----------+----------+

                   |

                   v

            Candidate Documents

                   |

                   v

                Reranker

                   |

                   v

             Final Context

```


---

# 4. Reranker 重排序


引入 Cross Encoder Reranker。


流程：

```
Query

 |

Retriever

 |

Top-K Documents

 |

Reranker

 |

Top-N Documents

 |

LLM

```


作用：

- 提升文档相关性
- 降低无关上下文干扰
- 提升最终回答质量


---

# 5. Memory 多轮对话系统


支持用户级上下文管理。


能力：

- 保存历史对话
- 用户Session管理
- 上下文拼接
- 长短期记忆管理


Memory结构：


```
User

 |

 +---- Conversation History

 |

 +---- User Profile

 |

 +---- Preferences

```


存储方式：

- JSON Memory
- Redis Memory


---

# 6. Prompt Engineering


实现 Prompt 模块化管理。


包含：

- System Prompt
- Chat Prompt
- QA Prompt
- Summary Prompt
- Role Prompt


优势：

- Prompt 与业务代码解耦
- 易维护
- 易扩展
- 支持不同任务模板


---

# 7. Redis缓存系统


支持：

- 请求缓存
- 对话缓存
- Memory持久化


结构：

```
Redis

 |

 +---- User Memory

 |

 +---- Conversation Cache

 |

 +---- Response Cache

```


---

# 项目结构


```
mini-ai-assistant

├── api
│   ├── server.py              # FastAPI入口
│   ├── chat.py                # Chat接口
│   ├── rag.py                 # RAG接口
│   └── model.py               # 模型接口
│

├── application
│   ├── chat_app.py            # 对话业务层
│   └── rag_app.py             # RAG业务层
│

├── core
│   ├── llm.py                 # LLM封装
│   ├── embedding.py           # Embedding
│   ├── vector_store.py        # 向量数据库
│   ├── reranker.py            # Reranker
│   ├── rag.py                 # RAG核心流程
│   ├── memory.py              # Memory
│   ├── cache.py               # Cache
│   ├── text_splitter.py       # 文本切分
│   └── prompt_manager.py      # Prompt管理
│

├── configs
│   └── settings.py            # 配置管理
│

├── tests                       # 测试代码

├── deploy
│   ├── start.sh               # 启动脚本
│   └── stop.sh                # 停止脚本
│

├── Dockerfile

└── docker-compose.yml

```


---

# API接口


## Health Check


请求：

```
GET /health
```


响应：

```json
{
    "status": "ok"
}
```


---

# Chat接口


请求：

```
POST /chat
```


Request:


```json
{
    "user_id": "user001",
    "message": "介绍一下这个项目"
}
```


Response:


```json
{
    "answer": "这是一个基于LLM+RAG架构实现的智能助手系统..."
}
```


---

# RAG问答接口


请求：

```
POST /rag
```


Request:

```json
{
    "query": "项目使用了哪些技术?"
}
```


Response:

```json
{
    "answer": "项目采用Python、FastAPI、RAG、Redis等技术..."
}
```


---

# 本地运行


## 1. Clone项目


```bash
git clone git@github.com:zixianglin1014/mini-ai-assistant.git

cd mini-ai-assistant
```


---

## 2. 创建Python环境


```bash
conda create -n ai-env python=3.12

conda activate ai-env
```


---

## 3. 安装依赖


```bash
pip install -r requirements.txt
```


---

## 4. 配置环境变量


复制配置文件：

```bash
cp configs/env/.env.example configs/env/.env.dev
```


修改：

```env
ZHIPU_API_KEY=your_api_key

MODEL_NAME=glm-4-flash
```


---

## 5. 启动服务


方式一：

```bash
python main.py
```


方式二：

```bash
uvicorn api.server:app --host 0.0.0.0 --port 8000
```


---

# Docker部署


## 构建镜像


```bash
docker compose build
```


## 启动服务


```bash
docker compose up -d
```


## 查看运行状态


```bash
docker ps
```


## 停止服务


```bash
docker compose down
```


---

# 测试


执行：

```bash
pytest -v
```


当前测试结果：

```
2 passed
```


覆盖：

- RAG流程测试
- LLM调用测试
- 文档加载测试
- Embedding测试
- Prompt测试
- API测试


---

# 技术栈


| 分类 | 技术 |
|-|-|
| 编程语言 | Python 3.12 |
| Web框架 | FastAPI |
| LLM | 智谱 GLM |
| RAG | 自研RAG Pipeline |
| Embedding | BGE-small-zh |
| Vector Database | Chroma |
| Reranker | BGE-Reranker |
| Cache | Redis |
| Testing | Pytest |
| Deployment | Docker |
| Logging | Loguru |


---

# 项目难点与解决方案


## 1. RAG准确率优化


问题：

单纯向量搜索容易召回语义相关但答案无关的数据。


解决：

- Hybrid Search
- Reranker二次排序
- Context优化


---

## 2. Memory设计


问题：

多轮对话需要保存上下文，同时控制历史长度。


解决：

- 用户级Memory
- Redis持久化
- 历史记录管理


---

## 3. AI应用工程化


问题：

AI项目不仅需要模型调用，还需要稳定服务。


解决：

- FastAPI服务化
- Docker部署
- 配置隔离
- 日志系统
- 自动化测试


---

# Future Improvement


后续计划：

- Streaming Response流式输出
- Agent Tool Calling
- Function Calling
- LangGraph Agent Workflow
- RAG Evaluation体系
- Kubernetes部署
- 多Agent协作架构


---

# Author


**zixianglin1014**


GitHub:

https://github.com/zixianglin1014/mini-ai-assistant


---

# License


MIT License
