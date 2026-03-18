import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update buttons
btn_old = """                <div class="controls">
                    <button id="btn-start" class="start-btn" type="button" onclick="init()">1. Start Camera</button>
                    <button id="btn-capture" class="scan-btn" type="button" onclick="captureAndIdentify()">2. Scan Plant</button>
                    <button id="btn-upload" class="upload-btn" type="button" onclick="document.getElementById('image-upload').click()">3. Upload Plant Photo</button>
                    <input type="file" id="image-upload" accept="image/*" style="display: none;" onchange="handleImageUpload(event)">
                </div>"""

btn_new = """                <div class="controls">
                    <button id="btn-tutorial" class="tutorial-btn" type="button" onclick="showTutorial()" style="background:#4b6b5f; color:#fff;">How to Use (Tutorial)</button>
                    <hr style="width:100%; border:0; margin: 4px 0;">
                    <select id="camera-select" style="padding:10px; border-radius:10px; border:1px solid #ccc; max-width:200px; display:none;" onchange="switchCamera()"></select>
                    <button id="btn-start" class="start-btn" type="button" onclick="startCustomCamera()">Start Camera</button>
                    <button id="btn-capture" class="scan-btn" type="button" onclick="captureAndIdentify()">Scan Plant</button>
                    <button id="btn-upload" class="upload-btn" type="button" onclick="document.getElementById('image-upload').click()">Upload Plant Photo</button>
                    <input type="file" id="image-upload" accept="image/*" style="display: none;" onchange="handleImageUpload(event)">
                </div>"""

text = text.replace(btn_old, btn_new)

# 2. Add video tag instead of webcam-container contents
cam_old = """                <div id="webcam-container" class="camera-shell"></div>"""
cam_new = """                <div id="webcam-container" class="camera-shell">
                    <video id="webcam-video" autoplay playsinline style="width: 100%; height: 100%; object-fit: cover; display: none;"></video>
                    <canvas id="snapshot-canvas" style="display: none;"></canvas>
                </div>"""
text = text.replace(cam_old, cam_new)

# 3. Add Tutorial Modal
tut_new = """
    <div id="tutorialModal" class="modal">
        <div class="modal-content">
            <div class="modal-head">
                <h3 style="margin:0; color:var(--deep-green);">How to Use</h3>
                <button class="close-btn" type="button" onclick="document.getElementById('tutorialModal').style.display='none'">&times;</button>
            </div>
            <div style="margin-top: 15px; line-height: 1.6; color: #2f4d40;">
                <p>Welcome to the Plant Mission Notebook!</p>
                <ol>
                    <li><strong>Start Camera:</strong> Click to turn on your device's camera. You can select different cameras (front/rear) from the dropdown above if available.</li>
                    <li><strong>Scan Plant:</strong> Point the camera at a clear leaf or flower, then click Scan. The system ensures the image contains at least 40% green area.</li>
                    <li><strong>Upload Photo:</strong> Alternatively, upload an existing plant photo from your gallery.</li>
                    <li><strong>Unlock Profile:</strong> Once successfully scanned, ecological data (Hong Kong / China conservation status, flowering/fruiting info) will be synced to your Notebook.</li>
                </ol>
            </div>
        </div>
    </div>
"""
text = text.replace('    <div id="toast" class="toast"></div>', tut_new + '\n    <div id="toast" class="toast"></div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

