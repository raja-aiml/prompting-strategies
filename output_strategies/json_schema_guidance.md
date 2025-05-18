### JSON Schema Guidance

**Definition:** Using JSON schemas or structural hints to ensure API-friendly responses from the model.

**Prompt Template:**
```
Respond in JSON using the following schema:
{
  "field1": "string",
  "field2": "integer",
  ...
}
```

**Example:**
```
Provide user information in the schema:
{
  "name": "string",
  "age": number,
  "email": "string"
}
```

**Best For:**
- Integrations requiring machine-readable output
- Scenarios where strict structure prevents parsing errors

**Tips:**
- Validate outputs against the schema during testing
- Keep schemas simple to reduce model confusion
