# Plant Mission Academy

Plant Mission Academy is an educational web game that uses a Teachable Machine image model to help students learn botany in an interactive way.

Instead of only searching plant names, users play missions:
- Scan a plant (camera or uploaded image)
- Reach confidence targets
- Unlock mission progress and points
- Collect plants in a personal Plant Book

Each unlocked Plant Book card includes:
- Plant photo
- Plant name
- Plant type
- Academy info (study direction)
- Mission note and study hint

## Project Pages

- [index.html](index.html): Main scanner game (missions + unlock system + Plant Book)
- [academy.html](academy.html): Academy guide that explains plant types and learning focus
- [product.html](product.html): Product introduction and concept overview

## Key Features

1. Mission-based learning with confidence thresholds
2. Gamification (points, streak, mission completion)
3. Plant Book collection with stored photos and metadata
4. Academy-focused study information for each unlocked plant
5. Browser-local storage so unlocked cards remain after refresh

## Tech Stack

- HTML/CSS/JavaScript
- TensorFlow.js
- Teachable Machine Image Library

## Run Locally

1. Open the project in VS Code.
2. Open [index.html](index.html) in browser or use a local static server.
3. Start camera permission and begin scanning plants.

## Educational Goal

This project is designed for students to combine AI tools with scientific observation:
- AI gives a prediction
- Missions give motivation
- Academy notes build understanding