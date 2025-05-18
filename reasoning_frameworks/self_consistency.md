### Self-consistent Prompting

**Definition:** Generating multiple independent solutions to the same problem, then synthesizing or selecting the most consistent answer.

**Prompt Template:**
```
[Problem statement]

Generate 5 independent solutions to this problem without referring to previous solutions. Then, identify the most consistent answer across these solutions and explain why it's likely correct.
```

**Example:**
```
Calculate the area of a triangle with sides of length 13, 14, and 15.

Generate 5 independent solutions to this problem without referring to previous solutions. Then, identify the most consistent answer across these solutions and explain why it's likely correct.
```

**Best For:**
- High-stakes decisions requiring reliability
- Problems with potential for error
- Mathematical or logical problems with verifiable answers

**Limitations:**
- Creative tasks with no "correct" answer
- Simple queries with straightforward answers
- When token usage must be minimized

**Advantages:**
- Reduces variance and hallucinations
- Improves accuracy through consensus
- Provides confidence level in answers

**Tips for Success:**
- Request explicit different approaches for each solution
- Ask for evaluation of confidence in each solution
- Use odd numbers of attempts (3, 5) to avoid ties
