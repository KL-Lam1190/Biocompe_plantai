import re
import glob

footer_html = """
    <footer style="margin-top: 40px; padding: 20px; text-align: center; background-color: var(--deep-green); color: var(--paper); font-size: 0.9em; border-radius: 8px 8px 0 0;">
        <p style="margin: 0 0 10px 0;">&copy; 2024 Plant Mission Notebook. All rights reserved.</p>
        <p style="margin: 0; font-size: 0.85em; opacity: 0.8;">
            <b>Disclaimer:</b> The AI model used for plant identification is not 100% accurate. Plant data and conservation statuses provided are for educational purposes only and may not be completely error-free or up-to-date. Do not rely on this tool for foraging, medical, or official conservation decisions.
        </p>
    </footer>
    </div>
"""

for filename in ['index.html', 'academy.html', 'product.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the closing </div> of the main .page container (it's right before modals or scripts usually)
    # The safest way is to find the script tags or modals and inject the footer before the end of the .page div.
    # Since all pages end with </body>, finding </div>\n    <script/modal or simply appending before scripts could be dangerous if structure differs.
    
    # Let's insert it right before the </body> tag, but wrap it so it doesn't break the page layout.
    # We will instead look for the end of the content.
    # Wait, all pages wrap their main content in <div class="page">. We can just put the footer at the very bottom of the page div, or right after it before closing body.
    
    # Easiest and most consistent: put it right before </body>, not inside the grid layout so it spans the bottom.
    page_footer_html = """
    <footer style="width: 100%; padding: 24px; text-align: center; background-color: #1f4031; color: #f9fbf4; font-size: 0.9em; margin-top: 40px;">
        <p style="margin: 0 0 10px 0;">&copy; 2024 Plant Mission Notebook. All rights reserved.</p>
        <p style="margin: 0; font-size: 0.85em; opacity: 0.8; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.5;">
            <b>Disclaimer:</b> The AI identification model is not 100% accurate and results should be verified independently. The plant data, ecological notes, and conservation statuses provided are for educational purposes and may not be completely correct or up-to-date. Please do not consume any plants or make critical decisions based solely on this tool.
        </p>
    </footer>
</body>"""

    if "<footer" not in content:
        content = re.sub(r'</body>', page_footer_html, content, count=1)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added footer to {filename}")
    else:
        print(f"Footer already exists in {filename}")

