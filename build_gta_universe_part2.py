import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# ------------------------------------------------------------------------------
# 2. SCATTERED ASTEROIDS ACROSS THE ENTIRE 3D UNIVERSE
# ------------------------------------------------------------------------------
# Replace the old belt-only asteroids with 4,500 omnidirectional scattered asteroids!
old_belt_code = '''    // --- 6. MAIN ASTEROID BELT (TOROIDAL RING OF 2,200 ASTEROIDS) ---
    const beltCount = 2200;
    const beltGeo = new THREE.BufferGeometry();
    const beltPositions = new Float32Array(beltCount * 3);
    const beltColors = new Float32Array(beltCount * 3);
    const beltAngles = new Float32Array(beltCount);
    const beltRadii = new Float32Array(beltCount);
    const beltSpeeds = new Float32Array(beltCount);
    const beltHeights = new Float32Array(beltCount);

    for (let i = 0; i < beltCount; i++) {
      const idx = i * 3;
      const angle = Math.random() * Math.PI * 2;
      const radius = 330 + Math.random() * 110;
      const h = (Math.random() - 0.5) * 36;
      const spd = 0.015 + Math.random() * 0.02;

      beltAngles[i] = angle;
      beltRadii[i] = radius;
      beltSpeeds[i] = spd;
      beltHeights[i] = h;

      beltPositions[idx] = Math.cos(angle) * radius;
      beltPositions[idx + 1] = h;
      beltPositions[idx + 2] = -350 + Math.sin(angle) * radius;

      const rockTone = 0.5 + Math.random() * 0.45;
      beltColors[idx] = rockTone;
      beltColors[idx + 1] = rockTone * 0.92;
      beltColors[idx + 2] = rockTone * 0.85;
    }
    beltGeo.setAttribute('position', new THREE.BufferAttribute(beltPositions, 3));
    beltGeo.setAttribute('color', new THREE.BufferAttribute(beltColors, 3));
    const beltMat = new THREE.PointsMaterial({
      size: 2.2, vertexColors: true, transparent: true, opacity: 0.85
    });
    const asteroidBeltPoints = new THREE.Points(beltGeo, beltMat);
    cosmosScene.add(asteroidBeltPoints);'''

new_scattered_asteroids_code = '''    // --- 6. OMNIDIRECTIONAL SCATTERED ASTEROID FIELDS (4,500 ASTEROIDS EVERYWHERE) ---
    // Asteroids scattered across the entire 3D universe in all directions (+X, -X, +Y, -Y, +Z, -Z)
    const beltCount = 4500;
    const beltGeo = new THREE.BufferGeometry();
    const beltPositions = new Float32Array(beltCount * 3);
    const beltColors = new Float32Array(beltCount * 3);
    const beltVelocities = new Float32Array(beltCount * 3);

    for (let i = 0; i < beltCount; i++) {
      const idx = i * 3;
      // Scatter broadly across deep space from -12,000 to +12,000 units
      const spreadX = (Math.random() - 0.5) * 24000;
      const spreadY = (Math.random() - 0.5) * 16000;
      const spreadZ = (Math.random() - 0.5) * 24000;

      beltPositions[idx]     = spreadX;
      beltPositions[idx + 1] = spreadY;
      beltPositions[idx + 2] = spreadZ;

      beltVelocities[idx]     = (Math.random() - 0.5) * 1.8;
      beltVelocities[idx + 1] = (Math.random() - 0.5) * 1.2;
      beltVelocities[idx + 2] = (Math.random() - 0.5) * 1.8;

      const rockTone = 0.45 + Math.random() * 0.55;
      beltColors[idx]     = rockTone;
      beltColors[idx + 1] = rockTone * 0.90;
      beltColors[idx + 2] = rockTone * 0.82;
    }
    beltGeo.setAttribute('position', new THREE.BufferAttribute(beltPositions, 3));
    beltGeo.setAttribute('color', new THREE.BufferAttribute(beltColors, 3));
    const beltMat = new THREE.PointsMaterial({
      size: 3.2, vertexColors: true, transparent: true, opacity: 0.88
    });
    const asteroidBeltPoints = new THREE.Points(beltGeo, beltMat);
    cosmosScene.add(asteroidBeltPoints);'''

if old_belt_code in text:
    text = text.replace(old_belt_code, new_scattered_asteroids_code)
    print("Scattered 4,500 asteroids across the entire 3D cosmos!")
else:
    print("Warning: old_belt_code not matched!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Part 2 complete.")
