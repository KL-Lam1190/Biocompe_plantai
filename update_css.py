import re
import glob

css_root = """:root {
            --deep-green: #1f4031;
            --leaf: #38825c;
            --mint: #e2f0e7;
            --sun: #f0c365;
            --ink: #2b3a32;
            --paper: #f9fbf4;
            --danger: #b5382f;
            --card-shadow: 0 10px 25px rgba(31, 64, 49, 0.12);
        }"""

body_css = """body {
            margin: 0;
            min-height: 100vh;
            font-family: "Nunito", "Segoe UI", sans-serif;
            color: var(--ink);
            background: linear-gradient(135deg, #fdfbf5 0%, #e6efe8 100%);
        }"""

for filename in ['index.html', 'academy.html', 'product.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace :root block (assuming it follows the known pattern)
    content = re.sub(r':root\s*\{[^}]*\}', css_root, content, flags=re.DOTALL)
    
    # Replace body block
    content = re.sub(r'body\s*\{[^}]*\}', body_css, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Unified style updated.")
