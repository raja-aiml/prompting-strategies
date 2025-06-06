### Output Formats

**Definition:** Techniques for directing the model to produce responses in a particular style, such as bullet points, tables, or paragraphs.

**Prompt Template:**
```
[Task instruction] Output format: [desired format]
```

**Example:**
```
List three benefits of regular exercise. Output format: bullet list.
```

**Best For:**
- Situations where downstream systems expect a certain format
- Ensuring consistency across multiple responses

**Tips:**
- State the format requirement explicitly
- If the format is complex, include a brief example

**Limitations:**
- May reduce creativity if the format is too constrained
- Additional instructions increase token count

**Advantages:**
- Promotes predictable structure for downstream processing
- Works well with parsing tools or templates
