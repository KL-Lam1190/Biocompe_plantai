import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Enhance green threshold check and add computer vision heuristics
improved_cv_logic = """
        function calculateGreenPercentage(imageSource) {
            const tempCanvas = document.createElement("canvas");
            const ctx = tempCanvas.getContext("2d");
            tempCanvas.width = imageSource.width || imageSource.videoWidth || 360;
            tempCanvas.height = imageSource.height || imageSource.videoHeight || 360;
            if (tempCanvas.width === 0 || tempCanvas.height === 0) return 100;
            
            ctx.drawImage(imageSource, 0, 0, tempCanvas.width, tempCanvas.height);
            const data = ctx.getImageData(0, 0, tempCanvas.width, tempCanvas.height).data;
            let greenPixels = 0;
            let totalPixels = tempCanvas.width * tempCanvas.height;
            
            // Computer Vision Heuristic:
            // Relaxed green criteria to account for shadows, highlights and different plant hues (like yellowish green or dark leaves)
            for (let i = 0; i < data.length; i += 4) {
                const r = data[i];
                const g = data[i + 1];
                const b = data[i + 2];
                
                // HSL/HSV approximation for green hue dominance
                // A pixel is considered 'plant-like' if Green is the dominant color, 
                // OR if it's a dark/shadow plant area (preventing rejection of real plants under bad lighting)
                if ((g > r * 0.9 && g > b * 0.8 && g > 20) || (g > 50 && r < 100 && b < 100)) {
                    greenPixels++;
                }
            }
            return (greenPixels / totalPixels) * 100;
        }

        function analyzeColorVariance(imageSource) {
            const tempCanvas = document.createElement("canvas");
            const ctx = tempCanvas.getContext("2d");
            tempCanvas.width = imageSource.width || imageSource.videoWidth || 360;
            tempCanvas.height = imageSource.height || imageSource.videoHeight || 360;
            if (tempCanvas.width === 0 || tempCanvas.height === 0) {
                return { variance: 0, greenPct: 0 };
            }

            ctx.drawImage(imageSource, 0, 0, tempCanvas.width, tempCanvas.height);
            const data = ctx.getImageData(0, 0, tempCanvas.width, tempCanvas.height).data;
            
            let count = 0;
            let sum = 0;
            let sumSq = 0;
            let greenPixels = 0;

            for (let i = 0; i < data.length; i += 4) {
                const r = data[i];
                const g = data[i + 1];
                const b = data[i + 2];
                const brightness = 0.299 * r + 0.587 * g + 0.114 * b;

                sum += brightness;
                sumSq += brightness * brightness;
                count += 1;

                if ((g > r * 0.9 && g > b * 0.8 && g > 20) || (g > 50 && r < 100 && b < 100)) {
                    greenPixels += 1;
                }
            }

            const mean = sum / count;
            const variance = Math.max(0, sumSq / count - mean * mean);
            const greenPct = (greenPixels / count) * 100;

            return { variance, greenPct };
        }
"""

content = re.sub(
    r'function calculateGreenPercentage\(imageSource\).*?return \{ variance, greenPct \};\n        \}',
    improved_cv_logic.strip(),
    content,
    flags=re.DOTALL
)

# Update runPrediction validation logic
old_pred = """const greenPct = calculateGreenPercentage(imageSource);
            if (greenPct < 40) {
                updateModal(
                    "Not Enough Green / Not a Plant",
                    `This photo has only ${greenPct.toFixed(1)}% green area. A plant photo must be >40% green.`
                );
                showToast("Not enough green.", true);
                return;
            }

            const quality = analyzeColorVariance(imageSource);
            const isFlatGreenSurface = quality.greenPct > 55 && quality.variance < 220;
            if (isFlatGreenSurface) {
                game.streak = 0;
                renderStats();
                updateModal(
                    "Sorry, Not Able",
                    "Sorry, it is not able to identify this image. It looks like a flat green surface, not a clear plant target."
                );
                showToast("Sorry, it is not able to identify this image.", true);
                return;
            }"""

new_pred = """const quality = analyzeColorVariance(imageSource);
            const greenPct = quality.greenPct;
            
            // Validate if it is actually a plant using Computer Vision heuristics
            // Plants are rarely perfectly flat colors, they have texture (variance)
            if (greenPct < 15) {
                updateModal("Not a Plant Detected", `We couldn't detect enough plant-like features (Green area: ${greenPct.toFixed(1)}%). Please make sure the plant is clearly visible and well-lit.`);
                showToast("Not enough plant area detected.", true);
                return;
            }

            const isFlatColorSurface = quality.greenPct > 40 && quality.variance < 100;
            if (isFlatColorSurface) {
                game.streak = 0;
                renderStats();
                updateModal("Invalid Photo", "This looks like a flat artificial surface (like a green wall or paper) because it lacks natural plant texture and shadows. Please scan a real plant.");
                showToast("Rejected: Flat artificial surface detected.", true);
                return;
            }"""

content = content.replace(old_pred, new_pred)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("CV heuristic updated.")
