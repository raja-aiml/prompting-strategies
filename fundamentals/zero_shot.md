### Zero-shot Prompting

**Definition:** Direct instruction without examples, relying solely on the model's pretrained knowledge.

**Prompt Template:**
```
[Task instruction]

[Input]
```

**Example:**
```
Summarize the following article in three concise paragraphs that capture the main points.

[Article text...]
```

**Best For:**
- Well-defined tasks within the model's capabilities
- Simple classification or generation tasks
- When prompt length must be minimized

**When NOT to Use:**
- Tasks involving novel formats the model may not understand
- Complex reasoning problems
- Requests that require a specific output structure

**Advantages:**
- Minimal prompt engineering effort
- Conserves token usage
- Fast to implement

**Tips for Success:**
- Be explicit about the desired output format
- Include clear evaluation criteria
- Use concise language
