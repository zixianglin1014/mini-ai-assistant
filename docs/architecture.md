# Mini AI Assistant Architecture


## 1. 项目整体架构


Mini AI Assistant采用分层架构设计，将AI能力、业务逻辑以及基础设施进行解耦。


整体架构：


```text
                        User Request


                             |

                             v


                     FastAPI API Layer


                             |

                             v


                  Application Business Layer


                 +-----------+-------------+

                 |                         |

                 v                         v


          Chat Application          RAG Application


                 |                         |

                 v                         v


              Memory              Retrieval Pipeline



                                           |

                    +----------------------+---------------------+

                    |                      |                     |

                    v                      v                     v


             Document Loader       Vector Search       Keyword Search


                                           |

                                           v


                                  Hybrid Retrieval


                                           |

                                           v


                                      Reranker


                                           |

                                           v


                                 Context Builder


                                           |

                                           v


                                         LLM


                                           |

                                           v


                                   Final Response

