### ReAct Framework

**Definition:** Alternating reasoning and action steps for interactive problem solving.

**Prompt Template:**
```
To solve this problem, alternate between:
1. Thought: Reasoning about the current state and what to do next
2. Action: A specific operation to perform
3. Observation: The result of the action
4. Repeat until reaching a conclusion

[Problem statement]
```

**Example:**
```
Using the ReAct framework (Reason-Act-Observe), help me find information about the population trends in Austin, Texas over the last decade.

Start by:
1. Thought: What information do I need and where might I find it?
2. Action: [Describe search or action to take]
3. Observation: [What would be observed from this action]
4. Continue this pattern until you've gathered comprehensive information.
```

**Best For:**
- Tasks requiring tool use (search, calculations)
- Multi-step information gathering
- Problems requiring environmental interaction
- Complex planning scenarios

**Limitations:**
- Simple, one-step queries
- Purely creative tasks
- When the full context is already available

**Advantages:**
- Combines decision-making with execution
- Makes reasoning explicit and auditable
- Breaks complex tasks into manageable steps

**Tips for Success:**
- Clearly separate thought, action, and observation steps
- Be specific about available actions
- Allow for revision of approach based on observations
