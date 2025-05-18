### JSON Repair

**Purpose:** Handle incomplete or malformed JSON outputs from the model.

**Approach:**
1. Detect whether the JSON can be parsed.
2. If invalid, attempt common fixes such as closing braces or quoting keys.
3. Revalidate and, if necessary, ask the model to regenerate just the malformed portion.

**Tip:** Keeping prompts concise and using JSON schema guidance reduces errors in the first place.
