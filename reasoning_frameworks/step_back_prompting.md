### Step-back Prompting

**Definition:** Instructing the model to take a broader perspective before diving into details.

**Prompt Template:**
```
[Problem statement]

Before answering, take a step back and consider:
1. What is the broader context of this problem?
2. What general principles or frameworks apply here?
3. What am I assuming that might not be true?

After this reflection, solve the problem.
```

**Example:**
```
A startup is trying to decide whether to focus on growing their user base or improving monetization of existing users. Current metrics: 100,000 users, $2 average revenue per user, 20% annual growth rate, $5 customer acquisition cost.

Before answering, take a step back and consider:
1. What business principles might apply to this decision?
2. What important information might be missing from the scenario?
3. What assumptions might I be making about the business model?

After this reflection, provide a recommendation with reasoning.
```

**Best For:**
- Strategic decisions
- Problems requiring perspective
- Avoiding fixation on immediate details
- Scenarios with potential hidden assumptions

**Limitations:**
- Simple factual queries
- Problems requiring immediate, tactical solutions
- When the broader context is irrelevant

**Advantages:**
- Avoids tunnel vision on complex topics
- Identifies overlooked factors
- Produces more nuanced, thoughtful responses

**Tips for Success:**
- Include specific reflection questions
- Allow "thinking space" for the model to explore context
- Explicitly request identification of assumptions
