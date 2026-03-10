"""
LangChain RAG 튜토리얼

이 스크립트는 LangChain의 최신 Agent API를 사용하여
RAG(Retrieval-Augmented Generation) 파이프라인을 구축합니다.

3가지 방식을 보여줍니다:
1. 에이전트 + 검색 도구 (Agent with Retrieval Tool)
2. 동적 프롬프트 방식 (Dynamic Prompt / RAG Chain)
3. 소스 문서 반환 (Middleware with Source Documents)
"""

import os
from typing import Any
import bs4
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import dynamic_prompt, ModelRequest, AgentMiddleware

load_dotenv()


# ============================================================
# 1단계: 문서 로드 및 전처리 (색인화)
# ============================================================
def step1_indexing():
    """웹에서 블로그 포스트를 로드하고 벡터 저장소에 색인화합니다."""
    print("=" * 60)
    print("1단계: 문서 로드 및 색인화")
    print("=" * 60)

    # BeautifulSoup으로 필요한 부분만 파싱
    bs4_strainer = bs4.SoupStrainer(
        class_=("post-title", "post-header", "post-content")
    )
    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
        bs_kwargs={"parse_only": bs4_strainer},
    )
    docs = loader.load()

    # 텍스트 분할
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )
    all_splits = text_splitter.split_documents(docs)

    # 벡터 저장소 생성
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    vector_store = InMemoryVectorStore(embeddings)
    document_ids = vector_store.add_documents(documents=all_splits)

    print(f"로드된 문서 수: {len(docs)}")
    print(f"분할 후 청크 수: {len(all_splits)}")
    print(f"색인된 문서 ID 수: {len(document_ids)}")

    return vector_store


# ============================================================
# 2단계: 방법 1 - 에이전트 + 검색 도구
# ============================================================
def step2_agent_with_tool(vector_store):
    """검색 도구를 사용하는 에이전트 방식의 RAG를 구현합니다."""
    print("\n" + "=" * 60)
    print("2단계: 방법 1 - 에이전트 + 검색 도구")
    print("=" * 60)

    @tool(response_format="content_and_artifact")
    def retrieve_context(query: str):
        """Retrieve information to help answer a query."""
        retrieved_docs = vector_store.similarity_search(query, k=2)
        serialized = "\n\n".join(
            (f"Source: {doc.metadata}\nContent: {doc.page_content}")
            for doc in retrieved_docs
        )
        return serialized, retrieved_docs

    model = init_chat_model("gpt-4.1", temperature=0)

    tools = [retrieve_context]
    # 블로그 포스트에서 컨텍스트를 검색하는 도구에 접근할 수 있습니다.
    # 사용자 쿼리에 답변하기 위해 도구를 사용하세요.
    prompt = (
        "You have access to a tool that retrieves context from a blog post. "
        "Use the tool to help answer user queries."
    )
    agent = create_agent(model, tools, system_prompt=prompt)

    # 멀티 스텝 쿼리 실행
    query = (
        "What is the standard method for Task Decomposition?\n\n"  # Task Decomposition의 표준 방법은 무엇인가?
        "Once you get the answer, look up common extensions of that method."  # 답을 얻으면, 그 방법의 일반적인 확장을 찾아봐.
    )

    print(f"\n쿼리: {query}")
    print("─" * 50)

    for event in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode="values",
    ):
        event["messages"][-1].pretty_print()

    return agent


# ============================================================
# 3단계: 방법 2 - 동적 프롬프트 (RAG Chain)
# ============================================================
def step3_dynamic_prompt_rag(vector_store):
    """동적 프롬프트를 사용하는 RAG 체인을 구현합니다."""
    print("\n" + "=" * 60)
    print("3단계: 방법 2 - 동적 프롬프트 (RAG Chain)")
    print("=" * 60)

    model = init_chat_model("gpt-4.1", temperature=0)

    @dynamic_prompt
    def prompt_with_context(request: ModelRequest) -> str:
        """Inject context into state messages."""
        last_query = request.state["messages"][-1].text
        retrieved_docs = vector_store.similarity_search(last_query)
        docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
        # 당신은 유용한 어시스턴트입니다. 응답에 다음 컨텍스트를 사용하세요.
        system_message = (
            "You are a helpful assistant. Use the following context in your response:"
            f"\n\n{docs_content}"
        )
        return system_message

    agent = create_agent(model, tools=[], middleware=[prompt_with_context])

    query = "What is task decomposition?"  # Task Decomposition이란 무엇인가?

    print(f"\n쿼리: {query}")
    print("─" * 50)

    for step in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()

    return agent


# ============================================================
# 4단계: 방법 3 - 소스 문서 반환 (Middleware)
# ============================================================
def step4_middleware_with_sources(vector_store):
    """미들웨어를 사용하여 소스 문서를 함께 반환하는 RAG를 구현합니다."""
    print("\n" + "=" * 60)
    print("4단계: 방법 3 - 소스 문서 반환 (Middleware)")
    print("=" * 60)

    model = init_chat_model("gpt-4.1", temperature=0)

    class State(AgentState):
        context: list[Document]

    class RetrieveDocumentsMiddleware(AgentMiddleware[State]):
        state_schema = State

        def before_model(self, state: AgentState) -> dict[str, Any] | None:
            last_message = state["messages"][-1]
            retrieved_docs = vector_store.similarity_search(last_message.text)
            docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
            augmented_message_content = (
                f"{last_message.text}\n\n"
                "Use the following context to answer the query:\n"
                f"{docs_content}"
            )
            return {
                "messages": [last_message.model_copy(update={"content": augmented_message_content})],
                "context": retrieved_docs,
            }

    agent = create_agent(
        model,
        tools=[],
        middleware=[RetrieveDocumentsMiddleware()],
    )

    query = "What is task decomposition?"  # Task Decomposition이란 무엇인가?

    print(f"\n쿼리: {query}")
    print("─" * 50)

    result = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )

    # 최종 답변
    print("\n답변:")
    result["messages"][-1].pretty_print()

    # 소스 문서 출력
    print(f"\n참조한 소스 문서 수: {len(result['context'])}")
    for i, doc in enumerate(result["context"]):
        print(f"\n소스 {i + 1}:")
        print(f"  시작 인덱스: {doc.metadata.get('start_index', 'N/A')}")
        print(f"  내용 미리보기: {doc.page_content[:100]}...")

    return agent


# ============================================================
# 메인 실행
# ============================================================
def main():
    vector_store = step1_indexing()
    step2_agent_with_tool(vector_store)
    step3_dynamic_prompt_rag(vector_store)
    step4_middleware_with_sources(vector_store)

    print("\n" + "=" * 60)
    print("튜토리얼 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()
