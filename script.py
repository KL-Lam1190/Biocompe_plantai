import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

green_func = """
        function calculateGreenPercentage(imageSource) {
            const tempCanvas = document.createElement("canvas");
            const ctx = tempCanvas.getContext("2d");
            tempCanvas.width = imageSource.width || imageSource.videoWidth || 360;
            tempCanvas.height = imageSource.height || imageSource.videoHeight || 360;
            if (tempCanvas.width === 0 || tempCanvas.height === 0) return 100; // Skip if invalid
            
            ctx.drawImage(imageSource, 0, 0, tempCanvas.width, tempCanvas.height);
            const data = ctx.getImageData(0, 0, tempCanvas.width, tempCanvas.height).data;
            let greenPixels = 0;
            for (let i = 0; i < data.length; i += 4) {
                const r = data[i];
                const g = data[i + 1];
                const b = data[i + 2];
                // basic green threshold
                if (g > r * 1.05 && g > b * 1.05 && g > 30) {
                    greenPixels++;
                }
            }
            return (greenPixels / (tempCanvas.width * tempCanvas.height)) * 100;
        }
"""

text = text.replace("function normalizePlantName", green_func + "\n        function normalizePlantName")

run_pred_old = """        async function runPrediction(imageSource, imageData) {"""
run_pred_new = """        async function runPrediction(imageSource, imageData) {
            const greenPct = calculateGreenPercentage(imageSource);
            if (greenPct < 40) {
                updateModal(
                    "Not Enough Green / Not a Plant",
                    `This photo has only ${greenPct.toFixed(1)}% green area. A plant photo must be >40% green.`
                );
                showToast("Not enough green.", true);
                return;
            }
"""
text = text.replace(run_pred_old, run_pred_new)

add_to_book_old = """                    type: plantDetails.type,
                    hkStatus: plantDetails.hkStatus,
                    publicNote: plantDetails.publicNote,
                    rarePrecious: plantDetails.rarePrecious,
                    rarityNote: plantDetails.rarityNote,"""

add_to_book_new = """                    type: plantDetails.type,
                    hkStatus: plantDetails.hkStatus,
                    publicNote: plantDetails.publicNote,
                    rarePrecious: plantDetails.rarePrecious,
                    rarityNote: plantDetails.rarityNote,
                    shengTai: plantDetails.shengTai || "陸生 / 常見",
                    hua: plantDetails.hua || "視乎品種",
                    huaQi: plantDetails.huaQi || "視乎品種",
                    guoShi: plantDetails.guoShi || "視乎品種",
                    guoQi: plantDetails.guoQi || "視乎品種",
                    hkRareCategory: plantDetails.hkRareCategory || (plantDetails.rarePrecious ? "VU 易危" : "LC 無危"),
                    cnRedBookCategory: plantDetails.cnRedBookCategory || (plantDetails.rarePrecious ? "NT 近危" : "LC 無危"),"""

text = text.replace(add_to_book_old, add_to_book_new)

update_existing_old = """                existing.rarePrecious = plantDetails.rarePrecious;
                existing.rarityNote = plantDetails.rarityNote;"""

update_existing_new = """                existing.rarePrecious = plantDetails.rarePrecious;
                existing.rarityNote = plantDetails.rarityNote;
                existing.shengTai = existing.shengTai || "陸生 / 常見";
                existing.hua = existing.hua || "視乎品種";
                existing.huaQi = existing.huaQi || "視乎品種";
                existing.guoShi = existing.guoShi || "視乎品種";
                existing.guoQi = existing.guoQi || "視乎品種";
                existing.hkRareCategory = existing.hkRareCategory || (plantDetails.rarePrecious ? "VU 易危" : "LC 無危");
                existing.cnRedBookCategory = existing.cnRedBookCategory || (plantDetails.rarePrecious ? "NT 近危" : "LC 無危");"""

text = text.replace(update_existing_old, update_existing_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
