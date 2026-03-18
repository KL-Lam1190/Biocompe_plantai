# Plant Mission Notebook

Plant Mission Notebook is an educational web game that uses a Teachable Machine image model to help students and the public recognize plants in an interactive way.

Instead of only searching plant names, users play missions:
- Scan a plant (camera or uploaded image)
- Reach confidence targets
- Unlock mission progress and points
- Collect plants in a personal Plant Book

Each unlocked Plant Notebook card includes:
- Plant photo
- Plant name
- Plant type
- Hong Kong status note
- Mission note and study hint

## Project Pages

- [index.html](index.html): Main scanner game (missions + unlock system + Plant Book)
- [academy.html](academy.html): Plant Notebook page with unlocked photos and plant information
- [product.html](product.html): Product introduction and concept overview

## Key Features

1. Mission-based learning with confidence thresholds
2. Gamification (points, streak, mission completion)
3. Plant Book collection with stored photos and metadata
4. Public-friendly Hong Kong status information for each unlocked plant
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

This project is designed for students and public users to combine AI tools with scientific observation:
- AI gives a prediction
- Missions give motivation
- Plant notebook notes build understanding