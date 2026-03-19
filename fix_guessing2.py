import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make it completely strict for EVERYTHING. No guessing.
old_infer = """        function inferPlantProfile(name) {
            const rawName = name.trim();
            const normalized = normalizePlantName(name);
            
            // Look for exact matches first
            let matchedKey = Object.keys(hongKongPlantCatalog).find((key) => {
                // If it is '南方安蘭', we can allow partial matching if needed, 
                // but for all other plants, we enforce strict matching.
                if (key === '南方安蘭') {
                    return normalized.includes(key) || rawName.includes(key);
                } else {
                    return rawName === key || normalized === key;
                }
            });"""

new_infer = """        function inferPlantProfile(name) {
            const rawName = name.trim();
            
            // Strictly match the name against the catalog keys. NO guessing.
            let matchedKey = Object.keys(hongKongPlantCatalog).find((key) => rawName === key);"""

content = content.replace(old_infer, new_infer)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("No guessing logic applied.")
