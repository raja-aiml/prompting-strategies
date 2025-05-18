### Contextual Prompting

**Definition:** Providing background information or reference materials so the model can better understand and respond to the request.

**Prompt Template:**
```
Context information:
[background text]

Question: [user query]
```

**Example:**
```
Context information:
- Product: WidgetPro 2.0
- Key features: longer battery life, waterproof design

Question: Write a short advertisement for this product.
```

**Best For:**
- Situations where the model lacks necessary background knowledge
- Keeping long-running conversations consistent

**Limitations:**
- Consumes token budget
- Context must be relevant and concise

**Advantages:**
- Reduces ambiguity
- Ensures output aligns with known facts or constraints

**Tips for Success:**
- Place critical context near the beginning of the prompt
- Remove unnecessary details to save tokens
