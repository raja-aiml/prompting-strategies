# AGENTS Instructions for Prompting Strategies Repository

This repository documents advanced template-driven prompting techniques for large language models (LLMs). The content was derived from the "Advanced Template-Driven Prompting Strategies" guide provided by the user. Use this file as a quick reference for contributors.

## Interactive Prompt Map Snippet
The following JavaScript snippet powers the interactive diagram used in some documentation pages. Preserve this behavior when editing the site.

```html
<script>
// JavaScript for interactive functionality
function expandCollapse(event, node) {
  // Toggle visibility of child nodes
  const children = node.querySelectorAll('.children');
  children.forEach(child => {
    child.style.display = child.style.display === 'none' ? 'block' : 'none';
  });
}

function expandNode(event, node) {
  // Show detailed information about this technique
  const details = document.getElementById('technique-details');
  const name = node.textContent.trim();

  // Populate details based on which node was clicked
  let content = '<h3>' + name + '</h3>';

  switch(name) {
    case 'Zero-shot Prompting':
      content += `<p><strong>Definition:</strong> Direct instruction without examples</p>
                 <p><strong>Example:</strong> "Summarize this article in three paragraphs."</p>
                 <p><strong>Best for:</strong> Well-defined tasks within model's capabilities</p>
                 <p><strong>Implementation tip:</strong> Be explicit about format and constraints</p>`;
      break;
    case 'Few-shot Prompting':
      content += `<p><strong>Definition:</strong> 2-5 demonstrations guiding model behavior</p>
                 <p><strong>Example:</strong> "Classify these reviews as positive or negative: 
                   1. 'Love this product!' → Positive
                   2. 'Completely disappointed.' → Negative
                   3. 'It works well but is expensive.' → ?"</p>
                 <p><strong>Best for:</strong> Establishing patterns and output format</p>
                 <p><strong>Implementation tip:</strong> Use diverse but representative examples</p>`;
      break;
    // Additional cases for other nodes can be added here
    default:
      content += '<p>Click on a specific technique to see detailed information.</p>';
  }

  details.innerHTML = content;
  details.style.display = 'block';
}

// Initialize with main categories expanded
document.addEventListener('DOMContentLoaded', function() {
  // Initial setup code here
});
</script>

<div id="technique-details" style="display:none; border:1px solid #ccc; padding:15px; margin-top:20px;">
  <p>Click on a specific technique in the diagram to see detailed information.</p>
</div>
```

## Key Prompting Techniques
- **Zero-shot Prompting** – Direct instructions without examples.
- **Few-shot Prompting** – 2-5 demonstrations that establish the pattern.
- **Multi-shot Prompting** – Extensive examples to cover edge cases.
- **Chain-of-Thought** – Step-by-step reasoning before final answer.
- **Tree-of-Thought** – Explore multiple reasoning paths in parallel.
- **Step-back Prompting** – Meta-cognitive reflection prior to answering.
- **Self-consistent Prompting** – Generate multiple solutions and synthesize the best.
- **Analogy-based Prompting** – Use familiar concepts to explain abstract ideas.
- **Role-based Prompting** – Adopt a specific expert persona.
- **ReAct Framework** – Alternate between reasoning and action steps.

## Best Practices
1. **Template Selection** – Match the prompting technique to task complexity.
2. **Provide Context** – Include relevant background and constraints.
3. **Explicit Instructions** – Clearly state format and approach.
4. **Iterate** – Test prompts with varied inputs and refine.
5. **Combine Methods** – Use hybrid techniques (e.g., Few-shot + CoT) for complex tasks.

## Evaluation Guidelines
- Measure responses based on completion, accuracy, reasoning quality, format adherence, and efficiency.
- When prompts fail, iterate by adding constraints or examples as outlined in the troubleshooting section of the guide.

