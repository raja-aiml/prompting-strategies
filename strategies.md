# Comprehensive Prompt Engineering Framework (Enhanced)
**Aligned with Boonstra, 2025 PDF + Review Enhancements**

## Framework Overview

### Core Techniques (Must Include)
- Zero-shot Prompting
- Few-shot Prompting
- System Prompting
- Role Prompting
- Contextual Prompting
- Step-back Prompting
- Chain of Thought
- Self-Consistency
- Tree of Thoughts
- ReAct

---

## Layer 1: Core Foundation

### Zero-shot Prompting
- **Purpose**: Direct instruction without examples [cite: 87]
- **Cost**: Low (single prompt)
- **Best For**: Simple, well-defined tasks
- **Notes**: Uses model's pre-trained knowledge [cite: 84]; Foundation for many other techniques [cite: 87]

### Few-shot Prompting
- **Purpose**: Learning from examples provided in the prompt [cite: 101, 103]
- **Subtypes**:
  - One-shot: Single example [cite: 105]
  - Few-shot: Multiple examples (typically 3-5 or more, depending on task and model limits) [cite: 107, 111, 112]
- **Cost**: Medium (longer prompts, multiple examples)
- **Cost-Benefit Analysis**: High value for complex tasks, diminishing returns after 5-7 examples
- **Notes**: Builds context and demonstrates desired output structure [cite: 104]; Crucial best practice: "Provide examples" [cite: 351]

### System Prompting
- **Purpose**: Behavior configuration and defining overall context/purpose for the LLM [cite: 124, 131]
- **Cost**: Low (typically persistent across interactions)
- **Best For**: Setting consistent behavior, safety controls, output formatting
- **Notes**: Controls tone, behavior, rules, output format [cite: 136, 142, 140]; Useful for safety and toxicity control [cite: 149]

---

## Layer 2: Context Engineering

### Role Prompting
- **Purpose**: Assigns a specific character, persona, or identity for the LLM to adopt [cite: 127, 151]
- **Example**: "Act as a travel guide..." [cite: 155]
- **Model Performance Variations**:
  - **GPT models**: Strong response to detailed role descriptions
  - **Claude**: Excellent at maintaining consistent persona throughout conversation
  - **Gemini**: Good at role-based reasoning, less consistent with creative personas
- **Notes**: Influences tone, style, and focused expertise [cite: 161]

### Contextual Prompting
- **Purpose**: Provides specific details, background information, or situational constraints [cite: 125, 132]
- **Cost Consideration**: Can significantly increase token usage with large contexts
- **Best Practices**: Prioritize most relevant context first; use structured formats for complex contexts
- **Notes**: Helps model understand nuances and tailor responses [cite: 126]; Can be dynamic and task-specific [cite: 133]

---

## Layer 3: Reasoning Architecture

### Step-back Prompting
- **Purpose**: Improves reasoning by considering general questions before specific tasks [cite: 169, 170]
- **Cost**: Medium (additional reasoning step)
- **Failure Mode**: Can lead to over-generalization; monitor for relevance drift
- **Notes**: Activates relevant background knowledge [cite: 171]; Useful for critical thinking [cite: 173, 175]

### Chain of Thought (CoT)
- **Purpose**: Improves reasoning through intermediate steps [cite: 190, 191]
- **Pattern**: "Let's think step by step." [cite: 205]
- **Cost**: Medium-High (longer outputs, more compute)
- **Model Performance**:
  - **GPT-4**: Excellent at complex multi-step reasoning
  - **Claude**: Strong logical consistency, good at catching errors
  - **Smaller models**: May struggle with long reasoning chains
- **Common Failure Modes**:
  - Reasoning drift: Steps become less relevant to original question
  - Circular reasoning: Getting stuck in logical loops
  - Premature conclusions: Skipping necessary intermediate steps
- **Diagnostics**: Check if each step logically follows; verify final answer alignment
- **Best Practices**: Set temperature to 0 for single correct paths [cite: 438, 439]; Ensure answer follows reasoning [cite: 436]

### Self-Consistency
- **Purpose**: Enhances reliability through multiple reasoning paths [cite: 224]
- **Cost**: High (multiple generations, 3-10x base cost)
- **Cost-Benefit Decision Matrix**:
  - **High-stakes decisions**: Worth the cost
  - **Creative tasks**: Usually not cost-effective
  - **Mathematical problems**: High value
  - **Simple classification**: Overkill
- **Implementation**: Generate 5-10 responses, select by majority vote
- **Notes**: Improves accuracy over greedy decoding [cite: 224]

### Tree of Thoughts (ToT)
- **Purpose**: Explore multiple reasoning paths simultaneously [cite: 240, 241]
- **Cost**: Very High (exponential with tree depth)
- **Best For**: Complex problem-solving requiring exploration
- **When NOT to use**: Simple tasks, tight budget constraints, real-time applications
- **Notes**: Suited for deliberate problem-solving [cite: 243, 247]

### ReAct Framework (Reason & Act)
- **Purpose**: Combines reasoning with external tool usage [cite: 247, 248]
- **Pattern**: Thought → Action → Observation → Repeat [cite: 251, 254]
- **Cost**: Variable (depends on tool usage)
- **Common Failure Modes**:
  - Tool selection errors: Using wrong tool for task
  - Infinite loops: Repeating same unsuccessful actions
  - Context loss: Forgetting previous observations
- **Diagnostics**: Monitor action diversity, track progress toward goal
- **Notes**: Requires careful setup and context management [cite: 273]

---

## Layer 4: Output Engineering

### Structured Output Specification
- **Purpose**: Predictable, parseable output formats [cite: 412]
- **Formats**: JSON, XML, Markdown, Table, Custom Formats
- **Model Performance**:
  - **JSON compliance**: GPT-4 > Claude > Gemini for complex schemas
  - **XML handling**: Generally good across models
  - **Custom formats**: Varies significantly by complexity
- **Notes**: "Be specific about the output" [cite: 364]; JSON limits hallucinations [cite: 414]

### JSON Schema Guidance
- **Purpose**: Define expected structure and data types
- **For Input**: Helps LLM understand data relationships [cite: 425-428]
- **For Output**: Ensures conforming generation [cite: 145]
- **Failure Mode**: Schema violations, especially with complex nested structures
- **Diagnostic**: Validate output against schema programmatically

### JSON Repair
- **Purpose**: Handle malformed JSON from truncation [cite: 419-421]
- **Tools**: `json-repair` library (Python)
- **When Needed**: Token limit truncation, complex nested structures

---

## Layer 5: Implementation Strategy

### LLM Output Configuration
- **Parameters**:
  - **Max Tokens**: Balance cost, speed, completeness [cite: 32, 33, 35]
  - **Temperature**: 0 for deterministic, 0.7-1.0 for creative [cite: 42, 43]
  - **Top-K/Top-P**: Fine-tune randomness [cite: 51, 53, 57]
- **Cost Optimization**: Lower max tokens for simple tasks, adjust temperature based on need
- **Common Issues**: Repetition loops at extreme temperatures [cite: 77-80]

### Prompt Evaluation Metrics
- **Automated Metrics**:
  - **Accuracy**: For classification/extraction tasks
  - **ROUGE/BLEU**: For text generation quality
  - **JSON Schema Compliance**: For structured outputs
  - **Latency**: Response time measurements
  - **Cost per Task**: Token usage tracking
- **Human Evaluation**:
  - **Relevance**: Does output address the query?
  - **Coherence**: Is reasoning logical and consistent?
  - **Completeness**: Are all requirements met?
  - **Safety**: Any harmful or inappropriate content?
- **A/B Testing Framework**:
  - Control vs experimental prompts
  - Statistical significance testing
  - Performance tracking over time

### Variables in Prompts
- **Purpose**: Dynamic, reusable prompts [cite: 390]
- **Example**: "Tell me a fact about the city: {city}" [cite: 395]
- **Cost Benefit**: Reduces development time, enables scaling
- **Notes**: Saves effort, useful for integration [cite: 393, 394]

### Documentation & Iteration Methods
- **Tracking Elements**:
  - Name, Goal, Model, Configuration, Prompt, Output, Feedback, Version [cite: 445-458]
  - Cost per iteration, performance metrics
  - Failure modes encountered and solutions
- **Version Control**: Track prompt evolution, enable rollbacks
- **A/B Testing Results**: Document winning variations and why

### Model-Specific Optimization Guidelines

#### GPT Models
- **Strengths**: Complex reasoning, code generation, following detailed instructions
- **Weaknesses**: Can be verbose, sometimes overconfident
- **Optimization**: Use system prompts for brevity, explicit format requirements

#### Claude Models
- **Strengths**: Nuanced understanding, ethical reasoning, balanced responses
- **Weaknesses**: Can be overly cautious, sometimes refuses valid requests
- **Optimization**: Clear context about legitimate use cases, structured role definitions

#### Gemini Models
- **Strengths**: Multimodal capabilities, factual accuracy, efficiency
- **Weaknesses**: Less creative, can be rigid with instructions
- **Optimization**: Explicit examples, clear success criteria

#### Smaller/Local Models
- **Strengths**: Cost-effective, privacy, customizable
- **Weaknesses**: Limited reasoning, context length, instruction following
- **Optimization**: Simpler prompts, more examples, explicit formatting

### Instructions over Constraints
- **Principle**: Tell the model what TO do rather than what NOT to do [cite: 370-386]
- **Cost Impact**: Positive instructions often require fewer iterations
- **When to Use Constraints**: Safety requirements, legal compliance, strict format needs

---

## Layer 6: Advanced Integration

### Combined Prompting Techniques
**Meta-Pattern Example**:
```
SYSTEM: [Behavior rules, overall purpose]
ROLE: [Specific persona]
CONTEXT: [Background information]
EXAMPLES: [Few-shot demonstrations]
REASONING_TRIGGER: [CoT or other reasoning method]
TASK: [Specific instruction]
OUTPUT_FORMAT: [Structure specification]
VALIDATION_CUE: [Self-check instruction]
```

### Cost-Optimized Technique Selection
- **Simple Tasks**: Zero-shot + System prompting
- **Medium Complexity**: Few-shot + CoT
- **High Stakes**: Self-Consistency + Human review
- **Complex Reasoning**: ToT (if budget allows) or ReAct + tools

### Failure Mode Diagnostic Flowchart
1. **Output Format Issues**: Check schema compliance, validate structure
2. **Reasoning Errors**: Trace logical steps, check for circular reasoning
3. **Irrelevant Responses**: Review context relevance, check role clarity
4. **Inconsistent Results**: Test with different temperatures, add more examples
5. **Safety Violations**: Strengthen system prompts, add explicit constraints

---

## Layer 7: Application-Specific Patterns

### Code Applications
- **Relevant Techniques**: System + Role + Few-shot + CoT + Structured Output
- **Cost Optimization**: Use simpler prompts for syntax tasks, complex reasoning for architecture
- **Common Failures**: Outdated libraries, security vulnerabilities, incomplete error handling
- **Evaluation**: Code compilation, test coverage, security scanning

### Content Creation & Summarization
- **Relevant Techniques**: Role + Contextual + Few-shot + Step-back + Output Specification
- **Model Selection**: GPT for creativity, Claude for balanced tone, Gemini for factual content
- **Evaluation**: Readability scores, fact-checking, audience appropriateness

### Complex Reasoning & Decision Support
- **Relevant Techniques**: CoT + Self-Consistency + ToT + ReAct + Structured Output
- **Cost Considerations**: High-value decisions justify expensive techniques
- **Evaluation**: Logic validation, stakeholder review, outcome tracking

### Information Extraction & Classification
- **Relevant Techniques**: Few-shot + System + JSON Output + Contextual Prompting
- **Cost Optimization**: Batch processing, caching common extractions
- **Evaluation**: Precision, recall, F1-score, manual spot-checks

---

## Meta-Framework Summary: Unified Prompting Strategy

### 6-Phase Iterative Approach
1. **Foundation**: Start with clear base instructions (Zero/Few-shot)
2. **Contextualization**: Add background, role, and system guidance
3. **Reasoning**: Apply appropriate reasoning architecture for complexity
4. **Output Structuring**: Define clear output format and validation
5. **Implementation Tuning**: Configure parameters and optimize for cost/performance
6. **Iteration & Optimization**: Test, measure, refine, scale

### Decision Framework for Technique Selection
```
IF task_complexity == "simple" AND budget == "low":
    USE zero_shot + system_prompting
ELIF task_complexity == "medium" AND accuracy_requirement == "high":
    USE few_shot + chain_of_thought
ELIF task_complexity == "high" AND budget == "flexible":
    USE self_consistency OR tree_of_thoughts
ELIF external_tools_needed:
    USE react_framework
ELSE:
    START with few_shot + chain_of_thought, ITERATE based on results
```

### Success Metrics Dashboard
- **Performance**: Accuracy, completeness, relevance scores
- **Efficiency**: Cost per task, response latency, iteration cycles
- **Reliability**: Consistency across runs, failure rate, error types
- **Business Impact**: User satisfaction, task completion rate, ROI

This enhanced framework now provides comprehensive guidance for cost-conscious implementation, failure diagnosis, model-specific optimization, and systematic evaluation—making it truly production-ready for enterprise prompt engineering.