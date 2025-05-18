### Tree-of-Thought (ToT) Prompting

**Definition:** Exploring multiple reasoning paths simultaneously before selecting the most promising one.

**Prompt Template:**
```
[Problem statement]

Consider multiple approaches to solving this problem:
1. First explore approach A...
2. Then explore approach B...
3. Finally explore approach C...

For each approach, evaluate its merits and limitations. Then select the most promising approach and use it to solve the problem.
```

**Example:**
```
Solve this logic puzzle: "Five people of different nationalities live in five consecutive houses on a street. Each person has a different profession, drives a different car, and keeps a different pet. Using the clues below, determine who keeps the fish."

[clues...]

Consider three different approaches to solving this puzzle:
1. First, create a grid and use elimination based on the given clues
2. Next, try starting with the most restrictive clues and build connections
3. Finally, try assuming each person has the fish and evaluate if it leads to contradictions

For each approach, work through the initial steps, evaluate its effectiveness, then choose the best approach to solve the puzzle completely.
```

**Best For:**
- Problems with multiple possible solution paths
- Scenarios requiring comparison of different approaches
- Complex decision-making with trade-offs

**Limitations:**
- Simple problems with obvious solution methods
- When limited by token context window
- Time-sensitive applications needing quick responses

**Advantages:**
- Prevents getting stuck in reasoning dead-ends
- Often finds more optimal solutions
- Models human expert problem-solving more closely

**Tips for Success:**
- Explicitly define how to evaluate each approach
- Ensure branches are distinct and meaningfully different
- Request explicit comparison of pros/cons for each approach
