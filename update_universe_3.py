import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

idx_start = text.find("async function startCamera() {")
idx_audio = text.find("// --- SOUND EFFECTS (Web Audio API) ---")

new_camera_code = '''async function startCamera() {
      camLabel.textContent = "Connecting...";
      pipBox.classList.add('active');

      try {
        // 1. Initialize MediaPipe Hands for Dual Fist & 2-Finger Flight
        handsInstance = new Hands({
          locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`
        });
        handsInstance.setOptions({
          maxNumHands: 2,
          modelComplexity: 1,
          minDetectionConfidence: 0.65,
          minTrackingConfidence: 0.65
        });
        handsInstance.onResults(onHandResults);

        // 2. Initialize MediaPipe FaceMesh for Eye-Blink Direction Change
        faceMeshInstance = new FaceMesh({
          locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/${file}`
        });
        faceMeshInstance.setOptions({
          maxNumFaces: 1,
          refineLandmarks: true,
          minDetectionConfidence: 0.6,
          minTrackingConfidence: 0.6
        });
        faceMeshInstance.onResults(onFaceResults);

        // 3. Shared camera stream with interleaved AI execution for silky 60 FPS
        cameraInstance = new Camera(pipVideo, {
          onFrame: async () => {
            if (!isCameraActive) return;
            cameraFrameCounter++;
            // Interleave frames: hands get 30 FPS, face gets 30 FPS
            if (cameraFrameCounter % 2 === 0) {
              await handsInstance.send({ image: pipVideo });
            } else if (faceMeshInstance) {
              await faceMeshInstance.send({ image: pipVideo });
            }
          },
          width: 320,
          height: 240
        });

        await cameraInstance.start();
        isCameraActive = true;
        camBtn.classList.add('active');
        camLabel.textContent = "Close Camera";
        pipStatus.textContent = "Show Hands / Blink Eyes";
      } catch (err) {
        console.error("Camera access error:", err);
        alert("Camera permission was not granted or camera is busy. You can use mouse, W/S keys to fly, and B key to blink!");
        stopCamera();
      }
    }

    function stopCamera() {
      if (cameraInstance) {
        cameraInstance.stop();
        cameraInstance = null;
      }
      isCameraActive = false;
      handTrackingActive = false;
      isTwoFingerFlying = false;
      if (flightIndicatorEl) flightIndicatorEl.classList.remove('active');
      pipBox.classList.remove('active');
      camBtn.classList.remove('active');
      camLabel.textContent = "Open Camera";
      setClenched(false);
    }

    // --- EYE BLINK DETECTION VIA MEDIAPIPE FACEMESH EAR ---
    function onFaceResults(results) {
      if (!results.multiFaceLandmarks || results.multiFaceLandmarks.length === 0) return;
      const lm = results.multiFaceLandmarks[0];

      // Eye Aspect Ratio (EAR)
      // Left eye landmarks: 159 (upper), 145 (lower), 33 (outer), 133 (inner)
      const leftV = Math.hypot(lm[159].x - lm[145].x, lm[159].y - lm[145].y);
      const leftH = Math.hypot(lm[33].x - lm[133].x, lm[33].y - lm[133].y) + 1e-6;
      const leftEAR = leftV / leftH;

      // Right eye landmarks: 386 (upper), 374 (lower), 362 (inner), 263 (outer)
      const rightV = Math.hypot(lm[386].x - lm[374].x, lm[386].y - lm[374].y);
      const rightH = Math.hypot(lm[362].x - lm[263].x, lm[362].y - lm[263].y) + 1e-6;
      const rightEAR = rightV / rightH;

      const avgEAR = (leftEAR + rightEAR) * 0.5;
      const now = performance.now() * 0.001;

      // Normal open eyes: EAR ~ 0.24-0.38; blink drops below 0.16
      if (avgEAR < 0.16) {
        if (!wasEyeBlinking && (now - lastBlinkTime > 0.8)) {
          wasEyeBlinking = true;
          lastBlinkTime = now;
          cycleDestination();
        }
      } else if (avgEAR > 0.20) {
        wasEyeBlinking = false;
      }
    }

    // --- HAND GESTURES: 2-FINGER FLIGHT & DUAL FIST COMBAT ---
    function onHandResults(results) {
      const numHands = results.multiHandLandmarks ? results.multiHandLandmarks.length : 0;

      if (numHands === 0) {
        pipStatus.textContent = "No Hand Detected";
        pipStatus.className = "pip-status";
        handTrackingActive = false;
        dualFists[0].tracked = false;
        dualFists[1].tracked = false;
        isTwoFingerFlying = false;
        if (flightIndicatorEl) flightIndicatorEl.classList.remove('active');
        if (!isManualHeld) {
          dualFists[0].isClenched = false;
          dualFists[1].isClenched = false;
        }
        return;
      }

      handTrackingActive = true;

      const detected = [];
      let anyTwoFingerActive = false;

      for (let h = 0; h < numHands; h++) {
        const lm = results.multiHandLandmarks[h];
        const wrist = lm[0];
        const handNormX = 1.0 - lm[9].x; // 0 (left) to 1 (right)
        const handNormY = lm[9].y;       // 0 (top) to 1 (bottom)

        const handSpan = Math.hypot(lm[0].x - lm[9].x, lm[0].y - lm[9].y);
        const punchDepth = THREE.MathUtils.clamp((handSpan - 0.16) / 0.16, -0.6, 1.8);

        function dist(p1, p2) {
          return Math.hypot(p1.x - p2.x, p1.y - p2.y, (p1.z || 0) - (p2.z || 0));
        }

        // Finger curl checks relative to MCP/PIP joints
        const indexCurled  = dist(lm[8], wrist) < dist(lm[6], wrist) * 1.05;
        const middleCurled = dist(lm[12], wrist) < dist(lm[10], wrist) * 1.05;
        const ringCurled   = dist(lm[16], wrist) < dist(lm[14], wrist) * 1.05;
        const pinkyCurled  = dist(lm[20], wrist) < dist(lm[18], wrist) * 1.05;

        const fistClenched = indexCurled && middleCurled && ringCurled && pinkyCurled;

        // 2-Finger Flight Gesture:
        // The two fingers after the thumb (Index #8 and Middle #12) extended outward,
        // while Ring #16 and Pinky #20 are curled inward
        const indexExtended  = dist(lm[8], wrist) > dist(lm[6], wrist) * 1.15;
        const middleExtended = dist(lm[12], wrist) > dist(lm[10], wrist) * 1.15;
        const twoFingerThrust = indexExtended && middleExtended && ringCurled && pinkyCurled;

        if (twoFingerThrust) {
          anyTwoFingerActive = true;
        }

        detected.push({
          lm,
          handNormX,
          handNormY,
          punchDepth,
          fistClenched,
          twoFingerThrust
        });
      }

      // Update 2-Finger flight state and HUD indicator
      isTwoFingerFlying = anyTwoFingerActive;
      if (flightIndicatorEl) {
        flightIndicatorEl.classList.toggle('active', isTwoFingerFlying);
      }

      // Sort by horizontal screen position: leftmost hand -> Left Fist, rightmost -> Right Fist
      detected.sort((a, b) => a.handNormX - b.handNormX);

      // Camera view steering: average center of detected hands in all directions
      const avgNormX = detected.reduce((sum, d) => sum + d.handNormX, 0) / detected.length;
      const avgNormY = detected.reduce((sum, d) => sum + d.handNormY, 0) / detected.length;

      const tiltUp = -(avgNormY - 0.5) * 0.65;
      const panSide = -(avgNormX - 0.5) * 0.85;
      targetRotationX = THREE.MathUtils.clamp(tiltUp, -Math.PI / 2.3, Math.PI / 2.3);
      targetRotationY = panSide;
      targetCameraY = -(avgNormY - 0.5) * 16;
      targetCameraX = (avgNormX - 0.5) * 22;

      if (detected.length >= 2) {
        // BOTH HANDS ACTIVE
        const leftData = detected[0];
        const rightData = detected[1];

        // Left Fist
        dualFists[0].tracked = true;
        dualFists[0].targetWorldPos.x = (leftData.handNormX - 0.5) * 62;
        dualFists[0].targetWorldPos.y = -(leftData.handNormY - 0.5) * 44;
        dualFists[0].targetWorldPos.z = 18 - leftData.punchDepth * 28;
        dualFists[0].isClenched = leftData.fistClenched || isManualHeld;

        // Right Fist
        dualFists[1].tracked = true;
        dualFists[1].targetWorldPos.x = (rightData.handNormX - 0.5) * 62;
        dualFists[1].targetWorldPos.y = -(rightData.handNormY - 0.5) * 44;
        dualFists[1].targetWorldPos.z = 18 - rightData.punchDepth * 28;
        dualFists[1].isClenched = rightData.fistClenched || isManualHeld;

        if (anyTwoFingerActive) {
          pipStatus.textContent = "🚀 2-Finger Flight Thrust!";
          pipStatus.className = "pip-status flight";
        } else if (dualFists[0].isClenched && dualFists[1].isClenched) {
          pipStatus.textContent = "✊✊ BOTH FISTS CLENCHED!";
          pipStatus.className = "pip-status fist";
        } else if (dualFists[0].isClenched) {
          pipStatus.textContent = "✊ Left Fist | ✋ Right Hand";
          pipStatus.className = "pip-status fist";
        } else if (dualFists[1].isClenched) {
          pipStatus.textContent = "✋ Left Hand | ✊ Right Fist";
          pipStatus.className = "pip-status fist";
        } else {
          pipStatus.textContent = "✋✋ Both Hands Open";
          pipStatus.className = "pip-status open";
        }
      } else {
        // ONE HAND ACTIVE
        const d = detected[0];
        const isLeft = d.handNormX < 0.5;
        const activeIdx = isLeft ? 0 : 1;
        const idleIdx = isLeft ? 1 : 0;

        dualFists[activeIdx].tracked = true;
        dualFists[activeIdx].targetWorldPos.x = (d.handNormX - 0.5) * 58;
        dualFists[activeIdx].targetWorldPos.y = -(d.handNormY - 0.5) * 42;
        dualFists[activeIdx].targetWorldPos.z = 18 - d.punchDepth * 28;
        dualFists[activeIdx].isClenched = d.fistClenched || isManualHeld;

        dualFists[idleIdx].tracked = false;
        dualFists[idleIdx].isClenched = isManualHeld;
        dualFists[idleIdx].targetWorldPos.x = isLeft ? 16 : -16;
        dualFists[idleIdx].targetWorldPos.y = -3;
        dualFists[idleIdx].targetWorldPos.z = 18;

        if (anyTwoFingerActive) {
          pipStatus.textContent = "🚀 2-Finger Flight Thrust!";
          pipStatus.className = "pip-status flight";
        } else if (d.fistClenched) {
          pipStatus.textContent = `✊ ${isLeft ? "Left" : "Right"} Fist • Raise 2nd Hand`;
          pipStatus.className = "pip-status fist";
        } else {
          pipStatus.textContent = `✋ 1 Hand Open • Raise 2nd Hand`;
          pipStatus.className = "pip-status open";
        }
      }
    }
'''

text = text[:idx_start] + new_camera_code + "\n\n    " + text[idx_audio:]
with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Step 3 complete: Camera, FaceMesh EAR, and 2-Finger flight updated!")
