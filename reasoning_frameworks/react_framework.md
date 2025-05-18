### ReAct Framework

**Definition:** Alternating reasoning and action steps for interactive problem solving, especially when external tools are required.

**Prompt Template:**
```
To solve this problem, alternate between:
1. Thought: Reason about the current state and next step
2. Action: Perform a specific operation
3. Observation: Note the result of the action
4. Repeat until you reach a conclusion

[Problem statement]
```

**Example:**
```
Using the ReAct framework, gather information about recent population trends in Austin, Texas.
Start with:
1. Thought: What data sources should I consult?
2. Action: [Describe search]
3. Observation: [Describe results]
4. Thought: How should I refine the search?
```

**Best For:**
- Tasks requiring tool use or external information
- Multi-step information gathering
- Complex planning scenarios

**Limitations:**
- Overkill for simple, one-step queries
- Requires careful separation of thoughts and actions

**Advantages:**
- Makes reasoning explicit and auditable
- Breaks complex tasks into manageable steps
- Combines decision-making with execution

**Tips for Success:**
- Be specific about allowed actions
- Include clear stopping conditions
