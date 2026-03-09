"""
LangChain 의미 검색(Semantic Search) 튜토리얼

이 스크립트는 LangChain의 핵심 추상화를 활용하여
PDF 문서에 대한 의미 검색 엔진을 구축하는 전체 파이프라인을 보여줍니다.

핵심 개념:
- 문서 로더 (Document Loader)
- 텍스트 분할 (Text Splitter)
- 임베딩 (Embeddings)
- 벡터 저장소 (Vector Store)
- 리트리버 (Retriever)
"""

import os
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

# .env 파일에서 환경변수 로드
load_dotenv()


# ============================================================
# 1단계: 문서(Document) 이해하기
# ============================================================
def step1_understand_documents():
    """Document 객체의 기본 구조를 이해합니다."""
    print("=" * 60)
    print("1단계: Document 객체 이해하기")
    print("=" * 60)

    documents = [
        Document(
            page_content="Dogs are great companions, known for their loyalty and friendliness.",
            metadata={"source": "mammal-pets-doc"},
        ),
        Document(
            page_content="Cats are independent pets that often enjoy their own space.",
            metadata={"source": "mammal-pets-doc"},
        ),
    ]

    for i, doc in enumerate(documents):
        print(f"\n문서 {i + 1}:")
        print(f"  내용: {doc.page_content}")
        print(f"  메타데이터: {doc.metadata}")

    return documents


# ============================================================
# 2단계: PDF 문서 로드
# ============================================================
def step2_load_pdf(pdf_path: str):
    """PyPDFLoader를 사용하여 PDF 문서를 로드합니다."""
    print("\n" + "=" * 60)
    print("2단계: PDF 문서 로드")
    print("=" * 60)

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    print(f"\n로드된 문서 수: {len(docs)}")
    print(f"첫 번째 페이지 내용 (앞 200자):\n{docs[0].page_content[:200]}")
    print(f"첫 번째 페이지 메타데이터: {docs[0].metadata}")

    return docs


# ============================================================
# 3단계: 텍스트 분할
# ============================================================
def step3_split_documents(docs):
    """RecursiveCharacterTextSplitter로 문서를 청크로 분할합니다."""
    print("\n" + "=" * 60)
    print("3단계: 텍스트 분할")
    print("=" * 60)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )
    all_splits = text_splitter.split_documents(docs)

    print(f"\n원본 문서 수: {len(docs)}")
    print(f"분할 후 청크 수: {len(all_splits)}")
    print(f"\n첫 번째 청크 길이: {len(all_splits[0].page_content)}자")
    print(f"첫 번째 청크 메타데이터: {all_splits[0].metadata}")

    return all_splits


# ============================================================
# 4단계: 임베딩 생성
# ============================================================
def step4_create_embeddings():
    """OpenAI 임베딩 모델을 초기화합니다."""
    print("\n" + "=" * 60)
    print("4단계: 임베딩 모델 초기화")
    print("=" * 60)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    # 임베딩 테스트
    sample_text = "LangChain is a framework for building LLM applications."
    vector = embeddings.embed_query(sample_text)

    print(f"\n임베딩 모델: text-embedding-3-large")
    print(f"샘플 텍스트: {sample_text}")
    print(f"벡터 차원: {len(vector)}")
    print(f"벡터 앞 5개 값: {vector[:5]}")

    return embeddings


# ============================================================
# 5단계: 벡터 저장소 생성 및 문서 추가
# ============================================================
def step5_create_vector_store(all_splits, embeddings):
    """InMemoryVectorStore에 문서 청크를 저장합니다."""
    print("\n" + "=" * 60)
    print("5단계: 벡터 저장소 생성")
    print("=" * 60)

    vector_store = InMemoryVectorStore(embeddings)
    ids = vector_store.add_documents(documents=all_splits)

    print(f"\n벡터 저장소에 추가된 문서 수: {len(ids)}")

    return vector_store


# ============================================================
# 6단계: 유사도 검색
# ============================================================
def step6_similarity_search(vector_store):
    """벡터 저장소에서 유사도 검색을 수행합니다."""
    print("\n" + "=" * 60)
    print("6단계: 유사도 검색")
    print("=" * 60)

    # 기본 유사도 검색
    query = "How many distribution centers does Nike have?"
    results = vector_store.similarity_search(query)

    print(f"\n쿼리: {query}")
    print(f"검색 결과 수: {len(results)}")
    for i, doc in enumerate(results):
        print(f"\n--- 결과 {i + 1} ---")
        print(f"내용: {doc.page_content}")
        print(f"메타데이터: {doc.metadata}")

    # 점수 포함 유사도 검색
    print("\n\n[점수 포함 유사도 검색]")
    query2 = "What was Nike's revenue?"
    results_with_score = vector_store.similarity_search_with_score(query2)

    print(f"쿼리: {query2}")
    for i, (doc, score) in enumerate(results_with_score):
        print(f"  결과 {i + 1}: 점수={score:.4f} | {doc.page_content}")

    return results


# ============================================================
# 7단계: 리트리버 사용
# ============================================================
def step7_use_retriever(vector_store):
    """VectorStoreRetriever를 생성하고 사용합니다."""
    print("\n" + "=" * 60)
    print("7단계: 리트리버 사용")
    print("=" * 60)

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 1},
    )

    # 단일 쿼리
    query = "When was Nike incorporated?"
    results = retriever.invoke(query)

    print(f"\n쿼리: {query}")
    print(f"검색 결과 수: {len(results)}")
    for doc in results:
        print(f"내용: {doc.page_content}")

    # 배치 쿼리
    print("\n\n[배치 쿼리]")
    batch_queries = [
        "How many distribution centers does Nike have?",
        "What was Nike's revenue?",
    ]
    batch_results = retriever.batch(batch_queries)

    for query, results in zip(batch_queries, batch_results):
        print(f"\n쿼리: {query}")
        print(f"  결과: {results[0].page_content}")


# ============================================================
# 메인 실행
# ============================================================
def main():
    pdf_path = "example_data/nke-10k-2023.pdf"

    if not os.path.exists(pdf_path):
        print(f"[오류] PDF 파일이 없습니다: {pdf_path}")
        print("example_data/ 폴더에 PDF 파일을 넣어주세요.")
        return

    # 각 단계 실행
    step1_understand_documents()
    docs = step2_load_pdf(pdf_path)
    all_splits = step3_split_documents(docs)
    embeddings = step4_create_embeddings()
    vector_store = step5_create_vector_store(all_splits, embeddings)
    step6_similarity_search(vector_store)
    step7_use_retriever(vector_store)

    print("\n" + "=" * 60)
    print("튜토리얼 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()