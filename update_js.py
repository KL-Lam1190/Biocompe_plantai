import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add tutorial open function
if "function showTutorial()" not in text:
    text = text.replace("function loadModel()", "function showTutorial() { document.getElementById('tutorialModal').style.display='block'; }\n\n        function loadModel()")

# Replace old init with startCustomCamera, add enumeration and switching
old_init = """        async function init() {
            const startButton = document.getElementById("btn-start");
            startButton.textContent = "Loading model...";

            try {
                await loadModel();

                if (!webcam) {
                    const flip = true;
                    webcam = new tmImage.Webcam(360, 360, flip);
                    await webcam.setup();
                    await webcam.play();
                    loop();

                    const webcamContainer = document.getElementById("webcam-container");
                    webcamContainer.innerHTML = "";
                    webcamContainer.appendChild(webcam.canvas);
                }

                startButton.style.display = "none";
                document.getElementById("btn-capture").style.display = "inline-block";
                showToast("Camera ready. Start your mission scan.");
            } catch (error) {
                startButton.textContent = "Start Camera";
                showToast("Cannot start camera. Check permission and try again.", true);
            }
        }

        function loop() {
            if (!webcam) {
                return;
            }

            webcam.update();
            animationId = window.requestAnimationFrame(loop);
        }"""

new_init = """        let currentStream;

        async function populateCameras() {
            const select = document.getElementById("camera-select");
            try {
                if (!navigator.mediaDevices || !navigator.mediaDevices.enumerateDevices) return;
                const devices = await navigator.mediaDevices.enumerateDevices();
                const videoDevices = devices.filter(device => device.kind === 'videoinput');
                select.innerHTML = "";
                if (videoDevices.length > 0) {
                    select.style.display = "inline-block";
                    videoDevices.forEach((device, index) => {
                        const option = document.createElement("option");
                        option.value = device.deviceId;
                        option.text = device.label || `Camera ${index + 1}`;
                        select.appendChild(option);
                    });
                }
            } catch (e) {
                console.error("Camera enumerate error", e);
            }
        }

        async function startCustomCamera(deviceId = null) {
            const startButton = document.getElementById("btn-start");
            startButton.textContent = "Loading...";

            try {
                await loadModel();
                
                if (currentStream) {
                    currentStream.getTracks().forEach(track => track.stop());
                }

                const constraints = { video: deviceId ? { deviceId: { exact: deviceId } } : { facingMode: 'environment' } };
                currentStream = await navigator.mediaDevices.getUserMedia(constraints);
                
                const video = document.getElementById("webcam-video");
                video.srcObject = currentStream;
                video.style.display = "block";
                
                await new Promise((resolve) => {
                    video.onloadedmetadata = () => resolve();
                });
                
                // Populate cameras on first load
                if (!deviceId) {
                    await populateCameras();
                }

                startButton.style.display = "none";
                document.getElementById("btn-capture").style.display = "inline-block";
                showToast("Camera ready. Start your mission scan.");
            } catch (error) {
                startButton.textContent = "Start Camera";
                showToast("Cannot start camera. Check permission.", true);
            }
        }

        async function switchCamera() {
            const select = document.getElementById("camera-select");
            const deviceId = select.value;
            if (deviceId) {
                await startCustomCamera(deviceId);
            }
        }"""

text = text.replace(old_init, new_init)


# Replace captureAndIdentify
old_capture = """        async function captureAndIdentify() {
            if (!webcam || !webcam.canvas) {
                showToast("Start camera first.", true);
                return;
            }

            showModal("Analyzing Plant...", "Checking your scan with Teachable Machine.", true);
            const imageData = webcam.canvas.toDataURL("image/jpeg");
            document.getElementById("modal-image").src = imageData;
            document.getElementById("modal-image").style.display = "block";
            await runPrediction(webcam.canvas, imageData);
        }"""

new_capture = """        async function captureAndIdentify() {
            const video = document.getElementById("webcam-video");
            if (!video || !currentStream) {
                showToast("Start camera first.", true);
                return;
            }

            showModal("Analyzing Plant...", "Checking your scan.", true);
            
            const canvas = document.getElementById("snapshot-canvas");
            canvas.width = video.videoWidth || 360;
            canvas.height = video.videoHeight || 360;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            
            const imageData = canvas.toDataURL("image/jpeg");
            document.getElementById("modal-image").src = imageData;
            document.getElementById("modal-image").style.display = "block";
            
            await runPrediction(canvas, imageData);
        }"""

text = text.replace(old_capture, new_capture)


# Add real data for HongKongPlantCatalog
data_old = """            rose: {
                type: "Flowering Shrub",
                hkStatus: "Common cultivated ornamental in Hong Kong gardens.",
                publicNote: "Check petal layers and thorn layout for easier recognition.",
                rarePrecious: false,
                rarityNote: "Not usually listed as a rare or precious species in Hong Kong." 
            },"""

data_new = """            "incense tree": {
                type: "常綠喬木 (Evergreen Tree)",
                shengTai: "常見於風水林及郊野叢林",
                hua: "黃綠色、鐘形",
                huaQi: "4月 - 5月",
                guoShi: "卵形木質蒴果",
                guoQi: "7月 - 8月",
                hkStatus: "Native Native | Species of Conservation Concern",
                hkRareCategory: "VU 易危",
                cnRedBookCategory: "VU 易危",
                publicNote: "土沉香 (Aquilaria sinensis) 是香港早期香木業重要樹種，野外群落受法例保護。",
                rarePrecious: true,
                rarityNote: "列入《國家重點保護野生植物名錄》."
            },
            "hong kong balsam": {
                type: "草本植物 (Herb)",
                shengTai: "生長於山谷林下潮濕地及溪邊",
                hua: "紫紅色、形似漏斗",
                huaQi: "8月 - 10月",
                guoShi: "蒴果",
                guoQi: "10月 - 11月",
                hkStatus: "Endemic (香港特有種) | Species of Conservation Concern",
                hkRareCategory: "EN 瀕危",
                cnRedBookCategory: "未列入 (但受本地高度保護)",
                publicNote: "香港鳳仙 (Impatiens hongkongensis) 首次在香港島發現，屬極受保護的本地特有品種。",
                rarePrecious: true,
                rarityNote: "香港特有種，受林務規例保護."
            },
            "grano": {
                type: "常綠灌木或小喬木",
                shengTai: "海岸及次生林邊緣",
                hua: "白色或淡黃色小花",
                huaQi: "春季",
                guoShi: "核果，熟時黑紫色",
                guoQi: "夏秋季",
                hkStatus: "Native native species in specific coastal areas",
                hkRareCategory: "LC 無危",
                cnRedBookCategory: "LC 無危",
                publicNote: "常見的灌木，果實為許多野鳥的食物來源。",
                rarePrecious: false,
                rarityNote: "普遍野生品種，未列入稀有級別。"
            },
            rose: {
                type: "灌木 (Flowering Shrub)",
                shengTai: "廣泛栽培",
                hua: "多種顏色",
                huaQi: "幾乎全年",
                guoShi: "薔薇果",
                guoQi: "秋季",
                hkStatus: "Common cultivated ornamental in Hong Kong gardens.",
                hkRareCategory: "LC 無危",
                cnRedBookCategory: "LC 無危",
                publicNote: "園藝觀賞植物",
                rarePrecious: false,
                rarityNote: "外來引入培植種。" 
            },"""

text = text.replace(data_old, data_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

