### Chain-of-Thought (CoT) Prompting

**Definition:** Guiding the model to reason through a problem step by step before providing the final answer.

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
- Mathematical reasoning and logic puzzles
- Multi-step analytical problems

**When NOT to Use:**
- Simple factual queries
- Creative generation tasks
- When token efficiency is critical

**Advantages:**
- Improves reasoning accuracy
- Makes the thought process explicit and auditable
- Reduces errors in complex calculations

**Tips for Success:**
- Request labeled steps or numbered reasoning
- For difficult problems, estimate the number of steps needed
