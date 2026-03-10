# Agentic RAG 튜토리얼 실행 결과

## 1단계: 문서 로드 및 전처리

```
로드된 문서 수: 3
분할 후 청크 수: 538
```

## 2단계: 벡터 저장소 및 검색 도구 생성

```
검색 도구 생성 완료: retrieve_blog_posts
```

## 3단계: 에이전트 노드 정의

```
노드 정의 완료: generate_query_or_respond, grade_documents, rewrite_question, generate_answer
```

## 4단계: 그래프 조립

```
그래프 조립 완료!
워크플로우: 질문 → 검색 판단 → 검색 → 문서 평가 → 답변/재작성
```

## 5단계: 에이전트 실행

### 쿼리: What does Lilian Weng say about types of reward hacking?

#### Node: generate_query_or_respond

LLM이 검색이 필요하다고 판단하여 `retrieve_blog_posts` 도구를 호출했습니다.

```
Tool Calls:
  retrieve_blog_posts (call_f8WyawQGfoWU9oToPN8NsLLP)
   Call ID: call_f8WyawQGfoWU9oToPN8NsLLP
    Args:
      query: types of reward hacking
```

#### Node: retrieve

검색된 문서 내용:

```
Detecting Reward Hacking#

In-Context Reward Hacking#

(Note: Some work defines reward tampering as a distinct category of misalignment behavior
from reward hacking. But I consider reward hacking as a broader concept here.)
At a high level, reward hacking can be categorized into two types:
environment or goal misspecification, and reward tampering.

Why does Reward Hacking Exist?#
```

문서 평가 결과: **관련 있음 (yes)** → 답변 생성으로 이동

#### Node: generate_answer

최종 답변:

> Lilian Weng categorizes reward hacking into two types: **environment or goal misspecification**, and **reward tampering**. She notes that some work treats reward tampering as a separate category, but she considers it under the broader concept of reward hacking. These categories help explain different ways agents can exploit flaws in reward systems.
