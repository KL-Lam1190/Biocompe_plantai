import re

# Update index.html hero section
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_hero = """        <section class="hero">
            <h1>Plant Mission Notebook</h1>
            <p>Scan plants with Teachable Machine, pass missions with correct identification, and unlock a public-friendly notebook with plant type, plant photo, and Hong Kong status notes.</p>
        </section>"""

new_hero = """        <section class="hero">
            <h1>🌿 生物多樣性 AI 守護者 (Plant AI) 🌿</h1>
            <p style="opacity: 0.9; margin-bottom: 5px;"><strong>2025「猛獁杯」國際生命科學創新大賽 (MICOS - Hong Kong) 參賽作品</strong></p>
            <p style="opacity: 0.8; font-size: 0.9em; margin-bottom: 15px;">主題：生命與環境的共生：科技守護未來 | 智能守護自然——人工智慧（AI）在生物多樣性保護中的應用</p>
            <p>本專案運用預先訓練的 Teachable Machine AI 模型，讓民眾可以輕鬆使用手機或電腦鏡頭辨識香港本土的珍稀及特色植物（例如秀英竹、豬籠草、南方安蘭等）。透過寓教於樂的解鎖任務，我們希望增加大眾對 SDGs 及本土植物保育的認識，了解 AI 如何助力生態監測與防護！</p>
        </section>"""

content = content.replace(old_hero, new_hero)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


# Update product.html content to directly address the competition requirements
with open('product.html', 'r', encoding='utf-8') as f:
    product_content = f.read()

product_hero_old = """        <section class="hero">
            <h1>About Product</h1>
            <p>Learn more about how the Plant Mission Notebook uses Teachable Machine to identify plants and build a public ecology notebook.</p>
        </section>

        <section class="stack">
            <article class="card">
                <h2>Product Overview</h2>
                <p>The Plant Mission Notebook combines machine learning and gamification to encourage users to explore local plant species, especially those with conservation value.</p>
            </article>

            <article class="card">
                <h2>How It Works</h2>
                <p>Using Google's Teachable Machine image classification model, the application securely processes plant photos from the users camera or local files without transmitting sensitive personal data. Once the AI confidently recognizes the plant, its profile—including its conservation status—is unlocked in the notebook.</p>
            </article>

            <article class="card">
                <h2>Value to Society</h2>
                <p>By transforming raw environmental data into an interactive format, this product serves as both an educational tool for schools and a field guide for nature enthusiasts, promoting daily awareness of biodiversity.</p>
            </article>
        </section>"""

product_hero_new = """        <section class="hero">
            <h1>研究背景與專案介紹 (About the Project)</h1>
            <p>專為 2025「猛獁杯」國際生命科學創新大賽 (MICOS - Hong Kong) 設計的學術展示平台。</p>
        </section>

        <section class="stack">
            <article class="card">
                <h2>🌍 大賽願景：生命與環境的共生</h2>
                <p>「猛獁杯」國際生命科學創新大賽（MICOS）致力於運用科技重構生命未來。本專案呼應聯合國2030年可持續發展目標（SDGs），以「智能守護自然——人工智慧（AI）在生物多樣性保護中的應用」為核心，探討如何利用電腦視覺技術落實生態監測。</p>
            </article>

            <article class="card">
                <h2>🎯 研究背景與目的</h2>
                <p><strong>背景：</strong>生態系統的完整性正面臨棲息地破壞與物種滅絕的嚴峻挑戰。許多市民雖然有意願維護生物多樣性，但因缺乏辨認本土植物的能力而無從下手。<br>
                <strong>目的：</strong>開發一個基於 AI 的植物辨識網站，降低民眾認識香港特色植物的門檻。我們透過 AI 建立「數字植物園」，讓大眾能夠輕鬆分辨植物，從而提升維持生物多樣性的保育意識。</p>
            </article>

            <article class="card">
                <h2>⚙️ 研究方法 (Teachable Machine)</h2>
                <p>本專案採用 <strong>Google Teachable Machine</strong> 訓練了一個輕量級的影像分類模型。我們針對香港本土的 12 種標誌性、珍貴或受威脅植物（如大嶼八角、土沉香、香港巴豆等）收集影像數據，讓 AI 模型學習其葉片、花朵及形態特徵。系統更加入像素色彩分析與紋理變異度（Variance）過濾機制，確保辨識的準確性並防止假照片作弊。</p>
            </article>

            <article class="card">
                <h2>📊 最終成果與貢獻</h2>
                <p>目前，我們的 AI 模型已能初步辨識 12 種特定植物。結合前端網頁的「成就與任務解鎖系統」，民眾每次成功掃描植物，即可解鎖該植物的《香港稀有及珍貴植物》保育級別與生態資料。這猶如一個<strong>普及化的「數字諾亞方舟」</strong>前導計畫，為未來的生境監測與公眾科學教育提供了實用的工具雛形。</p>
            </article>
        </section>"""

product_content = re.sub(product_hero_old, product_hero_new, product_content, flags=re.DOTALL)
with open('product.html', 'w', encoding='utf-8') as f:
    f.write(product_content)

print("Updated index and product pages with MICOS details")
