### System Prompting

**Definition:** Setting overarching instructions that guide the model's behavior across an entire session.

**Prompt Template:**
```
You are [desired persona]. Follow these rules:
1. [Guideline 1]
2. [Guideline 2]
...
```

**Example:**
```
You are a concise assistant. Always answer in one short paragraph and avoid speculation.
```

**Best For:**
- Establishing tone and style for multi-turn conversations
- Enforcing global restrictions or safety rules

**Limitations:**
- Instructions may be forgotten in very long conversations
- Conflicts between system and user messages can confuse the model

**Advantages:**
- Provides consistent behavior across requests
- Useful for customizing voice or style

**Tips for Success:**
- Keep system prompts short but explicit
- Restate critical guidelines if the conversation is long
