### Chain-of-Thought (CoT) Prompting

**Definition:** Instructing the model to reason through a problem step by step before providing the final answer.

**Prompt Template:**
```
[Problem statement]

Think through this problem step by step to find the correct answer.
```

**Example:**
```
A store sells notebooks for $3.50 each and pens for $1.25 each. If I bought 4 notebooks and some pens for a total of $21.50, how many pens did I buy?

Think through this problem step by step to find the correct answer.
```

**Best For:**
- Mathematical reasoning
- Logic puzzles
- Multi-step problems
- Analytical tasks

**Limitations:**
- Simple factual queries
- Creative generation tasks
- When token efficiency is critical

**Advantages:**
- 20-40% improvement on reasoning tasks
- Makes reasoning transparent and auditable
- Reduces errors in complex calculations

**Tips for Success:**
- Explicitly ask for labeled steps
- For complex problems, suggest estimated number of steps
- Combine with few-shot examples of good reasoning
