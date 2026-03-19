import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update game object definition
old_game = """const game = {
            missionIndex: 0,
            missionProgress: 0,
            points: 0,
            streak: 0,
            missionsDone: 0,
            book: []
        };"""
new_game = """const game = {
            missionIndex: 0,
            missionProgress: 0,
            points: 0,
            streak: 0,
            missionsDone: 0,
            book: [],
            missionScannedPlants: []
        };"""
content = content.replace(old_game, new_game)

# 2. Update runPrediction success logic
old_pred_success = """const mission = getCurrentMission();
            const confidence = bestMatch.probability;
            const confidencePct = (confidence * 100).toFixed(1);
            const isMissionSuccess = confidence >= mission.minConfidence;

            if (isMissionSuccess) {"""

new_pred_success = """const mission = getCurrentMission();
            const confidence = bestMatch.probability;
            const confidencePct = (confidence * 100).toFixed(1);
            
            const normalizedFoundName = normalizePlantName(bestMatch.className);
            if (game.missionScannedPlants.includes(normalizedFoundName)) {
                updateModal(
                    "Already Scanned",
                    `You already scanned a <b>${bestMatch.className}</b> for this mission. Please find a different plant to complete the mission!`
                );
                showToast("Already scanned this plant for the current mission.", true);
                return;
            }

            const isMissionSuccess = confidence >= mission.minConfidence;

            if (isMissionSuccess) {
                game.missionScannedPlants.push(normalizedFoundName);"""

content = content.replace(old_pred_success, new_pred_success)

# 3. Update mission reset logic
old_reset = """game.missionIndex = Math.min(game.missionIndex + 1, missions.length - 1);
                    game.missionProgress = 0;
                    unlockText = `<br><br><strong>Mission unlocked:</strong> ${mission.name} completed! Bonus +${mission.points} points.`;"""

new_reset = """game.missionIndex = Math.min(game.missionIndex + 1, missions.length - 1);
                    game.missionProgress = 0;
                    game.missionScannedPlants = [];
                    unlockText = `<br><br><strong>Mission unlocked:</strong> ${mission.name} completed! Bonus +${mission.points} points.`;"""

content = content.replace(old_reset, new_reset)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Game logic updated for one plant one mission.")
