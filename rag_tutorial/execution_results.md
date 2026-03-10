# RAG 튜토리얼 실행 결과

## 1단계: 문서 로드 및 색인화

```
로드된 문서 수: 1
분할 후 청크 수: 63
색인된 문서 ID 수: 63
```

## 2단계: 방법 1 - 에이전트 + 검색 도구

### 쿼리: What is the standard method for Task Decomposition? Once you get the answer, look up common extensions of that method.

#### 1차 도구 호출

LLM이 검색이 필요하다고 판단하여 `retrieve_context` 도구를 호출했습니다.

```
Tool Calls:
  retrieve_context (call_hDc9SFO5SqTMw2NKKgBXqa9n)
   Call ID: call_hDc9SFO5SqTMw2NKKgBXqa9n
    Args:
      query: standard method for Task Decomposition
```

검색된 문서 내용:

```
Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'start_index': 2578}
Content: Task decomposition can be done (1) by LLM with simple prompting like
"Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?",
(2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel,
or (3) with human inputs.

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'start_index': 1638}
Content: Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique
for enhancing model performance on complex tasks. The model is instructed to "think step by step"
to utilize more test-time computation to decompose hard tasks into smaller and simpler steps.
Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities
at each step.
```

#### 2차 도구 호출

1차 결과를 바탕으로 CoT의 확장 기법을 추가 검색했습니다.

```
Tool Calls:
  retrieve_context (call_pwVjzx0ipXaaeLZ7OaeyDCog)
   Call ID: call_pwVjzx0ipXaaeLZ7OaeyDCog
    Args:
      query: common extensions of Chain of Thought (CoT) for task decomposition
```

#### 최종 답변

> The standard method for Task Decomposition is the **Chain of Thought (CoT)** prompting technique. In CoT, the model is instructed to "think step by step," breaking down complex tasks into smaller, manageable steps. This approach helps the model utilize more computation at test time and provides interpretability into its reasoning process.
>
> Common extensions of Chain of Thought include:
>
> - **Tree of Thoughts (ToT):** This method extends CoT by generating multiple reasoning possibilities at each step, forming a tree structure. The search through this tree can use breadth-first search (BFS) or depth-first search (DFS), with each state evaluated by a classifier or majority vote.
> - **LLM+P (LLM with external Planner):** Here, the task is translated into a formal planning language (PDDL), and an external classical planner generates a plan, which is then translated back into natural language. This is especially used for long-horizon planning in domains like robotics.
>
> These extensions aim to improve the robustness and flexibility of task decomposition beyond the linear step-by-step approach of standard CoT.

## 3단계: 방법 2 - 동적 프롬프트 (RAG Chain)

### 쿼리: What is task decomposition?

동적 프롬프트 미들웨어가 사용자 쿼리를 기반으로 관련 문서를 자동 검색하여 시스템 프롬프트에 주입했습니다.

#### 최종 답변

> Task decomposition is the process of breaking down a complicated or large task into smaller, more manageable sub-tasks or steps. This helps an agent (such as an AI or a human) to plan ahead and tackle complex problems more effectively.
>
> There are several ways to perform task decomposition:
>
> 1. **LLM with Simple Prompting:** Large Language Models (LLMs) can be prompted with instructions like "Steps for XYZ" or "What are the subgoals for achieving XYZ?" to generate a list of steps or subgoals.
> 2. **Task-Specific Instructions:** Using prompts tailored to the specific task, such as "Write a story outline" for novel writing, helps the model break down the task in a way that fits the domain.
> 3. **Human Inputs:** Humans can manually decompose tasks based on their understanding and experience.
> 4. **LLM+P (LLM with External Planner):** In this approach, the LLM translates the problem into a formal planning language (like PDDL), sends it to a classical planner to generate a plan, and then translates the plan back into natural language.
>
> **Related Techniques:**
> - **Chain of Thought (CoT):** A prompting technique where the model is instructed to "think step by step," helping it break down complex tasks into simpler steps.
> - **Tree of Thoughts:** An extension of CoT where multiple reasoning paths are explored at each step, forming a tree structure of possible solutions.

## 4단계: 방법 3 - 소스 문서 반환 (Middleware)

### 쿼리: What is task decomposition?

미들웨어가 검색된 문서를 사용자 메시지에 자동으로 추가하고, 소스 문서를 상태에 함께 저장했습니다.

#### 최종 답변

> **Task decomposition** is the process of breaking down a complex task into smaller, more manageable subtasks or steps. This makes it easier for an agent (such as a large language model, or LLM) to plan, execute, and track progress toward completing the overall goal.
>
> Task decomposition can be achieved in several ways:
>
> 1. **LLM with Simple Prompting:** By asking the LLM directly for steps or subgoals.
> 2. **Task-Specific Instructions:** Using prompts tailored to the domain.
> 3. **Human Inputs:** Humans can manually specify how to break down a task into subtasks.
> 4. **LLM+P (LLM plus Planner):** The LLM translates the problem into a formal planning language (PDDL), an external classical planner generates a plan, and the LLM translates the plan back into natural language.
>
> **Techniques for Task Decomposition:**
> - **Chain of Thought (CoT):** The LLM is prompted to "think step by step."
> - **Tree of Thoughts (ToT):** The LLM explores multiple possible reasoning paths at each step, creating a tree structure.

#### 참조한 소스 문서

```
참조한 소스 문서 수: 4

소스 1:
  시작 인덱스: 2578
  내용 미리보기: Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1."...

소스 2:
  시작 인덱스: 1638
  내용 미리보기: Component One: Planning# A complicated task usually involves many steps...

소스 3:
  시작 인덱스: 17734
  내용 미리보기: The AI assistant can parse user input to several tasks: [{"task": task, "id", task_id...

소스 4:
  시작 인덱스: 17352
  내용 미리보기: Illustration of how HuggingGPT works. (Image source: Shen et al. 2023)...
```
