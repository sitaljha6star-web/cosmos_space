import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Expand camera far plane & fog so giant universe is visible
text = text.replace("0.1, 8000);", "0.1, 24000);")
text = text.replace("FogExp2(0x010104, 0.00035);", "FogExp2(0x010104, 0.000065);")

# 2. Build the mega celestial code block
mega_celestial_code = '''
    // ==============================================================
    // --- PHOTOREALISTIC PROCEDURAL TEXTURE GENERATORS ---
    // ==============================================================
    function createSunTexture() {
      const c = document.createElement('canvas'); c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');
      const grad = ctx.createLinearGradient(0, 0, 0, 512);
      grad.addColorStop(0.0, '#fffbeb'); grad.addColorStop(0.3, '#fef08a');
      grad.addColorStop(0.65, '#f59e0b'); grad.addColorStop(1.0, '#d97706');
      ctx.fillStyle = grad; ctx.fillRect(0, 0, 1024, 512);

      // Convection granules & solar flare eruptions
      for (let i = 0; i < 4000; i++) {
        const x = Math.random() * 1024, y = Math.random() * 512;
        const rad = Math.random() * 9 + 2;
        ctx.beginPath(); ctx.arc(x, y, rad, 0, Math.PI * 2);
        ctx.fillStyle = Math.random() < 0.65 ? 'rgba(255, 255, 255, 0.45)' : 'rgba(180, 83, 9, 0.4)';
        ctx.fill();
      }
      return new THREE.CanvasTexture(c);
    }

    function createMercuryTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      ctx.fillStyle = '#8c857b'; ctx.fillRect(0, 0, 512, 256);
      for (let i = 0; i < 1800; i++) {
        const x = Math.random() * 512, y = Math.random() * 256;
        const rad = Math.random() * 6 + 1;
        ctx.beginPath(); ctx.arc(x, y, rad, 0, Math.PI * 2);
        ctx.fillStyle = Math.random() < 0.5 ? 'rgba(60, 55, 50, 0.5)' : 'rgba(180, 175, 165, 0.45)';
        ctx.fill();
      }
      return new THREE.CanvasTexture(c);
    }

    function createVenusTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createLinearGradient(0, 0, 0, 256);
      grad.addColorStop(0.0, '#eab308'); grad.addColorStop(0.5, '#fde047'); grad.addColorStop(1.0, '#ca8a04');
      ctx.fillStyle = grad; ctx.fillRect(0, 0, 512, 256);
      // Atmospheric toxic sulfuric streak bands
      for (let i = 0; i < 35; i++) {
        ctx.beginPath();
        const y = Math.random() * 256;
        ctx.ellipse(256, y, 280, Math.random() * 12 + 4, 0.05, 0, Math.PI * 2);
        ctx.fillStyle = Math.random() < 0.5 ? 'rgba(254, 240, 138, 0.35)' : 'rgba(161, 98, 7, 0.3)';
        ctx.fill();
      }
      return new THREE.CanvasTexture(c);
    }

    function createEarthTexture() {
      const c = document.createElement('canvas'); c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');
      ctx.fillStyle = '#0f2b5c'; ctx.fillRect(0, 0, 1024, 512);

      // Deep Ocean trenches and shelf highlights
      for (let i = 0; i < 600; i++) {
        const x = Math.random() * 1024, y = Math.random() * 512;
        ctx.beginPath(); ctx.arc(x, y, Math.random() * 40 + 10, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(6, 78, 120, 0.35)'; ctx.fill();
      }

      // Procedural continents (Afro-Eurasia, Americas, Australia, Antarctica)
      const landPatches = [
        { x: 520, y: 220, rx: 110, ry: 90 }, { x: 580, y: 160, rx: 140, ry: 75 },
        { x: 720, y: 200, rx: 120, ry: 85 }, { x: 260, y: 170, rx: 110, ry: 75 },
        { x: 320, y: 320, rx: 75, ry: 100 }, { x: 790, y: 360, rx: 65, ry: 45 },
        { x: 512, y: 480, rx: 420, ry: 25 }, { x: 512, y: 25, rx: 320, ry: 18 }
      ];
      landPatches.forEach(lp => {
        for (let i = 0; i < 35; i++) {
          const px = lp.x + (Math.random() - 0.5) * lp.rx;
          const py = lp.y + (Math.random() - 0.5) * lp.ry;
          ctx.beginPath();
          ctx.arc(px, py, Math.random() * 32 + 10, 0, Math.PI * 2);
          ctx.fillStyle = py < 50 || py > 460 ? '#f8fafc' : (Math.random() < 0.65 ? '#15803d' : '#854d0e');
          ctx.fill();
        }
      });
      return new THREE.CanvasTexture(c);
    }

    function createEarthCloudsTexture() {
      const c = document.createElement('canvas'); c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');
      ctx.clearRect(0, 0, 1024, 512);
      ctx.fillStyle = 'rgba(255, 255, 255, 0.88)';
      for (let i = 0; i < 500; i++) {
        const x = Math.random() * 1024, y = Math.random() * 512;
        ctx.beginPath();
        ctx.ellipse(x, y, Math.random() * 45 + 12, Math.random() * 15 + 4, Math.random() * 0.6, 0, Math.PI * 2);
        ctx.fill();
      }
      return new THREE.CanvasTexture(c);
    }

    function createMarsTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      ctx.fillStyle = '#b43403'; ctx.fillRect(0, 0, 512, 256);
      for (let i = 0; i < 800; i++) {
        const x = Math.random() * 512, y = Math.random() * 256;
        ctx.beginPath(); ctx.arc(x, y, Math.random() * 18 + 4, 0, Math.PI * 2);
        ctx.fillStyle = Math.random() < 0.6 ? 'rgba(124, 45, 18, 0.45)' : 'rgba(234, 88, 12, 0.35)';
        ctx.fill();
      }
      // Valles Marineris canyon scratch
      ctx.beginPath(); ctx.ellipse(230, 140, 70, 8, -0.15, 0, Math.PI * 2);
      ctx.fillStyle = '#451a03'; ctx.fill();
      // Polar Ice Caps
      ctx.fillStyle = '#ffffff';
      ctx.beginPath(); ctx.ellipse(256, 8, 85, 12, 0, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.ellipse(256, 248, 70, 10, 0, 0, Math.PI * 2); ctx.fill();
      return new THREE.CanvasTexture(c);
    }

    function createJupiterTexture() {
      const c = document.createElement('canvas'); c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');
      const colors = ['#fde68a', '#d97706', '#fed7aa', '#b45309', '#fef3c7', '#78350f', '#fde68a'];
      for (let y = 0; y < 512; y++) {
        const idx = Math.floor((y / 512) * colors.length);
        ctx.fillStyle = colors[idx % colors.length];
        ctx.fillRect(0, y, 1024, 1);
      }
      // Atmospheric turbulence eddies
      for (let i = 0; i < 900; i++) {
        const x = Math.random() * 1024, y = Math.random() * 512;
        ctx.beginPath();
        ctx.ellipse(x, y, Math.random() * 45 + 10, Math.random() * 8 + 2, 0, 0, Math.PI * 2);
        ctx.fillStyle = Math.random() < 0.5 ? 'rgba(255, 255, 255, 0.32)' : 'rgba(120, 53, 15, 0.35)';
        ctx.fill();
      }
      // The Great Red Spot
      ctx.beginPath(); ctx.ellipse(680, 310, 52, 32, -0.12, 0, Math.PI * 2);
      ctx.fillStyle = '#b91c1c'; ctx.fill();
      ctx.beginPath(); ctx.ellipse(680, 310, 38, 22, -0.12, 0, Math.PI * 2);
      ctx.fillStyle = '#ef4444'; ctx.fill();
      return new THREE.CanvasTexture(c);
    }

    function createSaturnRingTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 64;
      const ctx = c.getContext('2d');
      ctx.clearRect(0, 0, 512, 64);
      for (let x = 0; x < 512; x++) {
        const norm = x / 512;
        let alpha = 0.85;
        if (norm > 0.58 && norm < 0.66) alpha = 0.05; // Cassini Division!
        else if (norm > 0.88 && norm < 0.91) alpha = 0.15; // Encke gap
        const cVal = 190 + Math.sin(norm * 45) * 55;
        ctx.fillStyle = `rgba(${cVal}, ${cVal * 0.9}, ${cVal * 0.72}, ${alpha})`;
        ctx.fillRect(x, 0, 1, 64);
      }
      return new THREE.CanvasTexture(c);
    }

    function createUranusTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createLinearGradient(0, 0, 0, 256);
      grad.addColorStop(0.0, '#a5f3fc'); grad.addColorStop(0.5, '#67e8f9'); grad.addColorStop(1.0, '#22d3ee');
      ctx.fillStyle = grad; ctx.fillRect(0, 0, 512, 256);
      for (let y = 0; y < 256; y += 4) {
        ctx.fillStyle = `rgba(255, 255, 255, ${0.08 + Math.sin(y * 0.15) * 0.05})`;
        ctx.fillRect(0, y, 512, 2);
      }
      return new THREE.CanvasTexture(c);
    }

    function createNeptuneTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createLinearGradient(0, 0, 0, 256);
      grad.addColorStop(0.0, '#1e3a8a'); grad.addColorStop(0.5, '#2563eb'); grad.addColorStop(1.0, '#1d4ed8');
      ctx.fillStyle = grad; ctx.fillRect(0, 0, 512, 256);
      // High-altitude white methane cirrus cloud streaks
      for (let i = 0; i < 40; i++) {
        ctx.beginPath();
        const y = Math.random() * 256;
        ctx.ellipse(Math.random() * 512, y, Math.random() * 70 + 20, Math.random() * 5 + 2, 0.02, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255, 255, 255, 0.45)'; ctx.fill();
      }
      // Great Dark Spot
      ctx.beginPath(); ctx.ellipse(220, 130, 36, 20, -0.1, 0, Math.PI * 2);
      ctx.fillStyle = '#0f172a'; ctx.fill();
      return new THREE.CanvasTexture(c);
    }

    function createPlutoTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      ctx.fillStyle = '#7c2d12'; ctx.fillRect(0, 0, 512, 256);
      for (let i = 0; i < 600; i++) {
        const x = Math.random() * 512, y = Math.random() * 256;
        ctx.beginPath(); ctx.arc(x, y, Math.random() * 12 + 3, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(120, 53, 15, 0.4)'; ctx.fill();
      }
      // Tombaugh Regio (The Nitrogen Ice Heart)
      ctx.fillStyle = '#fef08a';
      ctx.beginPath(); ctx.ellipse(230, 130, 42, 35, 0.25, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.ellipse(270, 130, 38, 32, -0.25, 0, Math.PI * 2); ctx.fill();
      return new THREE.CanvasTexture(c);
    }

    function createBlackHoleAccretionTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 64;
      const ctx = c.getContext('2d');
      for (let x = 0; x < 512; x++) {
        const norm = x / 512;
        const dopplerShift = 0.5 + 0.5 * Math.sin(norm * Math.PI * 2);
        const r = Math.floor(255 * (0.8 + 0.2 * dopplerShift));
        const g = Math.floor(140 * dopplerShift);
        const b = Math.floor(30 * (1 - dopplerShift));
        const a = Math.sin(norm * Math.PI) * 0.92;
        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${a})`;
        ctx.fillRect(x, 0, 1, 64);
      }
      return new THREE.CanvasTexture(c);
    }

    // ==============================================================
    // --- OMNIDIRECTIONAL 3D CELESTIAL REALMS & MODELS ---
    // Spanning thousands of units in all 3D directions (+X, -X, +Y, -Y, +Z, -Z)
    // ==============================================================

    // --- 1. THE SUN (SOLAR CENTER ANCHOR) ---
    const sunTexture = createSunTexture();
    const sunGeo = new THREE.SphereGeometry(45, 64, 64);
    const sunMat = new THREE.MeshBasicMaterial({ map: sunTexture, color: 0xffffff });
    const sunMesh = new THREE.Mesh(sunGeo, sunMat);
    sunMesh.position.set(0, 0, -350);
    cosmosScene.add(sunMesh);

    // Inner fiery corona
    const sunCoronaGeo = new THREE.SphereGeometry(49.5, 48, 48);
    const sunCoronaMat = new THREE.MeshBasicMaterial({
      color: 0xffaa22, transparent: true, opacity: 0.45,
      blending: THREE.AdditiveBlending, side: THREE.BackSide
    });
    const sunCorona = new THREE.Mesh(sunCoronaGeo, sunCoronaMat);
    sunMesh.add(sunCorona);

    // Solar Prominence Arcs (Magnetic Loop Flares)
    const sunProminences = [];
    const promMat = new THREE.MeshBasicMaterial({
      color: 0xff4500, transparent: true, opacity: 0.85, blending: THREE.AdditiveBlending
    });
    for (let p = 0; p < 4; p++) {
      const promGeo = new THREE.TorusGeometry(12, 1.4, 12, 36, Math.PI);
      const promMesh = new THREE.Mesh(promGeo, promMat);
      promMesh.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, Math.random() * Math.PI);
      promMesh.position.set((Math.random() - 0.5) * 35, (Math.random() - 0.5) * 35, (Math.random() - 0.5) * 35);
      sunMesh.add(promMesh);
      sunProminences.push(promMesh);
    }

    // Dynamic Solar Illumination
    const sunPointLight = new THREE.PointLight(0xfff5e6, 4.2, 5500, 0.35);
    sunPointLight.position.set(0, 0, -350);
    cosmosScene.add(sunPointLight);

    // --- 2. MERCURY (SUN-SCORCHED IRON WORLD) ---
    const mercuryTex = createMercuryTexture();
    const mercuryGeo = new THREE.SphereGeometry(5.2, 40, 40);
    const mercuryMat = new THREE.MeshStandardMaterial({ map: mercuryTex, roughness: 0.95, metalness: 0.1 });
    const mercuryMesh = new THREE.Mesh(mercuryGeo, mercuryMat);
    mercuryMesh.position.set(55, 14, -305);
    cosmosScene.add(mercuryMesh);

    // --- 3. VENUS (TOXIC GREENHOUSE WORLD) ---
    const venusTex = createVenusTexture();
    const venusGeo = new THREE.SphereGeometry(13.2, 48, 48);
    const venusMat = new THREE.MeshStandardMaterial({ map: venusTex, roughness: 0.65 });
    const venusMesh = new THREE.Mesh(venusGeo, venusMat);
    venusMesh.position.set(115, -28, -250);
    cosmosScene.add(venusMesh);

    const venusAtmosGeo = new THREE.SphereGeometry(13.9, 32, 32);
    const venusAtmosMat = new THREE.MeshBasicMaterial({
      color: 0xfacc15, transparent: true, opacity: 0.28, blending: THREE.AdditiveBlending, side: THREE.BackSide
    });
    venusMesh.add(new THREE.Mesh(venusAtmosGeo, venusAtmosMat));

    // --- 4. EARTH & THE MOON ---
    const earthTexture = createEarthTexture();
    const earthCloudsTexture = createEarthCloudsTexture();
    const earthGeo = new THREE.SphereGeometry(14, 48, 48);
    const earthMat = new THREE.MeshStandardMaterial({ map: earthTexture, roughness: 0.65, metalness: 0.1 });
    const earthMesh = new THREE.Mesh(earthGeo, earthMat);
    earthMesh.position.set(180, 20, -120);
    cosmosScene.add(earthMesh);

    const cloudsGeo = new THREE.SphereGeometry(14.3, 48, 48);
    const cloudsMat = new THREE.MeshStandardMaterial({
      map: earthCloudsTexture, transparent: true, opacity: 0.72,
      blending: THREE.NormalBlending, roughness: 1.0
    });
    const earthClouds = new THREE.Mesh(cloudsGeo, cloudsMat);
    earthMesh.add(earthClouds);

    const atmosGeo = new THREE.SphereGeometry(14.8, 32, 32);
    const atmosMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8, transparent: true, opacity: 0.22,
      blending: THREE.AdditiveBlending, side: THREE.BackSide
    });
    earthMesh.add(new THREE.Mesh(atmosGeo, atmosMat));

    // The Moon
    const moonGeo = new THREE.SphereGeometry(3.6, 32, 32);
    const moonMat = new THREE.MeshStandardMaterial({ color: 0xa8a29e, roughness: 0.92 });
    const moonMesh = new THREE.Mesh(moonGeo, moonMat);
    moonMesh.position.set(215, 26, -120);
    cosmosScene.add(moonMesh);

    // --- 5. MARS & ITS MOONS (PHOBOS & DEIMOS) ---
    const marsTex = createMarsTexture();
    const marsGeo = new THREE.SphereGeometry(8.5, 48, 48);
    const marsMat = new THREE.MeshStandardMaterial({ map: marsTex, roughness: 0.88, metalness: 0.05 });
    const marsMesh = new THREE.Mesh(marsGeo, marsMat);
    marsMesh.position.set(290, -35, -220);
    cosmosScene.add(marsMesh);

    // Phobos & Deimos irregular asteroid moons
    const phobosGeo = new THREE.IcosahedronGeometry(1.4, 1);
    const phobosMat = new THREE.MeshStandardMaterial({ color: 0x78716c, roughness: 0.9 });
    const marsPhobos = new THREE.Mesh(phobosGeo, phobosMat);
    cosmosScene.add(marsPhobos);

    const deimosGeo = new THREE.IcosahedronGeometry(0.9, 1);
    const deimosMat = new THREE.MeshStandardMaterial({ color: 0x57534e, roughness: 0.9 });
    const marsDeimos = new THREE.Mesh(deimosGeo, deimosMat);
    cosmosScene.add(marsDeimos);

    // --- 6. MAIN ASTEROID BELT (TOROIDAL RING OF 2,200 ASTEROIDS) ---
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
    cosmosScene.add(asteroidBeltPoints);

    // --- 7. JUPITER & THE 4 GALILEAN MOONS ---
    const jupiterTexture = createJupiterTexture();
    const jupiterGeo = new THREE.SphereGeometry(32, 64, 64);
    const jupiterMat = new THREE.MeshStandardMaterial({ map: jupiterTexture, roughness: 0.75, metalness: 0.05 });
    const jupiterMesh = new THREE.Mesh(jupiterGeo, jupiterMat);
    jupiterMesh.position.set(-340, 60, -420);
    cosmosScene.add(jupiterMesh);

    // 4 Galilean Moons (Io, Europa, Ganymede, Callisto)
    const moonIo = new THREE.Mesh(new THREE.SphereGeometry(2.8, 24, 24), new THREE.MeshStandardMaterial({ color: 0xfacc15, roughness: 0.85 }));
    const moonEuropa = new THREE.Mesh(new THREE.SphereGeometry(2.4, 24, 24), new THREE.MeshStandardMaterial({ color: 0xe0f2fe, roughness: 0.45 }));
    const moonGanymede = new THREE.Mesh(new THREE.SphereGeometry(4.2, 24, 24), new THREE.MeshStandardMaterial({ color: 0xa8a29e, roughness: 0.9 }));
    const moonCallisto = new THREE.Mesh(new THREE.SphereGeometry(3.8, 24, 24), new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.95 }));
    cosmosScene.add(moonIo); cosmosScene.add(moonEuropa); cosmosScene.add(moonGanymede); cosmosScene.add(moonCallisto);

    // --- 8. SATURN, MAGNIFICENT RINGS & MOONS ---
    const saturnGeo = new THREE.SphereGeometry(24, 64, 64);
    const saturnMat = new THREE.MeshStandardMaterial({ color: 0xfde68a, roughness: 0.72, metalness: 0.08 });
    const saturnMesh = new THREE.Mesh(saturnGeo, saturnMat);
    saturnMesh.position.set(-240, -50, -220);
    saturnMesh.rotation.z = 0.46; // 26.7 deg axial tilt
    cosmosScene.add(saturnMesh);

    // Saturn Ring System
    const ringTex = createSaturnRingTexture();
    const saturnRingGeo = new THREE.RingGeometry(30, 58, 96);
    const ringPos = saturnRingGeo.attributes.position;
    const ringUv = saturnRingGeo.attributes.uv;
    for (let i = 0; i < ringPos.count; i++) {
      const vx = ringPos.getX(i), vy = ringPos.getY(i);
      const r = Math.sqrt(vx * vx + vy * vy);
      ringUv.setXY(i, (r - 30) / (58 - 30), 0.5);
    }
    const saturnRingMat = new THREE.MeshStandardMaterial({
      map: ringTex, side: THREE.DoubleSide, transparent: true, roughness: 0.65, metalness: 0.1
    });
    const saturnRing = new THREE.Mesh(saturnRingGeo, saturnRingMat);
    saturnRing.rotation.x = Math.PI / 2;
    saturnMesh.add(saturnRing);

    // Titan (Dense atmosphere) & Enceladus (Ice geysers)
    const moonTitan = new THREE.Mesh(new THREE.SphereGeometry(3.6, 24, 24), new THREE.MeshStandardMaterial({ color: 0xf97316, roughness: 0.7 }));
    const moonEnceladus = new THREE.Mesh(new THREE.SphereGeometry(1.6, 16, 16), new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.2 }));
    cosmosScene.add(moonTitan); cosmosScene.add(moonEnceladus);

    // --- 9. URANUS & VERTICAL RINGS ---
    const uranusTex = createUranusTexture();
    const uranusGeo = new THREE.SphereGeometry(18, 48, 48);
    const uranusMat = new THREE.MeshStandardMaterial({ map: uranusTex, roughness: 0.65 });
    const uranusMesh = new THREE.Mesh(uranusGeo, uranusMat);
    uranusMesh.position.set(-160, 260, 320);
    uranusMesh.rotation.x = Math.PI * 0.54; // Severe 98 deg axial tilt (rolling on its side!)
    cosmosScene.add(uranusMesh);

    // Thin vertical dark charcoal rings
    const uranusRingGeo = new THREE.RingGeometry(24, 34, 64);
    const uranusRingMat = new THREE.MeshBasicMaterial({
      color: 0x67e8f9, side: THREE.DoubleSide, transparent: true, opacity: 0.45
    });
    const uranusRing = new THREE.Mesh(uranusRingGeo, uranusRingMat);
    uranusRing.rotation.y = Math.PI / 2;
    uranusMesh.add(uranusRing);

    const moonMiranda = new THREE.Mesh(new THREE.SphereGeometry(1.8, 16, 16), new THREE.MeshStandardMaterial({ color: 0xd4d4d8, roughness: 0.9 }));
    cosmosScene.add(moonMiranda);

    // --- 10. NEPTUNE & TRITON ---
    const neptuneTex = createNeptuneTexture();
    const neptuneGeo = new THREE.SphereGeometry(17, 48, 48);
    const neptuneMat = new THREE.MeshStandardMaterial({ map: neptuneTex, roughness: 0.6 });
    const neptuneMesh = new THREE.Mesh(neptuneGeo, neptuneMat);
    neptuneMesh.position.set(360, -220, 380);
    cosmosScene.add(neptuneMesh);

    const moonTriton = new THREE.Mesh(new THREE.SphereGeometry(2.8, 24, 24), new THREE.MeshStandardMaterial({ color: 0xfbcfe8, roughness: 0.85 }));
    cosmosScene.add(moonTriton);

    // --- 11. PLUTO & CHARON BINARY DWARF SYSTEM ---
    const plutoTex = createPlutoTexture();
    const plutoGeo = new THREE.SphereGeometry(4.2, 32, 32);
    const plutoMat = new THREE.MeshStandardMaterial({ map: plutoTex, roughness: 0.9 });
    const plutoMesh = new THREE.Mesh(plutoGeo, plutoMat);
    plutoMesh.position.set(580, 160, 520);
    cosmosScene.add(plutoMesh);

    const charonGeo = new THREE.SphereGeometry(2.2, 24, 24);
    const charonMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.95 });
    const charonMesh = new THREE.Mesh(charonGeo, charonMat);
    charonMesh.position.set(594, 164, 520);
    cosmosScene.add(charonMesh);

    // --- 12. HALLEY'S COMET (INTERPLANETARY WANDERER) ---
    const cometGroup = new THREE.Group();
    cometGroup.position.set(-220, 340, -180);
    cosmosScene.add(cometGroup);

    // Irregular icy nucleus
    const cometNucleus = new THREE.Mesh(new THREE.IcosahedronGeometry(2.6, 2), new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.95 }));
    cometGroup.add(cometNucleus);

    // Glowing cyan spherical coma
    const comaMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8, transparent: true, opacity: 0.45, blending: THREE.AdditiveBlending
    });
    cometGroup.add(new THREE.Mesh(new THREE.SphereGeometry(6.5, 24, 24), comaMat));

    // Ion Gas Tail (Electric Blue Straight Column pointing away from Sun)
    const ionTailGeo = new THREE.CylinderGeometry(0.5, 9, 130, 24, 1, true);
    const ionTailMat = new THREE.MeshBasicMaterial({
      color: 0x0ea5e9, transparent: true, opacity: 0.42, blending: THREE.AdditiveBlending, side: THREE.DoubleSide
    });
    const cometIonTail = new THREE.Mesh(ionTailGeo, ionTailMat);
    cometIonTail.position.set(-30, 45, 45);
    cometIonTail.rotation.z = Math.PI / 3;
    cometGroup.add(cometIonTail);

    // Curved Dust Tail
    const dustTailGeo = new THREE.CylinderGeometry(1.0, 18, 110, 24, 1, true);
    const dustTailMat = new THREE.MeshBasicMaterial({
      color: 0xfef08a, transparent: true, opacity: 0.25, blending: THREE.AdditiveBlending, side: THREE.DoubleSide
    });
    const cometDustTail = new THREE.Mesh(dustTailGeo, dustTailMat);
    cometDustTail.position.set(-25, 40, 30);
    cometDustTail.rotation.z = Math.PI / 2.6;
    cometGroup.add(cometDustTail);

    // --- 13. JAMES WEBB SPACE TELESCOPE (JWST) ---
    const jwstGroup = new THREE.Group();
    jwstGroup.position.set(195, 24, -95);
    cosmosScene.add(jwstGroup);

    // Golden 18-Hex Mirror Array
    const mirrorGeo = new THREE.CylinderGeometry(2.8, 2.8, 0.2, 6);
    const mirrorMat = new THREE.MeshStandardMaterial({ color: 0xfacc15, metalness: 0.95, roughness: 0.08 });
    const jwstMirror = new THREE.Mesh(mirrorGeo, mirrorMat);
    jwstMirror.rotation.x = Math.PI / 2;
    jwstGroup.add(jwstMirror);

    // 5-Layer Silver Sunshield Membrane
    const shieldGeo = new THREE.PlaneGeometry(8, 5);
    const shieldMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.85, roughness: 0.3, side: THREE.DoubleSide });
    const jwstShield = new THREE.Mesh(shieldGeo, shieldMat);
    jwstShield.position.set(0, -1.8, -0.6);
    jwstGroup.add(jwstShield);

    // --- 14. VOYAGER 1 INTERSTELLAR PROBE ---
    const voyagerGroup = new THREE.Group();
    voyagerGroup.position.set(240, 380, -520);
    cosmosScene.add(voyagerGroup);

    // High-Gain White Parabolic Dish Antenna
    const dishGeo = new THREE.SphereGeometry(3.2, 24, 12, 0, Math.PI * 2, 0, Math.PI * 0.4);
    const dishMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.4, side: THREE.DoubleSide });
    const voyagerDish = new THREE.Mesh(dishGeo, dishMat);
    voyagerDish.rotation.x = Math.PI / 2;
    voyagerGroup.add(voyagerDish);

    // Golden Record mounted on the bus
    const recordGeo = new THREE.CylinderGeometry(0.9, 0.9, 0.08, 24);
    const recordMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.95, roughness: 0.1 });
    const goldenRecord = new THREE.Mesh(recordGeo, recordMat);
    goldenRecord.position.set(1.2, -1.2, 0);
    voyagerGroup.add(goldenRecord);

    // RTG Power Boom
    const rtgGeo = new THREE.CylinderGeometry(0.2, 0.2, 8, 8);
    const rtgMat = new THREE.MeshStandardMaterial({ color: 0x475569, metalness: 0.8 });
    const rtgBoom = new THREE.Mesh(rtgGeo, rtgMat);
    rtgBoom.position.set(-4, -1, 0);
    rtgBoom.rotation.z = Math.PI / 2;
    voyagerGroup.add(rtgBoom);

    // --- 15. PILLARS OF CREATION (EAGLE NEBULA M16) ---
    const eagleGroup = new THREE.Group();
    eagleGroup.position.set(-720, 420, -820);
    cosmosScene.add(eagleGroup);

    const pillarCount = 6000;
    const pillarGeo = new THREE.BufferGeometry();
    const pillarPositions = new Float32Array(pillarCount * 3);
    const pillarColors = new Float32Array(pillarCount * 3);

    const colPillarEmerald = new THREE.Color(0x10b981);
    const colPillarAmber = new THREE.Color(0xf59e0b);
    const colPillarCyan = new THREE.Color(0x06b6d4);
    const tmpPil = new THREE.Color();

    for (let i = 0; i < pillarCount; i++) {
      const idx = i * 3;
      // 3 towering columns of interstellar dust
      const colIdx = Math.floor(Math.random() * 3);
      const baseX = (colIdx - 1) * 38;
      const height = (colIdx === 0 ? 120 : (colIdx === 1 ? 85 : 55)) * Math.random();
      const spread = (1.0 - height / 130) * 18 + 4;

      const px = baseX + (Math.random() - 0.5) * spread;
      const py = height;
      const pz = (Math.random() - 0.5) * spread;

      pillarPositions[idx] = px;
      pillarPositions[idx + 1] = py;
      pillarPositions[idx + 2] = pz;

      const tColor = colIdx === 0 ? colPillarEmerald : (colIdx === 1 ? colPillarAmber : colPillarCyan);
      tmpPil.copy(tColor).lerp(new THREE.Color(0xffffff), Math.random() * 0.2);
      pillarColors[idx] = tmpPil.r;
      pillarColors[idx + 1] = tmpPil.g;
      pillarColors[idx + 2] = tmpPil.b;
    }
    pillarGeo.setAttribute('position', new THREE.BufferAttribute(pillarPositions, 3));
    pillarGeo.setAttribute('color', new THREE.BufferAttribute(pillarColors, 3));
    const pillarMat = new THREE.PointsMaterial({
      size: 3.5, vertexColors: true, transparent: true, opacity: 0.65, blending: THREE.AdditiveBlending
    });
    eagleGroup.add(new THREE.Points(pillarGeo, pillarMat));

    // --- 16. CRAB NEBULA SUPERNOVA REMNANT (M1) ---
    const crabGroup = new THREE.Group();
    crabGroup.position.set(780, -360, -680);
    cosmosScene.add(crabGroup);

    const crabCount = 5000;
    const crabGeo = new THREE.BufferGeometry();
    const crabPos = new Float32Array(crabCount * 3);
    const crabCol = new Float32Array(crabCount * 3);

    const colCrabCrimson = new THREE.Color(0xef4444);
    const colCrabViolet = new THREE.Color(0x8b5cf6);
    const colCrabCyan = new THREE.Color(0x06b6d4);

    for (let i = 0; i < crabCount; i++) {
      const idx = i * 3;
      const u = Math.random(), v = Math.random();
      const theta = u * 2.0 * Math.PI, phi = Math.acos(2.0 * v - 1.0);
      const r = 25 + Math.random() * 45;

      // Filamentary turbulence
      const fx = Math.sin(phi) * Math.cos(theta) * r * (1 + Math.sin(theta * 6) * 0.25);
      const fy = Math.sin(phi) * Math.sin(theta) * r * (1 + Math.cos(phi * 6) * 0.25);
      const fz = Math.cos(phi) * r;

      crabPos[idx] = fx; crabPos[idx + 1] = fy; crabPos[idx + 2] = fz;

      const pick = Math.random();
      const col = pick < 0.4 ? colCrabCrimson : (pick < 0.75 ? colCrabViolet : colCrabCyan);
      crabCol[idx] = col.r; crabCol[idx + 1] = col.g; crabCol[idx + 2] = col.b;
    }
    crabGeo.setAttribute('position', new THREE.BufferAttribute(crabPos, 3));
    crabGeo.setAttribute('color', new THREE.BufferAttribute(crabCol, 3));
    crabGroup.add(new THREE.Points(crabGeo, new THREE.PointsMaterial({
      size: 2.8, vertexColors: true, transparent: true, opacity: 0.72, blending: THREE.AdditiveBlending
    })));

    // Central pulsar core
    const crabPulsar = new THREE.Mesh(new THREE.SphereGeometry(2.4, 16, 16), new THREE.MeshBasicMaterial({ color: 0xffffff }));
    crabGroup.add(crabPulsar);

    // --- 17. PULSAR / MAGNETAR PSR B1919+21 ---
    const pulsarGroup = new THREE.Group();
    pulsarGroup.position.set(-520, -450, 480);
    cosmosScene.add(pulsarGroup);

    // Neutron Star Core
    const neutronCore = new THREE.Mesh(new THREE.SphereGeometry(3.8, 32, 32), new THREE.MeshBasicMaterial({ color: 0x93c5fd }));
    pulsarGroup.add(neutronCore);

    // Dual Relativistic Synchrotron Beams (Light Cones)
    const beamGeo = new THREE.ConeGeometry(14, 240, 24, 1, true);
    const beamMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8, transparent: true, opacity: 0.55, side: THREE.DoubleSide, blending: THREE.AdditiveBlending
    });

    const northBeam = new THREE.Mesh(beamGeo, beamMat);
    northBeam.position.y = 120;
    pulsarGroup.add(northBeam);

    const southBeam = new THREE.Mesh(beamGeo, beamMat);
    southBeam.position.y = -120;
    southBeam.rotation.x = Math.PI;
    pulsarGroup.add(southBeam);

    // --- 18. GARGANTUA SUPERMASSIVE BLACK HOLE & POLAR RELATIVISTIC JETS ---
    const blackHoleGroup = new THREE.Group();
    blackHoleGroup.position.set(0, -150, -1100);
    cosmosScene.add(blackHoleGroup);

    // Pitch-black Event Horizon
    const eventHorizonGeo = new THREE.SphereGeometry(38, 48, 48);
    const eventHorizonMat = new THREE.MeshBasicMaterial({ color: 0x000000 });
    const eventHorizonMesh = new THREE.Mesh(eventHorizonGeo, eventHorizonMat);
    blackHoleGroup.add(eventHorizonMesh);

    // Relativistic Doppler-beamed Accretion Disk
    const accretionTexture = createBlackHoleAccretionTexture();
    const accretionGeo = new THREE.RingGeometry(44, 98, 96);
    const accretionMat = new THREE.MeshBasicMaterial({
      map: accretionTexture, side: THREE.DoubleSide, transparent: true,
      blending: THREE.AdditiveBlending, depthWrite: false
    });
    const blackHoleAccretion = new THREE.Mesh(accretionGeo, accretionMat);
    blackHoleAccretion.rotation.x = Math.PI / 2.3;
    blackHoleGroup.add(blackHoleAccretion);

    // Gravitational Lensing Photon Ring
    const lensingGeo = new THREE.RingGeometry(39, 78, 96);
    const lensingMat = new THREE.MeshBasicMaterial({
      color: 0xf59e0b, transparent: true, opacity: 0.45, side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending, depthWrite: false
    });
    const blackHoleLensing = new THREE.Mesh(lensingGeo, lensingMat);
    blackHoleLensing.rotation.y = Math.PI / 4;
    blackHoleGroup.add(blackHoleLensing);

    // Bipolar Relativistic Plasma Jets (shooting 850 units into +Y and -Y!)
    const jetGeo = new THREE.CylinderGeometry(2.5, 42, 850, 32, 1, true);
    const jetMat = new THREE.MeshBasicMaterial({
      color: 0x818cf8, transparent: true, opacity: 0.55, blending: THREE.AdditiveBlending, side: THREE.DoubleSide
    });
    const northJet = new THREE.Mesh(jetGeo, jetMat);
    northJet.position.y = 440;
    blackHoleGroup.add(northJet);

    const southJet = new THREE.Mesh(jetGeo, jetMat);
    southJet.position.y = -440;
    blackHoleGroup.add(southJet);

    // --- 19. ANDROMEDA SPIRAL GALAXY (M31) ---
    const andromedaGroup = new THREE.Group();
    andromedaGroup.position.set(920, 680, -1050);
    andromedaGroup.rotation.x = 0.85;
    andromedaGroup.rotation.z = -0.45;
    cosmosScene.add(andromedaGroup);

    const galaxyStarsCount = 12000;
    const galaxyGeo = new THREE.BufferGeometry();
    const galaxyPositions = new Float32Array(galaxyStarsCount * 3);
    const galaxyColors = new Float32Array(galaxyStarsCount * 3);

    const cGalCore = new THREE.Color(0xfef08a);
    const cGalArm = new THREE.Color(0x38bdf8);
    const cGalDust = new THREE.Color(0xf43f5e);

    for (let i = 0; i < galaxyStarsCount; i++) {
      const idx = i * 3;
      const armIndex = i % 2;
      const distFromCenter = Math.pow(Math.random(), 2.2) * 220;
      const angle = (distFromCenter * 0.055) + (armIndex * Math.PI);
      const scatter = (Math.random() - 0.5) * (12 + distFromCenter * 0.15);
      const vertical = (Math.random() - 0.5) * (8 * (1.0 - distFromCenter / 230));

      const gx = Math.cos(angle) * distFromCenter + (Math.random() - 0.5) * scatter;
      const gy = vertical;
      const gz = Math.sin(angle) * distFromCenter + (Math.random() - 0.5) * scatter;

      galaxyPositions[idx] = gx;
      galaxyPositions[idx + 1] = gy;
      galaxyPositions[idx + 2] = gz;

      const normDist = distFromCenter / 220;
      const col = normDist < 0.25 ? cGalCore : (Math.random() < 0.85 ? cGalArm : cGalDust);
      galaxyColors[idx] = col.r;
      galaxyColors[idx + 1] = col.g;
      galaxyColors[idx + 2] = col.b;
    }
    galaxyGeo.setAttribute('position', new THREE.BufferAttribute(galaxyPositions, 3));
    galaxyGeo.setAttribute('color', new THREE.BufferAttribute(galaxyColors, 3));
    andromedaGroup.add(new THREE.Points(galaxyGeo, new THREE.PointsMaterial({
      size: 2.2, vertexColors: true, transparent: true, opacity: 0.75, blending: THREE.AdditiveBlending
    })));

    // --- 20. VISHVARUPA: THE ASTRAL GOD & SUDARSHANA CHAKRA ---
    const astralGodGroup = new THREE.Group();
    astralGodGroup.position.set(260, 280, -780);
    cosmosScene.add(astralGodGroup);

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
        col = (h > 0.75) ? cCyan : cGold;
      } else if (part < 0.32) {
        // Serene Face, Tilak & Divine Halo
        const angle = Math.random() * Math.PI * 2;
        const rad = Math.random() * 8.5;
        x = Math.cos(angle) * rad;
        y = 35 + Math.sin(angle) * rad * 1.25;
        z = (Math.random() - 0.5) * 4.5;
        col = (Math.abs(x) < 0.8 && y > 35 && y < 45) ? cGold : ((Math.random() < 0.5) ? cWhite : cCyan);
      } else if (part < 0.52) {
        // Divine Torso, Sacred Thread & Royal Necklaces
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
          x = 10 + t * 24;
          y = 26 + t * 44;
          z = (Math.random() - 0.5) * 4.5;
        } else {
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
      size: 1.8, vertexColors: true, transparent: true, opacity: 0.88,
      blending: THREE.AdditiveBlending, depthWrite: false
    });
    const astralGodPoints = new THREE.Points(astralGeo, astralMat);
    astralGodGroup.add(astralGodPoints);

    // The Sudarshana Chakra
    const sudarshanaGroup = new THREE.Group();
    sudarshanaGroup.position.set(24.5, 74, 0);
    astralGodGroup.add(sudarshanaGroup);

    const chakraOuterGeo = new THREE.RingGeometry(12, 17.5, 72);
    const chakraOuterMat = new THREE.MeshBasicMaterial({
      color: 0xf59e0b, transparent: true, opacity: 0.82, side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending, depthWrite: false
    });
    const sudarshanaOuterDisc = new THREE.Mesh(chakraOuterGeo, chakraOuterMat);
    sudarshanaGroup.add(sudarshanaOuterDisc);

    const chakraInnerGeo = new THREE.RingGeometry(2.5, 12, 36);
    const chakraInnerMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8, transparent: true, opacity: 0.75, side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending, depthWrite: false
    });
    const sudarshanaSpokes = new THREE.Mesh(chakraInnerGeo, chakraInnerMat);
    sudarshanaGroup.add(sudarshanaSpokes);

    const chakraCoreGeo = new THREE.SphereGeometry(2.8, 24, 24);
    const chakraCoreMat = new THREE.MeshBasicMaterial({ color: 0xffffff, blending: THREE.AdditiveBlending });
    sudarshanaGroup.add(new THREE.Mesh(chakraCoreGeo, chakraCoreMat));

    const chakraLight = new THREE.PointLight(0xfef08a, 4.5, 550, 0.4);
    sudarshanaGroup.add(chakraLight);

    const godAuraGeo = new THREE.SphereGeometry(58, 32, 32);
    const godAuraMat = new THREE.MeshBasicMaterial({
      color: 0x1e3a8a, transparent: true, opacity: 0.14,
      blending: THREE.AdditiveBlending, side: THREE.BackSide, depthWrite: false
    });
    astralGodGroup.add(new THREE.Mesh(godAuraGeo, godAuraMat));
'''

# Find boundaries to replace the old celestial definitions
idx_start = text.find('function createSunTexture()')
idx_end = text.find('// ==============================================================\n    // --- CINEMATIC 3D CLENCHED FIST POINT CLOUD GENERATOR ---')

if idx_start != -1 and idx_end != -1:
    text = text[:idx_start] + mega_celestial_code.strip() + "\n\n    " + text[idx_end:]
    print("Replaced celestial models block with 20+ cosmic entities!")
else:
    print(f"Error finding markers: start={idx_start}, end={idx_end}")

# 3. Update the celestialDestinations array
new_destinations = '''const celestialDestinations = [
      { name: "THE SUN", pos: new THREE.Vector3(0, 0, -350), r: 45 },
      { name: "MERCURY", pos: new THREE.Vector3(55, 14, -305), r: 5.2 },
      { name: "VENUS", pos: new THREE.Vector3(115, -28, -250), r: 13.2 },
      { name: "EARTH & MOON", pos: new THREE.Vector3(180, 20, -120), r: 14 },
      { name: "MARS & MOONS", pos: new THREE.Vector3(290, -35, -220), r: 8.5 },
      { name: "MAIN ASTEROID BELT", pos: new THREE.Vector3(380, 0, -350), r: 40 },
      { name: "JUPITER & 4 MOONS", pos: new THREE.Vector3(-340, 60, -420), r: 32 },
      { name: "SATURN & RINGS", pos: new THREE.Vector3(-240, -50, -220), r: 24 },
      { name: "URANUS & RINGS", pos: new THREE.Vector3(-160, 260, 320), r: 18 },
      { name: "NEPTUNE & TRITON", pos: new THREE.Vector3(360, -220, 380), r: 17 },
      { name: "PLUTO & CHARON", pos: new THREE.Vector3(580, 160, 520), r: 4.2 },
      { name: "HALLEY\\'S COMET", pos: new THREE.Vector3(-220, 340, -180), r: 12 },
      { name: "JWST TELESCOPE", pos: new THREE.Vector3(195, 24, -95), r: 6 },
      { name: "VOYAGER 1 PROBE", pos: new THREE.Vector3(240, 380, -520), r: 6 },
      { name: "PILLARS OF CREATION", pos: new THREE.Vector3(-720, 420, -820), r: 110 },
      { name: "CRAB NEBULA SUPERNOVA", pos: new THREE.Vector3(780, -360, -680), r: 80 },
      { name: "PULSAR PSR B1919+21", pos: new THREE.Vector3(-520, -450, 480), r: 40 },
      { name: "GARGANTUA BLACK HOLE", pos: new THREE.Vector3(0, -150, -1100), r: 45 },
      { name: "ANDROMEDA GALAXY", pos: new THREE.Vector3(920, 680, -1050), r: 220 },
      { name: "VISHVARUPA ASTRAL GOD", pos: new THREE.Vector3(260, 280, -780), r: 50 }
    ];'''

dest_start = text.find('const celestialDestinations = [')
dest_end = text.find('];', dest_start) + 2

if dest_start != -1 and dest_end != -1:
    text = text[:dest_start] + new_destinations + text[dest_end:]
    print("Updated celestialDestinations with all 20 celestial marvels!")

# 4. Update the continuous rotations loop in animate()
new_rotations = '''// ================================================================
      // CELESTIAL BODY CONTINUOUS ROTATION & ORBITAL DYNAMICS
      // ================================================================
      // 1. The Sun & Solar Prominence loop dynamics
      sunMesh.rotation.y = elapsed * 0.08;
      sunCorona.scale.setScalar(1.0 + Math.sin(elapsed * 2.5) * 0.06);
      sunCoronaMat.opacity = 0.35 + Math.sin(elapsed * 3.8) * 0.15;
      for (let p = 0; p < sunProminences.length; p++) {
        sunProminences[p].rotation.z += delta * (0.3 + p * 0.1);
      }

      // 2. Mercury rotation
      mercuryMesh.rotation.y = elapsed * 0.06;

      // 3. Venus rotation & atmospheric drift
      venusMesh.rotation.y = -elapsed * 0.04; // Retrograde spin!

      // 4. Earth & Moon orbit
      earthMesh.rotation.y = elapsed * 0.22;
      earthClouds.rotation.y = elapsed * 0.08;
      const moonOrbitRadius = 36;
      const moonAngle = elapsed * 0.35;
      moonMesh.position.set(
        earthMesh.position.x + Math.cos(moonAngle) * moonOrbitRadius,
        earthMesh.position.y + 2,
        earthMesh.position.z + Math.sin(moonAngle) * moonOrbitRadius
      );
      moonMesh.rotation.y = elapsed * 0.1;

      // 5. Mars & Phobos/Deimos orbits
      marsMesh.rotation.y = elapsed * 0.19;
      marsPhobos.position.set(
        marsMesh.position.x + Math.cos(elapsed * 1.2) * 14,
        marsMesh.position.y + Math.sin(elapsed * 1.2) * 2,
        marsMesh.position.z + Math.sin(elapsed * 1.2) * 14
      );
      marsDeimos.position.set(
        marsMesh.position.x + Math.cos(elapsed * 0.6) * 22,
        marsMesh.position.y - Math.sin(elapsed * 0.6) * 3,
        marsMesh.position.z + Math.sin(elapsed * 0.6) * 22
      );

      // 6. Main Asteroid Belt continuous orbital revolution
      const beltPosArray = beltGeo.attributes.position.array;
      for (let i = 0; i < beltCount; i++) {
        const idx = i * 3;
        beltAngles[i] += delta * beltSpeeds[i] * 0.25;
        beltPosArray[idx] = Math.cos(beltAngles[i]) * beltRadii[i];
        beltPosArray[idx + 2] = -350 + Math.sin(beltAngles[i]) * beltRadii[i];
      }
      beltGeo.attributes.position.needsUpdate = true;

      // 7. Jupiter & 4 Galilean Moons
      jupiterMesh.rotation.y = elapsed * 0.15;
      const jx = jupiterMesh.position.x, jy = jupiterMesh.position.y, jz = jupiterMesh.position.z;
      moonIo.position.set(jx + Math.cos(elapsed * 1.5) * 46, jy + Math.sin(elapsed * 1.5) * 2, jz + Math.sin(elapsed * 1.5) * 46);
      moonEuropa.position.set(jx + Math.cos(elapsed * 1.0) * 62, jy - Math.sin(elapsed * 1.0) * 4, jz + Math.sin(elapsed * 1.0) * 62);
      moonGanymede.position.set(jx + Math.cos(elapsed * 0.65) * 80, jy + Math.sin(elapsed * 0.65) * 5, jz + Math.sin(elapsed * 0.65) * 80);
      moonCallisto.position.set(jx + Math.cos(elapsed * 0.42) * 102, jy - Math.sin(elapsed * 0.42) * 6, jz + Math.sin(elapsed * 0.42) * 102);

      // 8. Saturn & Rings & Moons
      saturnMesh.rotation.y = elapsed * 0.12;
      const sx = saturnMesh.position.x, sy = saturnMesh.position.y, sz = saturnMesh.position.z;
      moonTitan.position.set(sx + Math.cos(elapsed * 0.55) * 72, sy + Math.sin(elapsed * 0.55) * 8, sz + Math.sin(elapsed * 0.55) * 72);
      moonEnceladus.position.set(sx + Math.cos(elapsed * 1.3) * 42, sy - Math.sin(elapsed * 1.3) * 4, sz + Math.sin(elapsed * 1.3) * 42);

      // 9. Uranus & Miranda
      uranusMesh.rotation.z = elapsed * 0.14;
      const ux = uranusMesh.position.x, uy = uranusMesh.position.y, uz = uranusMesh.position.z;
      moonMiranda.position.set(ux, uy + Math.cos(elapsed * 0.8) * 44, uz + Math.sin(elapsed * 0.8) * 44);

      // 10. Neptune & Retrograde Triton
      neptuneMesh.rotation.y = elapsed * 0.16;
      const nx = neptuneMesh.position.x, ny = neptuneMesh.position.y, nz = neptuneMesh.position.z;
      moonTriton.position.set(nx + Math.cos(-elapsed * 0.7) * 52, ny + Math.sin(-elapsed * 0.7) * 12, nz + Math.sin(-elapsed * 0.7) * 52);

      // 11. Pluto & Charon binary orbit
      plutoMesh.rotation.y = elapsed * 0.08;
      charonMesh.position.set(
        plutoMesh.position.x + Math.cos(elapsed * 0.45) * 18,
        plutoMesh.position.y + Math.sin(elapsed * 0.45) * 3,
        plutoMesh.position.z + Math.sin(elapsed * 0.45) * 18
      );

      // 12. Halley's Comet ripple & trajectory drift
      cometGroup.position.x = -220 + Math.sin(elapsed * 0.08) * 25;
      cometGroup.position.z = -180 + Math.cos(elapsed * 0.08) * 35;
      cometIonTail.scale.set(1.0 + Math.sin(elapsed * 4.0) * 0.06, 1.0, 1.0 + Math.cos(elapsed * 4.0) * 0.06);

      // 13. JWST & Voyager drifts
      jwstGroup.rotation.y = elapsed * 0.05;
      voyagerGroup.rotation.x = elapsed * 0.03;
      voyagerGroup.rotation.y = elapsed * 0.04;

      // 14. Pulsar light beams sweeping across space!
      pulsarGroup.rotation.y = elapsed * 8.5; // Rapid neutron star spin
      pulsarGroup.rotation.z = Math.sin(elapsed * 0.8) * 0.45;

      // 15. Supernova Remnant & Pillars shimmering
      crabGroup.rotation.y = elapsed * 0.015;
      eagleGroup.rotation.y = Math.sin(elapsed * 0.05) * 0.02;

      // 16. Black Hole: Accretion disk spin + lensing halo shimmer + polar jet pulse
      blackHoleAccretion.rotation.z = elapsed * 0.65;
      blackHoleLensing.rotation.z = -elapsed * 0.3;
      blackHoleLensing.scale.setScalar(1.0 + Math.sin(elapsed * 1.8) * 0.08);
      northJet.scale.x = 1.0 + Math.sin(elapsed * 6.0) * 0.12;
      northJet.scale.z = 1.0 + Math.cos(elapsed * 6.0) * 0.12;
      southJet.scale.x = northJet.scale.x;
      southJet.scale.z = northJet.scale.z;

      // 17. Andromeda Spiral Galaxy rotation
      andromedaGroup.rotation.y = elapsed * 0.005;

      // 18. VISHVARUPA ASTRAL GOD: Ethereal cosmic breathing & Sudarshana Chakra spin
      astralGodGroup.rotation.y = Math.sin(elapsed * 0.12) * 0.08;
      astralGodGroup.position.y = 280 + Math.sin(elapsed * 0.4) * 4.5;
      sudarshanaGroup.rotation.z = elapsed * 3.5;
      sudarshanaOuterDisc.rotation.z = elapsed * -1.2;
      chakraOuterMat.opacity = 0.68 + Math.sin(elapsed * 6.0) * 0.18;
      chakraInnerMat.opacity = 0.55 + Math.sin(elapsed * 8.0) * 0.22;
      chakraLight.intensity = 4.0 + Math.sin(elapsed * 7.5) * 2.5;

      const aPos = astralGeo.attributes.position.array;
      for (let i = 0; i < astralCount; i += 6) {
        const idx = i * 3;
        aPos[idx]     += Math.sin(elapsed * 2.0 + i * 0.1) * 0.015;
        aPos[idx + 1] += Math.cos(elapsed * 1.5 + i * 0.08) * 0.012;
      }
      astralGeo.attributes.position.needsUpdate = true;'''

rot_start = text.find('// ================================================================\n      // CELESTIAL BODY CONTINUOUS ROTATION & ORBITAL DYNAMICS')
rot_end = text.find('// ----------------------------------------------------------------\n      // UPDATE BOTH FISTS', rot_start)

if rot_start != -1 and rot_end != -1:
    text = text[:rot_start] + new_rotations + "\n\n      " + text[rot_end:]
    print("Replaced animate() rotations with all 20 celestial systems!")
else:
    print(f"Error finding rotation markers: start={rot_start}, end={rot_end}")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("build_full_cosmos.py completed successfully!")
