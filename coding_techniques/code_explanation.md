### Code Explanation Prompts

**Definition:** Getting the model to describe what a piece of code does, step by step.

**Prompt Template:**
```
Explain the following [language] code line by line:
[code snippet]
```

**Example:**
```
Explain the following Python function line by line:

def add(a, b):
    return a + b
```

**Tips:**
- Provide the code in a fenced block for clarity
- Mention the target audience (e.g., beginner, advanced)

**Best For:**
- Understanding legacy or poorly documented code
- Creating educational materials

**Limitations:**
- Explanations may omit edge-case behavior
- Complex code can lead to lengthy outputs

**Advantages:**
- Helps onboard new developers quickly
- Reveals implicit logic in unfamiliar code
