import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. ADD VISHVARUPA ASTRAL GOD & SUDARSHANA CHAKRA RIGHT AFTER BLACK HOLE
astral_code = '''
    // ==============================================================
    // --- 7. VISHVARUPA: THE ASTRAL GOD & SUDARSHANA CHAKRA ---
    // Inspired directly by the celestial Vishnu/Krishna form & Ramayana cosmic VFX
    // A monumental stardust deity with a radiant spinning Sudarshana Chakra
    // ==============================================================
    const astralGodGroup = new THREE.Group();
    astralGodGroup.position.set(160, 140, -680);
    cosmosScene.add(astralGodGroup);

    // Generate Celestial Stardust Point Cloud for the Deity
    const astralCount = 14000;
    const astralGeo = new THREE.BufferGeometry();
    const astralPositions = new Float32Array(astralCount * 3);
    const astralColors = new Float32Array(astralCount * 3);

    const cGold = new THREE.Color(0xfacc15);
    const cCyan = new THREE.Color(0x38bdf8);
    const cWhite = new THREE.Color(0xffffff);
    const cIndigo = new THREE.Color(0x818cf8);
    const tmpColor = new THREE.Color();

    for (let i = 0; i < astralCount; i++) {
      const idx = i * 3;
      let x = 0, y = 0, z = 0;
      let col = cCyan;
      const part = Math.random();

      if (part < 0.16) {
        // Crown / Mukut & Peacock Feather Plume
        const h = Math.random();
        const arch = Math.sin(h * Math.PI) * 7.5;
        x = (Math.random() - 0.5) * arch;
        y = 48 + h * 24;
        z = (Math.random() - 0.5) * 5.0;
        col = (h > 0.75) ? cCyan : cGold; // Peacock feather peak is cyan/emerald, base is gold
      } else if (part < 0.32) {
        // Serene Face, Tilak & Divine Halo
        const angle = Math.random() * Math.PI * 2;
        const rad = Math.random() * 8.5;
        x = Math.cos(angle) * rad;
        y = 35 + Math.sin(angle) * rad * 1.25;
        z = (Math.random() - 0.5) * 4.5;
        if (Math.abs(x) < 0.8 && y > 35 && y < 45) {
          col = cGold; // Sacred Urdhva Pundra Tilak
        } else {
          col = (Math.random() < 0.5) ? cWhite : cCyan;
        }
      } else if (part < 0.52) {
        // Divine Torso, Sacred Thread (Yajnopavita) & Royal Necklaces
        const h = Math.random();
        const taper = 14 - h * 5;
        x = (Math.random() - 0.5) * taper;
        y = 12 + h * 23;
        z = (Math.random() - 0.5) * 7;
        col = (Math.random() < 0.45) ? cGold : cIndigo;
      } else if (part < 0.72) {
        // Raised Right Arm & Index Finger (holding Sudarshana Chakra)
        const t = Math.random();
        if (t < 0.6) {
          // Forearm angled upward towards the Chakra
          x = 10 + t * 24;
          y = 26 + t * 44;
          z = (Math.random() - 0.5) * 4.5;
        } else {
          // Left blessing hand
          x = -10 - (t - 0.6) * 18;
          y = 22 + (t - 0.6) * 12;
          z = (Math.random() - 0.5) * 4.5;
        }
        col = cCyan;
      } else {
        // Flowing Celestial Dhoti / Pitambara Robes
        const h = Math.random();
        const skirtSpread = 8 + (1.0 - h) * 22;
        x = (Math.random() - 0.5) * skirtSpread;
        y = -40 + h * 52;
        z = (Math.random() - 0.5) * 8;
        col = (Math.random() < 0.65) ? cGold : cIndigo;
      }

      // Add gentle cosmic dust scatter
      x += (Math.random() - 0.5) * 1.5;
      y += (Math.random() - 0.5) * 1.5;
      z += (Math.random() - 0.5) * 1.5;

      astralPositions[idx] = x;
      astralPositions[idx + 1] = y;
      astralPositions[idx + 2] = z;

      tmpColor.copy(col).lerp(cWhite, Math.random() * 0.25);
      astralColors[idx] = tmpColor.r;
      astralColors[idx + 1] = tmpColor.g;
      astralColors[idx + 2] = tmpColor.b;
    }

    astralGeo.setAttribute('position', new THREE.BufferAttribute(astralPositions, 3));
    astralGeo.setAttribute('color', new THREE.BufferAttribute(astralColors, 3));

    const astralMat = new THREE.PointsMaterial({
      size: 1.8,
      vertexColors: true,
      transparent: true,
      opacity: 0.88,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    });
    const astralGodPoints = new THREE.Points(astralGeo, astralMat);
    astralGodGroup.add(astralGodPoints);

    // --- THE SUDARSHANA CHAKRA ---
    // Blazing sacred wheel of pure divine starlight spinning above the raised finger
    const sudarshanaGroup = new THREE.Group();
    sudarshanaGroup.position.set(24.5, 74, 0); // Directly above raised index finger
    astralGodGroup.add(sudarshanaGroup);

    // 1. Outer Flaming Serrated Energy Rim
    const chakraOuterGeo = new THREE.RingGeometry(12, 17.5, 72);
    const chakraOuterMat = new THREE.MeshBasicMaterial({
      color: 0xf59e0b, transparent: true, opacity: 0.82, side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending, depthWrite: false
    });
    const sudarshanaOuterDisc = new THREE.Mesh(chakraOuterGeo, chakraOuterMat);
    sudarshanaGroup.add(sudarshanaOuterDisc);

    // 2. Inner Radiant 12-Spoke Sacred Wheel
    const chakraInnerGeo = new THREE.RingGeometry(2.5, 12, 36);
    const chakraInnerMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8, transparent: true, opacity: 0.75, side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending, depthWrite: false
    });
    const sudarshanaSpokes = new THREE.Mesh(chakraInnerGeo, chakraInnerMat);
    sudarshanaGroup.add(sudarshanaSpokes);

    // 3. Central Dazzling Jewel Core & Volumetric Corona
    const chakraCoreGeo = new THREE.SphereGeometry(2.8, 24, 24);
    const chakraCoreMat = new THREE.MeshBasicMaterial({
      color: 0xffffff, blending: THREE.AdditiveBlending
    });
    const sudarshanaCore = new THREE.Mesh(chakraCoreGeo, chakraCoreMat);
    sudarshanaGroup.add(sudarshanaCore);

    // Radiant Chakra Point Light casting divine aura on the cosmos
    const chakraLight = new THREE.PointLight(0xfef08a, 4.5, 550, 0.4);
    sudarshanaGroup.add(chakraLight);

    // Soft celestial aura sphere around the Deity
    const godAuraGeo = new THREE.SphereGeometry(58, 32, 32);
    const godAuraMat = new THREE.MeshBasicMaterial({
      color: 0x1e3a8a, transparent: true, opacity: 0.14,
      blending: THREE.AdditiveBlending, side: THREE.BackSide, depthWrite: false
    });
    astralGodGroup.add(new THREE.Mesh(godAuraGeo, godAuraMat));
'''

# Find insertion point for astral code
bh_target = "blackHoleGroup.add(blackHoleLensing);"
if bh_target in text and "astralGodGroup" not in text:
    text = text.replace(bh_target, bh_target + "\n" + astral_code)
    print("Added Vishvarupa Astral God and Sudarshana Chakra!")
else:
    print("Astral God already exists or target not found.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Step 1 complete.")
