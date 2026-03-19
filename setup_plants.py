import re
import json

plant_catalog = {
    "秀英竹": {
        "type": "禾本科竹亞科 (Bamboo)",
        "shengTai": "生長於山地林下或灌叢",
        "hua": "不常見",
        "huaQi": "不詳",
        "guoShi": "穎果",
        "guoQi": "不詳",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "EN 瀕危",
        "cnRedBookCategory": "未評估",
        "publicNote": "秀英竹是香港特有的珍稀竹類，以植物學家胡秀英命名。",
        "rarePrecious": True,
        "rarityNote": "受《林務規例》保護，分佈極為狹窄。"
    },
    "豬籠草": {
        "type": "食蟲植物 (Carnivorous Plant)",
        "shengTai": "生長於向陽貧瘠山坡或濕地",
        "hua": "總狀花序",
        "huaQi": "4月 - 11月",
        "guoShi": "蒴果",
        "guoQi": "8月 - 12月",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "VU 易危",
        "cnRedBookCategory": "VU 易危",
        "publicNote": "豬籠草能捕捉並消化昆蟲以補充營養，切勿野外採摘。",
        "rarePrecious": True,
        "rarityNote": "受香港法例第96章《林區及遊樂區條例》保護。"
    },
    "大嶼八角": {
        "type": "常綠小喬木 (Evergreen Tree)",
        "shengTai": "生長於山地林中",
        "hua": "白色至淡黃色",
        "huaQi": "2月 - 4月",
        "guoShi": "蓇葖果",
        "guoQi": "9月 - 10月",
        "hkStatus": "Endemic (香港特有種)",
        "hkRareCategory": "CR 極危",
        "cnRedBookCategory": "CR 極危",
        "publicNote": "全球僅見於香港大嶼山，是極度瀕危的珍稀植物。",
        "rarePrecious": True,
        "rarityNote": "受香港法例第96章《林區及遊樂區條例》保護。"
    },
    "棱果花": {
        "type": "常綠灌木 (Evergreen Shrub)",
        "shengTai": "生長於山谷林下陰濕處",
        "hua": "白色或略帶粉紅",
        "huaQi": "夏季",
        "guoShi": "漿果狀",
        "guoQi": "秋季至冬季",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "LC 無危",
        "cnRedBookCategory": "未評估",
        "publicNote": "花朵造型獨特，果實具棱角，是良好的庭園觀賞植物。",
        "rarePrecious": False,
        "rarityNote": "在香港有一定分佈，但仍需保護其自然棲息地。"
    },
    "珊瑚菜": {
        "type": "多年生草本 (Perennial Herb)",
        "shengTai": "生長於海濱沙灘",
        "hua": "白色複繖形花序",
        "huaQi": "6月 - 7月",
        "guoShi": "雙懸果",
        "guoQi": "8月 - 9月",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "VU 易危",
        "cnRedBookCategory": "未評估",
        "publicNote": "根部可入藥（北沙參），因過度採挖而變得稀少。",
        "rarePrecious": True,
        "rarityNote": "生境容易受海岸發展破壞。"
    },
    "斑葉女貞": {
        "type": "常綠灌木 (Evergreen Shrub)",
        "shengTai": "生長於山地林下或林緣",
        "hua": "白色",
        "huaQi": "春夏季",
        "guoShi": "核果",
        "guoQi": "秋冬季",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "NT 近危",
        "cnRedBookCategory": "未評估",
        "publicNote": "葉片常帶有斑紋，具觀賞價值。",
        "rarePrecious": True,
        "rarityNote": "在香港分佈有限。"
    },
    "畫筆南星": {
        "type": "多年生草本 (Perennial Herb)",
        "shengTai": "生長於林下陰濕地",
        "hua": "佛焰苞肉穗花序",
        "huaQi": "春季",
        "guoShi": "漿果",
        "guoQi": "夏秋季",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "VU 易危",
        "cnRedBookCategory": "未評估",
        "publicNote": "花序特殊，形如畫筆，整株有毒，切勿誤食。",
        "rarePrecious": True,
        "rarityNote": "分佈範圍狹窄，受棲息地破壞威脅。"
    },
    "香港細辛": {
        "type": "多年生草本 (Perennial Herb)",
        "shengTai": "生長於山谷林下陰濕處",
        "hua": "紫褐色",
        "huaQi": "冬季至春季",
        "guoShi": "蒴果",
        "guoQi": "春季至夏季",
        "hkStatus": "Endemic (香港特有種)",
        "hkRareCategory": "EN 瀕危",
        "cnRedBookCategory": "EN 瀕危",
        "publicNote": "香港特有的細辛屬植物，具有獨特的花朵結構。",
        "rarePrecious": True,
        "rarityNote": "受香港法例第96章《林區及遊樂區條例》保護。"
    },
    "長葉矛膏菜": {
        "type": "食蟲植物 (Carnivorous Plant)",
        "shengTai": "生長於向陽濕地",
        "hua": "粉紅色或白色",
        "huaQi": "夏秋季",
        "guoShi": "蒴果",
        "guoQi": "秋季",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "EN 瀕危",
        "cnRedBookCategory": "未評估",
        "publicNote": "葉片具腺毛，能分泌黏液捕捉微小昆蟲。",
        "rarePrecious": True,
        "rarityNote": "濕地生境受破壞，導致數量大減。"
    },
    "南方安蘭": {
        "type": "地生蘭 (Terrestrial Orchid)",
        "shengTai": "生長於林下陰濕地",
        "hua": "小形，不顯眼",
        "huaQi": "春季",
        "guoShi": "蒴果",
        "guoQi": "夏季",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "VU 易危",
        "cnRedBookCategory": "未評估",
        "publicNote": "一種原始的蘭科植物，對研究蘭科演化具重要意義。",
        "rarePrecious": True,
        "rarityNote": "蘭科植物全科受保護。"
    },
    "香港巴豆": {
        "type": "常綠灌木或小喬木 (Evergreen Shrub/Tree)",
        "shengTai": "生長於山地林中",
        "hua": "黃綠色",
        "huaQi": "春季",
        "guoShi": "蒴果",
        "guoQi": "夏季",
        "hkStatus": "Endemic (香港特有種)",
        "hkRareCategory": "CR 極危",
        "cnRedBookCategory": "CR 極危",
        "publicNote": "曾被認為已滅絕，後於青衣島再次發現，極度稀有。",
        "rarePrecious": True,
        "rarityNote": "受香港法例第96章《林區及遊樂區條例》保護。"
    },
    "土沉香": {
        "type": "常綠喬木 (Evergreen Tree)",
        "shengTai": "常見於風水林及郊野叢林",
        "hua": "黃綠色、鐘形",
        "huaQi": "4月 - 5月",
        "guoShi": "卵形木質蒴果",
        "guoQi": "7月 - 8月",
        "hkStatus": "Native (香港原生種)",
        "hkRareCategory": "NT 近危",
        "cnRedBookCategory": "VU 易危",
        "publicNote": "昔日香港香木業重要樹種，野外群落常遭非法砍伐。",
        "rarePrecious": True,
        "rarityNote": "受《林區及遊樂區條例》及《保護瀕危動植物物種條例》保護。"
    }
}

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace hongKongPlantCatalog
catalog_str = json.dumps(plant_catalog, ensure_ascii=False, indent=12)
catalog_str = catalog_str.replace("true", "true").replace("false", "false")
content = re.sub(
    r"const hongKongPlantCatalog = \{.*?\};",
    f"const hongKongPlantCatalog = {catalog_str};",
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html with new plant catalog!")
