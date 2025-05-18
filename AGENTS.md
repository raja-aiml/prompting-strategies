# AGENTS Instructions for Prompting Strategies Repository

This repository documents advanced template-driven prompting techniques for large language models (LLMs). The content was derived from the "Advanced Template-Driven Prompting Strategies" guide provided by the user. Use this file as a quick reference for contributors.

## Key Prompting Techniques
- **Zero-shot Prompting** – Direct instructions without examples.
- **Few-shot Prompting** – 2-5 demonstrations that establish the pattern.
- **Multi-shot Prompting** – Extensive examples to cover edge cases.
- **Chain-of-Thought** – Step-by-step reasoning before final answer.
- **Tree-of-Thought** – Explore multiple reasoning paths in parallel.
- **Step-back Prompting** – Meta-cognitive reflection prior to answering.
- **Self-consistent Prompting** – Generate multiple solutions and synthesize the best.
- **Analogy-based Prompting** – Use familiar concepts to explain abstract ideas.
- **Role-based Prompting** – Adopt a specific expert persona.
- **ReAct Framework** – Alternate between reasoning and action steps.

## Best Practices
1. **Template Selection** – Match the prompting technique to task complexity.
2. **Provide Context** – Include relevant background and constraints.
3. **Explicit Instructions** – Clearly state format and approach.
4. **Iterate** – Test prompts with varied inputs and refine.
5. **Combine Methods** – Use hybrid techniques (e.g., Few-shot + CoT) for complex tasks.

## Evaluation Guidelines
- Measure responses based on completion, accuracy, reasoning quality, format adherence, and efficiency.
- When prompts fail, iterate by adding constraints or examples as outlined in the troubleshooting section of the guide.

