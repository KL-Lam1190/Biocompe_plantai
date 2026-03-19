import re

with open('academy.html', 'r', encoding='utf-8') as f:
    content = f.read()

academy_hero_old = """    <main class="page-container">
        <section class="hero">
            <h1>Plant Mission Academy</h1>
            <p>Your collected ecological specimens.</p>
        </section>"""

academy_hero_new = """    <main class="page-container">
        <section class="hero">
            <h1>🌱 生物多樣性資料庫 (Biodiversity Academy) 🌱</h1>
            <p><strong>智能守護自然——AI 在生物多樣性保護中的應用</strong><br>您所成功辨識並保育的珍貴植物記錄。</p>
        </section>"""

content = content.replace(academy_hero_old, academy_hero_new)

with open('academy.html', 'w', encoding='utf-8') as f:
    f.write(content)
