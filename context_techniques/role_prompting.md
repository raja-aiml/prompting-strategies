### Role-based Prompting

**Definition:** Instructing the model to respond from the perspective of a specified expert persona.

**Prompt Template:**
```
As an experienced [expert role], [task instruction]. Incorporate specialized knowledge typical of this role.
```

**Example:**
```
As an experienced cybersecurity analyst, review the following configuration and identify potential vulnerabilities.
```

**Best For:**
- Domain-specific tasks requiring expert knowledge
- Professional writing with field-specific conventions

**Limitations:**
- May introduce unwanted bias from the chosen role
- Not ideal when multiple perspectives are required

**Advantages:**
- Activates domain-specific knowledge patterns
- Produces more relevant, specialized answers

**Tips for Success:**
- Specify the role clearly, including expertise level
- Provide any relevant context the expert would consider
