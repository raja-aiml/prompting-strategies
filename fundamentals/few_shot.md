### Few-shot Prompting

**Definition:** Providing 2-5 examples that demonstrate the input-output pattern expected from the model.

**Prompt Template:**
```
[Task instruction]

Example 1:
Input: [input example 1]
Output: [output example 1]

Example 2:
Input: [input example 2]
Output: [output example 2]

Now complete this:
Input: [actual input]
Output:
```

**Example:**
```
Classify these reviews as positive, negative, or neutral.

Example 1:
Input: "This product exceeded my expectations!"
Output: Positive

Example 2:
Input: "Worked as advertised but shipping was slow."
Output: Neutral

Now classify this:
Input: "Broke after two uses."
Output:
```

**Best For:**
- Establishing consistent output format
- Clarifying subjective judgment criteria
- Tasks with clear patterns

**When NOT to Use:**
- When examples would consume too many tokens
- When the task is easily understood without examples

**Advantages:**
- Improves consistency in model responses
- Reduces need for additional clarification

**Tips for Success:**
- Use diverse examples covering edge cases
- Order examples from simple to complex
