### Retrieval-Augmented Generation (RAG) Prompting

**Definition:** Combining external knowledge retrieval with generation prompts.

**Prompt Template:**
```
Context information:
[Retrieved document chunks]

Using ONLY the information above, answer the following question.
Question: [User query]
```

**Best Practices:**
- Clearly separate retrieved context from instructions
- Specify how to handle missing information
- Consider chunk boundaries when designing prompts
