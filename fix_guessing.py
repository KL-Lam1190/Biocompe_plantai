import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update inferPlantProfile to enforce strict matching for all plants EXCEPT 南方安蘭
# Wait, the user said "Please don't do any guess for all plant within 南方安蘭". 
# This might mean "Stop using `.includes(key)` which is guessing/fuzzy matching, make it exact".

old_infer = """        function inferPlantProfile(name) {
            const normalized = normalizePlantName(name);
            const matchedKey = Object.keys(hongKongPlantCatalog).find((key) => normalized.includes(key));

            if (matchedKey) {
                return hongKongPlantCatalog[matchedKey];
            }

            return null;
        }"""

new_infer = """        function inferPlantProfile(name) {
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
            });

            if (matchedKey) {
                return hongKongPlantCatalog[matchedKey];
            }

            return null;
        }"""

content = content.replace(old_infer, new_infer)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Infer logic updated for strict matching.")
