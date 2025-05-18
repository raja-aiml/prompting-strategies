import os
import re

root_dir = os.path.dirname(__file__)
# patterns to check
sections = {
    'Definition': re.compile(r'^\*\*Definition:.*', re.MULTILINE),
    'Prompt Template': re.compile(r'^\*\*Prompt Template:.*', re.MULTILINE),
    'Example': re.compile(r'^\*\*Example:.*', re.MULTILINE),
    'Best For': re.compile(r'^\*\*Best For:.*', re.MULTILINE),
    'Limitations': re.compile(r'^\*\*(Limitations|When NOT to Use):.*', re.MULTILINE),
    'Advantages': re.compile(r'^\*\*Advantages:.*', re.MULTILINE),
    'Tips': re.compile(r'^\*\*(Tips|Best Practices|Tips for Success):.*', re.MULTILINE),
}

result_lines = []
for path, _, files in os.walk(root_dir):
    for fname in files:
        if fname.endswith('.md'):
            fpath = os.path.join(path, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            if '**Prompt Template:**' in content:
                missing = [name for name, pattern in sections.items() if not pattern.search(content)]
                if missing:
                    rel_path = os.path.relpath(fpath, root_dir)
                    result_lines.append(f"{rel_path}: Missing sections: {', '.join(missing)}")

if result_lines:
    print('\n'.join(result_lines))
else:
    print('All prompt templates contain all checked sections.')
