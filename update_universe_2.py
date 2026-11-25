import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect where keyboard listeners and camera code start
old_nav_code = '''    window.addEventListener('keydown', (e) => {
      if (e.code === 'Space') {
        if (!e.repeat) { setClenched(true); manualBtn.classList.add('active'); }
      } else if (e.code === 'KeyQ') {
        dualFists[0].isClenched = true;
      } else if (e.code === 'KeyE' || e.code === 'KeyF') {
        dualFists[1].isClenched = true;
      }
    });

    window.addEventListener('keyup', (e) => {
      if (e.code === 'Space') {
        setClenched(false); manualBtn.classList.remove('active');
      } else if (e.code === 'KeyQ') {
        dualFists[0].isClenched = false;
      } else if (e.code === 'KeyE' || e.code === 'KeyF') {
        dualFists[1].isClenched = false;
      }
    });
    // --- WEBCAM & MEDIAPIPE AI DUAL HAND TRACKING ---'''

new_nav_code = '''    // ==============================================================
    // --- CELESTIAL DESTINATIONS & EYE-BLINK NAVIGATION SYSTEM ---
    // Destinations spanning the expanded realistic universe
    // ==============================================================
    const celestialDestinations = [
      { name: "THE SUN", pos: new THREE.Vector3(0, 0, -350), r: 45 },
      { name: "EARTH & MOON", pos: new THREE.Vector3(180, 20, -120), r: 14 },
      { name: "MARS (RED PLANET)", pos: new THREE.Vector3(290, -35, -220), r: 8.5 },
      { name: "JUPITER (STORM GIANT)", pos: new THREE.Vector3(-340, 60, -420), r: 32 },
      { name: "SATURN (RINGS)", pos: new THREE.Vector3(-240, -50, -220), r: 24 },
      { name: "GARGANTUA BLACK HOLE", pos: new THREE.Vector3(0, -90, -850), r: 38 },
      { name: "VISHVARUPA ASTRAL GOD", pos: new THREE.Vector3(160, 140, -680), r: 50 }
    ];

    let currentDestIndex = 0;
    let isTwoFingerFlying = false;
    let isKeyboardFlyingForward = false;
    let isKeyboardFlyingBackward = false;
    let flightVelocity = new THREE.Vector3(0, 0, 0);

    let isAutoNavigating = false;
    let autoNavTarget = new THREE.Vector3(0, 0, -350);
    let autoNavTimer = 0.0;

    let wasEyeBlinking = false;
    let lastBlinkTime = 0.0;
    let faceMeshInstance = null;
    let cameraFrameCounter = 0;

    const navDestNameEl = document.getElementById('nav-dest-name');
    const flightIndicatorEl = document.getElementById('flight-indicator');
    const blinkNotifyEl = document.getElementById('blink-notify');

    function cycleDestination() {
      currentDestIndex = (currentDestIndex + 1) % celestialDestinations.length;
      const target = celestialDestinations[currentDestIndex];
      if (navDestNameEl) navDestNameEl.textContent = target.name;

      autoNavTarget.copy(target.pos);
      isAutoNavigating = true;
      autoNavTimer = 3.2;

      if (blinkNotifyEl) {
        blinkNotifyEl.textContent = `👁️ COURSE LOCKED: ${target.name}`;
        blinkNotifyEl.classList.add('visible');
        setTimeout(() => blinkNotifyEl.classList.remove('visible'), 2400);
      }

      triggerWarpChime();
    }

    function triggerWarpChime() {
      if (!audioCtx) initAudio();
      audioCtx.resume();
      const t = audioCtx.currentTime;

      // Harmonic dual chime (528 Hz & 1056 Hz Solfeggio frequencies)
      const osc1 = audioCtx.createOscillator();
      const osc2 = audioCtx.createOscillator();
      const gain1 = audioCtx.createGain();
      const gain2 = audioCtx.createGain();

      osc1.type = 'sine';
      osc2.type = 'triangle';
      osc1.frequency.setValueAtTime(528, t);
      osc1.frequency.exponentialRampToValueAtTime(792, t + 0.6);
      osc2.frequency.setValueAtTime(1056, t);
      osc2.frequency.exponentialRampToValueAtTime(1584, t + 0.7);

      gain1.gain.setValueAtTime(0.28, t);
      gain1.gain.exponentialRampToValueAtTime(0.001, t + 0.85);
      gain2.gain.setValueAtTime(0.18, t);
      gain2.gain.exponentialRampToValueAtTime(0.001, t + 0.95);

      osc1.connect(gain1);
      osc2.connect(gain2);
      gain1.connect(audioCtx.destination);
      gain2.connect(audioCtx.destination);

      osc1.start(t);
      osc2.start(t);
      osc1.stop(t + 0.9);
      osc2.stop(t + 1.0);
    }

    window.addEventListener('keydown', (e) => {
      if (e.code === 'Space') {
        if (!e.repeat) { setClenched(true); manualBtn.classList.add('active'); }
      } else if (e.code === 'KeyQ') {
        dualFists[0].isClenched = true;
      } else if (e.code === 'KeyE' || e.code === 'KeyF') {
        dualFists[1].isClenched = true;
      } else if (e.code === 'KeyB' || e.code === 'KeyC') {
        cycleDestination(); // Manual Eye-Blink / Course change fallback
      } else if (e.code === 'KeyW' || e.code === 'ArrowUp') {
        isKeyboardFlyingForward = true;
      } else if (e.code === 'KeyS' || e.code === 'ArrowDown') {
        isKeyboardFlyingBackward = true;
      }
    });

    window.addEventListener('keyup', (e) => {
      if (e.code === 'Space') {
        setClenched(false); manualBtn.classList.remove('active');
      } else if (e.code === 'KeyQ') {
        dualFists[0].isClenched = false;
      } else if (e.code === 'KeyE' || e.code === 'KeyF') {
        dualFists[1].isClenched = false;
      } else if (e.code === 'KeyW' || e.code === 'ArrowUp') {
        isKeyboardFlyingForward = false;
      } else if (e.code === 'KeyS' || e.code === 'ArrowDown') {
        isKeyboardFlyingBackward = false;
      }
    });
    // --- WEBCAM & MEDIAPIPE AI DUAL HAND & EYE TRACKING ---'''

if old_nav_code in text:
    text = text.replace(old_nav_code, new_nav_code)
    print("Replaced keyboard listeners and added destination navigation state!")
else:
    print("WARNING: old_nav_code not matched exactly. Searching partial...")
    idx = text.find("window.addEventListener('keydown', (e) => {")
    idx_webcam = text.find("// --- WEBCAM & MEDIAPIPE AI DUAL HAND TRACKING ---")
    if idx != -1 and idx_webcam != -1:
        text = text[:idx] + new_nav_code + text[idx_webcam + len("// --- WEBCAM & MEDIAPIPE AI DUAL HAND TRACKING ---"):]
        print("Replaced by slice successfully!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)
