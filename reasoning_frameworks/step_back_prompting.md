### Step-back Prompting

**Definition:** Encouraging the model to take a broader perspective or reflect on assumptions before producing a final answer.

**Prompt Template:**
```
[Problem statement]

Before answering, take a step back and consider:
1. What is the broader context of this problem?
2. What general principles or frameworks apply here?
3. What assumptions might be incorrect?

After this reflection, solve the problem.
```

**Example:**
```
A startup must decide whether to focus on growing its user base or increasing revenue from existing users.

Before answering, take a step back and consider:
1. What business principles might apply?
2. What information is missing?
3. What assumptions am I making?

After this reflection, provide a recommendation with reasoning.
```

**Best For:**
- Strategic decisions and high-level analysis
- Avoiding tunnel vision on complex issues

**Limitations:**
- Adds extra steps that may not be necessary for simple tasks
- Broad reflections consume additional tokens

**Advantages:**
- Surfaces hidden assumptions
- Produces more nuanced, thoughtful responses

**Tips for Success:**
- Include specific reflection questions
- Allow space for the model to reason before answering
