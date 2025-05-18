### Self-consistent Prompting

**Definition:** Generating multiple independent solutions to a problem and then selecting or synthesizing the most consistent answer.

**Prompt Template:**
```
[Problem statement]

Generate 5 independent solutions to this problem without referring to previous solutions. Then identify the most consistent answer and explain why it's likely correct.
```

**Example:**
```
[Problem statement]

Generate 5 different approaches, evaluate them, and present the consensus answer.
```

**Best For:**
- High-stakes decisions requiring reliability
- Problems with potential for error
- Mathematical or logical questions with verifiable answers

**Limitations:**
- Not suited for creative tasks with no single right answer
- Consumes more tokens due to multiple attempts

**Advantages:**
- Reduces variance and hallucinations
- Provides a confidence measure through consensus

**Tips for Success:**
- Request distinct approaches for each attempt
- Use an odd number of solutions to avoid ties
