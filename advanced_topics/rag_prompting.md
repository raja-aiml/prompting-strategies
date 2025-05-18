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

**Example:**
```
Context information:
"Paris is the capital of France."

Using ONLY the information above, answer the following question.
Question: "What city is the capital of France?"
```

**Best For:**
- Tasks requiring up-to-date or specialized knowledge
- Scenarios where the base model lacks necessary facts

**Limitations:**
- Quality depends on the retrieved documents
- Longer prompts may approach token limits

**Advantages:**
- Reduces hallucinations by grounding responses in source texts
- Allows dynamic updates without retraining the model
