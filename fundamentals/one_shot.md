### One-shot Prompting

**Definition:** Providing a single example demonstration to establish the desired pattern.

**Prompt Template:**
```
[Task instruction]

Example:
Input: [example input]
Output: [example output]

Now complete this:
Input: [actual input]
Output:
```

**Example:**
```
Translate the following sentence to French.

Example:
Input: "Good morning"
Output: "Bonjour"

Now translate:
Input: "How are you?"
Output:
```

**Best For:**
- Simple tasks that benefit from one clear demonstration
- Establishing format when few tokens are available for examples

**Limitations:**
- Provides less coverage than few-shot examples
- May not capture edge cases

**Advantages:**
- Quick to create
- Clarifies expected structure with minimal token usage

**Tips for Success:**
- Use a representative example
- Keep instructions concise
