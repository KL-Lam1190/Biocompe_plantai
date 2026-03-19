import re

for filename in ['index.html', 'academy.html', 'product.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Make the text clear with line breaks and the desired message.
    new_footer = """    <footer style="width: 100%; padding: 24px; text-align: center; background-color: #1f4031; color: #f9fbf4; font-size: 0.9em; margin-top: 40px;">
        <p style="margin: 0 0 10px 0;">&copy; 2024 Plant Mission Notebook. All rights reserved.</p>
        <p style="margin: 0; font-size: 0.85em; opacity: 0.8; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.5;">
            <b>Disclaimer:</b> The AI identification model is NOT 100% accurate. Plant data and conservation statuses provided are for educational purposes only and may not be completely correct. Do not use this AI for definitive identification, foraging, medical, or official conservation decisions.
        </p>
    </footer>
</body>"""
    
    content = re.sub(r'<footer.*?</footer>\n</body>', new_footer, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

