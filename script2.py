import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

render_book_old = """<p class="book-note">Best confidence: ${(plant.confidence * 100).toFixed(1)}%<br>Scans: ${plant.scanCount}<br>Mission note: ${plant.note}<br>Hong Kong status: ${plant.hkStatus}<br>Rare note: ${plant.rarityNote}<br>Public note: ${plant.publicNote}</p>"""

render_book_new = """<div class="book-note">
                            <div>Best config: ${(plant.confidence * 100).toFixed(1)}% | Scans: ${plant.scanCount}</div>
                            <hr style="border:0; border-top:1px dashed #c7dece; margin: 6px 0;">
                            <strong>植物種類:</strong> ${plant.type || "植物"}<br>
                            <strong>生態資料:</strong> ${plant.shengTai || "陸生 / 常見"}<br>
                            <strong>花:</strong> ${plant.hua || "視乎品種"} | <strong>花期:</strong> ${plant.huaQi || "視乎品種"}<br>
                            <strong>果實:</strong> ${plant.guoShi || "視乎品種"} | <strong>果期:</strong> ${plant.guoQi || "視乎品種"}<br>
                            <strong>《香港稀有及珍貴植物》:</strong> ${plant.hkRareCategory || (plant.rarePrecious?"VU 易危":"LC 無危")}<br>
                            <strong>《中國植物紅皮書》:</strong> ${plant.cnRedBookCategory || (plant.rarePrecious?"NT 近危":"LC 無危")}<br>
                            <hr style="border:0; border-top:1px dashed #c7dece; margin: 6px 0;">
                            <div><em>${plant.hkStatus}</em></div>
                        </div>"""

text = text.replace(render_book_old, render_book_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('academy.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

academy_old = """<p><strong>Plant type:</strong> ${type}<br><strong>Hong Kong status:</strong> ${hkStatus}<br><strong>Rare note:</strong> ${rarityNote}<br><strong>Best confidence:</strong> ${confidenceText}<br><strong>Scans:</strong> ${plant.scanCount || 1}<br><strong>Public note:</strong> ${publicNote}</p>"""

academy_new = """<p>
                        <strong>植物種類 (Plant type):</strong> ${type}<br>
                        <strong>生態資料:</strong> ${plant.shengTai || "陸生 / 常見"}<br>
                        <strong>花:</strong> ${plant.hua || "視乎品種"} | <strong>花期:</strong> ${plant.huaQi || "視乎品種"}<br>
                        <strong>果實:</strong> ${plant.guoShi || "視乎品種"} | <strong>果期:</strong> ${plant.guoQi || "視乎品種"}<br>
                        <strong>《香港稀有及珍貴植物》類別註解:</strong> ${plant.hkRareCategory || (rarePrecious?"VU 易危":"LC 無危")}<br>
                        <strong>《中國植物紅皮書》類別註解:</strong> ${plant.cnRedBookCategory || (rarePrecious?"NT 近危":"LC 無危")}<br>
                        <br>
                        <strong>Hong Kong status:</strong> ${hkStatus}<br>
                        <strong>Rare note:</strong> ${rarityNote}<br>
                        <strong>Best confidence:</strong> ${confidenceText} | <strong>Scans:</strong> ${plant.scanCount || 1}<br>
                        <strong>Public note:</strong> ${publicNote}
                    </p>"""

text2 = text2.replace(academy_old, academy_new)

with open('academy.html', 'w', encoding='utf-8') as f:
    f.write(text2)

