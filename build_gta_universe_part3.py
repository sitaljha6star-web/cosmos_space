import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# ------------------------------------------------------------------------------
# 3. INTERSTELLAR WORMHOLE & LIVING OPEN-WORLD EARTH SYSTEM
# ------------------------------------------------------------------------------

wormhole_and_gta_code = '''
    // ==============================================================
    // --- 29. THE INTERSTELLAR WORMHOLE (DIMENSIONAL WARP GATE) ---
    // A spherical gravitational lensing wormhole connecting space to Earth!
    // ==============================================================
    const wormholeGroup = new THREE.Group();
    wormholeGroup.position.set(450, 180, -520);
    cosmosScene.add(wormholeGroup);

    // 1. Gravitational Lensing Spherical Throat
    const wormholeThroatGeo = new THREE.SphereGeometry(36, 48, 48);
    const wormholeThroatMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8, transparent: true, opacity: 0.65, blending: THREE.AdditiveBlending, side: THREE.DoubleSide
    });
    const wormholeThroat = new THREE.Mesh(wormholeThroatGeo, wormholeThroatMat);
    wormholeGroup.add(wormholeThroat);

    // 2. Relativistic Outer Ring Distortion
    const wormholeRingGeo = new THREE.RingGeometry(38, 72, 64);
    const wormholeRingMat = new THREE.MeshBasicMaterial({
      color: 0xf59e0b, transparent: true, opacity: 0.75, side: THREE.DoubleSide, blending: THREE.AdditiveBlending
    });
    const wormholeRing = new THREE.Mesh(wormholeRingGeo, wormholeRingMat);
    wormholeRing.rotation.x = Math.PI / 2.5;
    wormholeGroup.add(wormholeRing);

    // 3. Swirling Hyperspace Infalling Particle Vortex
    const vortexCount = 2000;
    const vortexGeo = new THREE.BufferGeometry();
    const vortexPositions = new Float32Array(vortexCount * 3);
    const vortexColors = new Float32Array(vortexCount * 3);
    const vortexRadii = new Float32Array(vortexCount);
    const vortexAngles = new Float32Array(vortexCount);

    const cVortexCyan = new THREE.Color(0x38bdf8);
    const cVortexGold = new THREE.Color(0xfbbf24);

    for (let i = 0; i < vortexCount; i++) {
      const idx = i * 3;
      const r = 38 + Math.random() * 55;
      const a = Math.random() * Math.PI * 2;
      vortexRadii[i] = r;
      vortexAngles[i] = a;

      vortexPositions[idx]     = Math.cos(a) * r;
      vortexPositions[idx + 1] = (Math.random() - 0.5) * 14;
      vortexPositions[idx + 2] = Math.sin(a) * r;

      const col = Math.random() < 0.6 ? cVortexCyan : cVortexGold;
      vortexColors[idx]     = col.r;
      vortexColors[idx + 1] = col.g;
      vortexColors[idx + 2] = col.b;
    }
    vortexGeo.setAttribute('position', new THREE.BufferAttribute(vortexPositions, 3));
    vortexGeo.setAttribute('color', new THREE.BufferAttribute(vortexColors, 3));
    const wormholeVortex = new THREE.Points(vortexGeo, new THREE.PointsMaterial({
      size: 2.4, vertexColors: true, transparent: true, opacity: 0.85, blending: THREE.AdditiveBlending
    }));
    wormholeGroup.add(wormholeVortex);

    // ==============================================================
    // --- 30. LIVING OPEN-WORLD EARTH ENVIRONMENT (GTA-SCALE WORLD) ---
    // Ground landscape with Skyscrapers, Monuments, Jungle, Animals & NPCs!
    // ==============================================================
    const earthGroundWorld = new THREE.Group();
    // Positioned seamlessly on the surface coordinates of Earth (or explored when descending!)
    earthGroundWorld.position.set(180, 20, -120);
    cosmosScene.add(earthGroundWorld);

    // --- TERRAIN & OCEAN WATER ---
    const terrainGeo = new THREE.PlaneGeometry(320, 320, 48, 48);
    const terrainPos = terrainGeo.attributes.position;
    for (let i = 0; i < terrainPos.count; i++) {
      const vx = terrainPos.getX(i), vy = terrainPos.getY(i);
      // Gentle rolling hills and coastal drop-off
      const hill = Math.sin(vx * 0.04) * Math.cos(vy * 0.04) * 4.5 + Math.sin(vx * 0.08) * 2.0;
      terrainPos.setZ(i, hill);
    }
    terrainGeo.computeVertexNormals();

    const terrainMat = new THREE.MeshStandardMaterial({
      color: 0x2e7d32, roughness: 0.85, metalness: 0.05
    });
    const groundTerrain = new THREE.Mesh(terrainGeo, terrainMat);
    groundTerrain.rotation.x = -Math.PI / 2;
    groundTerrain.position.y = 14.2; // Right on Earth surface!
    earthGroundWorld.add(groundTerrain);

    // Coastal Ocean Water Plane
    const oceanGeo = new THREE.PlaneGeometry(160, 320);
    const oceanMat = new THREE.MeshStandardMaterial({
      color: 0x0284c7, roughness: 0.15, metalness: 0.45, transparent: true, opacity: 0.88
    });
    const oceanWater = new THREE.Mesh(oceanGeo, oceanMat);
    oceanWater.rotation.x = -Math.PI / 2;
    oceanWater.position.set(80, 14.0, 0);
    earthGroundWorld.add(oceanWater);

    // --- CITY SKYLINE & SKYSCRAPERS ---
    const cityGroup = new THREE.Group();
    cityGroup.position.set(-45, 14.5, -30);
    earthGroundWorld.add(cityGroup);

    const bldColors = [0x1e293b, 0x0f172a, 0x334155, 0x0284c7, 0x38bdf8];
    const cityBuildings = [];

    // Create 24 Skyscraper models of varied architectural heights
    for (let bx = 0; bx < 6; bx++) {
      for (let bz = 0; bz < 4; bz++) {
        const height = 18 + Math.random() * 38;
        const width = 6 + Math.random() * 5;
        const depth = 6 + Math.random() * 5;

        const bldGeo = new THREE.BoxGeometry(width, height, depth);
        const col = bldColors[Math.floor(Math.random() * bldColors.length)];
        const bldMat = new THREE.MeshStandardMaterial({
          color: col, roughness: 0.25, metalness: 0.75
        });
        const building = new THREE.Mesh(bldGeo, bldMat);
        building.position.set((bx - 2.5) * 14 + (Math.random() - 0.5) * 3, height / 2, (bz - 1.5) * 14 + (Math.random() - 0.5) * 3);
        cityGroup.add(building);
        cityBuildings.push(building);

        // Rooftop antenna spire with blinking warning light
        if (height > 30) {
          const spireGeo = new THREE.CylinderGeometry(0.1, 0.1, 6, 8);
          const spire = new THREE.Mesh(spireGeo, new THREE.MeshBasicMaterial({ color: 0xef4444 }));
          spire.position.set(building.position.x, building.position.y + height / 2 + 3, building.position.z);
          cityGroup.add(spire);
        }
      }
    }

    // Paved Asphalt City Roads
    const roadMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.9 });
    for (let r = -2; r <= 2; r++) {
      const roadH = new THREE.Mesh(new THREE.PlaneGeometry(90, 4), roadMat);
      roadH.rotation.x = -Math.PI / 2;
      roadH.position.set(0, 0.05, r * 14);
      cityGroup.add(roadH);

      const roadV = new THREE.Mesh(new THREE.PlaneGeometry(4, 90), roadMat);
      roadV.rotation.x = -Math.PI / 2;
      roadV.position.set(r * 18, 0.05, 0);
      cityGroup.add(roadV);
    }

    // --- FAMOUS WORLD MONUMENTS ---
    const monumentGroup = new THREE.Group();
    monumentGroup.position.set(35, 14.5, -45);
    earthGroundWorld.add(monumentGroup);

    // 1. The Great Pyramid of Giza (Sandstone Stepped Pyramid)
    const pyramidGeo = new THREE.ConeGeometry(18, 14, 4);
    const pyramidMat = new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.95 });
    const pyramid = new THREE.Mesh(pyramidGeo, pyramidMat);
    pyramid.rotation.y = Math.PI / 4;
    pyramid.position.set(-25, 7, 0);
    monumentGroup.add(pyramid);

    // 2. The Eiffel Tower Spire
    const eiffelGroup = new THREE.Group();
    eiffelGroup.position.set(10, 0, -25);
    monumentGroup.add(eiffelGroup);

    const eiffelBaseGeo = new THREE.ConeGeometry(7, 16, 4);
    const eiffelMat = new THREE.MeshStandardMaterial({ color: 0x64748b, metalness: 0.85, roughness: 0.35 });
    const eiffelBase = new THREE.Mesh(eiffelBaseGeo, eiffelMat);
    eiffelBase.position.y = 8;
    eiffelGroup.add(eiffelBase);

    const eiffelSpireGeo = new THREE.CylinderGeometry(0.2, 2.5, 24, 8);
    const eiffelSpire = new THREE.Mesh(eiffelSpireGeo, eiffelMat);
    eiffelSpire.position.y = 26;
    eiffelGroup.add(eiffelSpire);

    // 3. The Taj Mahal (White Marble Grand Dome & 4 Minarets)
    const tajGroup = new THREE.Group();
    tajGroup.position.set(15, 0, 25);
    monumentGroup.add(tajGroup);

    const tajBase = new THREE.Mesh(new THREE.BoxGeometry(16, 6, 16), new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.2 }));
    tajBase.position.y = 3;
    tajGroup.add(tajBase);

    const tajDome = new THREE.Mesh(new THREE.SphereGeometry(4.5, 24, 24), new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.15 }));
    tajDome.position.y = 9.5;
    tajGroup.add(tajDome);

    // 4 Corner Minarets
    const minaretOffsets = [[-8, -8], [8, -8], [-8, 8], [8, 8]];
    minaretOffsets.forEach(mo => {
      const minaret = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.8, 14, 12), new THREE.MeshStandardMaterial({ color: 0xf8fafc }));
      minaret.position.set(mo[0], 7, mo[1]);
      tajGroup.add(minaret);
    });

    // Reflecting Pool
    const pool = new THREE.Mesh(new THREE.PlaneGeometry(8, 28), new THREE.MeshStandardMaterial({ color: 0x06b6d4, roughness: 0.1 }));
    pool.rotation.x = -Math.PI / 2;
    pool.position.set(0, 0.1, 24);
    tajGroup.add(pool);

    // --- JUNGLE & RAINFOREST BIOME (100+ DENSE TREES) ---
    const jungleGroup = new THREE.Group();
    jungleGroup.position.set(-30, 14.5, 45);
    earthGroundWorld.add(jungleGroup);

    const palmTrunkMat = new THREE.MeshStandardMaterial({ color: 0x78350f, roughness: 0.9 });
    const palmLeafMat = new THREE.MeshStandardMaterial({ color: 0x15803d, roughness: 0.65 });
    const pineLeafMat = new THREE.MeshStandardMaterial({ color: 0x064e3b, roughness: 0.7 });

    for (let t = 0; t < 95; t++) {
      const tree = new THREE.Group();
      const tx = (Math.random() - 0.5) * 90;
      const tz = (Math.random() - 0.5) * 90;
      tree.position.set(tx, 0, tz);

      const treeType = Math.random();
      if (treeType < 0.45) {
        // Tropical Palm Tree
        const trunkGeo = new THREE.CylinderGeometry(0.25, 0.5, 7.5, 6);
        const trunk = new THREE.Mesh(trunkGeo, palmTrunkMat);
        trunk.position.y = 3.75;
        trunk.rotation.z = (Math.random() - 0.5) * 0.2;
        tree.add(trunk);

        // Palm Leaf Crown
        for (let l = 0; l < 6; l++) {
          const leafGeo = new THREE.ConeGeometry(0.8, 4.5, 4);
          const leaf = new THREE.Mesh(leafGeo, palmLeafMat);
          leaf.position.y = 7.5;
          leaf.rotation.z = Math.PI / 2.8;
          leaf.rotation.y = (l / 6) * Math.PI * 2;
          tree.add(leaf);
        }
      } else if (treeType < 0.75) {
        // Conical Evergreen Pine
        const trunkGeo = new THREE.CylinderGeometry(0.3, 0.6, 3, 6);
        const trunk = new THREE.Mesh(trunkGeo, palmTrunkMat);
        trunk.position.y = 1.5;
        tree.add(trunk);

        const pineTop = new THREE.Mesh(new THREE.ConeGeometry(2.8, 8, 8), pineLeafMat);
        pineTop.position.y = 6.5;
        tree.add(pineTop);
      } else {
        // Broadleaf Jungle Giant Canopy Tree
        const trunkGeo = new THREE.CylinderGeometry(0.6, 1.0, 5, 8);
        const trunk = new THREE.Mesh(trunkGeo, palmTrunkMat);
        trunk.position.y = 2.5;
        tree.add(trunk);

        const canopy = new THREE.Mesh(new THREE.SphereGeometry(3.5, 12, 12), palmLeafMat);
        canopy.position.y = 6.8;
        canopy.scale.set(1.4, 0.8, 1.4);
        tree.add(canopy);
      }

      jungleGroup.add(tree);
    }

    // --- ANIMATED LIVING ANIMALS ---
    const animalGroup = new THREE.Group();
    animalGroup.position.set(0, 14.5, 0);
    earthGroundWorld.add(animalGroup);

    // 1. Birds Flying in the Sky (Flapping Wings Animation!)
    const birds = [];
    const birdMat = new THREE.MeshBasicMaterial({ color: 0x1e293b, side: THREE.DoubleSide });
    for (let b = 0; b < 12; b++) {
      const bird = new THREE.Group();
      const body = new THREE.Mesh(new THREE.ConeGeometry(0.25, 1.2, 4), birdMat);
      body.rotation.x = Math.PI / 2;
      bird.add(body);

      const wingL = new THREE.Mesh(new THREE.PlaneGeometry(1.2, 0.5), birdMat);
      wingL.position.x = -0.7;
      bird.add(wingL);

      const wingR = new THREE.Mesh(new THREE.PlaneGeometry(1.2, 0.5), birdMat);
      wingR.position.x = 0.7;
      bird.add(wingR);

      bird.position.set((Math.random() - 0.5) * 120, 24 + Math.random() * 18, (Math.random() - 0.5) * 120);
      animalGroup.add(bird);
      birds.push({ group: bird, wingL, wingR, speed: 0.4 + Math.random() * 0.3, angle: Math.random() * Math.PI * 2, radius: 30 + Math.random() * 45 });
    }

    // 2. Deer / Gazelles on the Meadows (Animated Walking Legs!)
    const deerList = [];
    const deerMat = new THREE.MeshStandardMaterial({ color: 0xb45309, roughness: 0.8 });
    for (let d = 0; d < 8; d++) {
      const deer = new THREE.Group();
      // Torso
      const body = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.9, 2.2), deerMat);
      body.position.y = 1.6;
      deer.add(body);

      // Neck & Head
      const head = new THREE.Mesh(new THREE.ConeGeometry(0.4, 1.1, 4), deerMat);
      head.position.set(0, 2.6, 1.1);
      head.rotation.x = Math.PI / 4;
      deer.add(head);

      // 4 Legs
      const legs = [];
      const legOffsets = [[-0.45, 0.8, -0.8], [0.45, 0.8, -0.8], [-0.45, 0.8, 0.8], [0.45, 0.8, 0.8]];
      legOffsets.forEach(lo => {
        const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 1.6, 6), deerMat);
        leg.position.set(lo[0], lo[1], lo[2]);
        deer.add(leg);
        legs.push(leg);
      });

      deer.position.set(-10 + (Math.random() - 0.5) * 45, 0, 15 + (Math.random() - 0.5) * 45);
      animalGroup.add(deer);
      deerList.push({ group: deer, legs, basePos: deer.position.clone(), dir: Math.random() * Math.PI * 2 });
    }

    // 3. African Elephants
    const elephantList = [];
    const eleMat = new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.9 });
    for (let e = 0; e < 4; e++) {
      const elephant = new THREE.Group();
      const body = new THREE.Mesh(new THREE.BoxGeometry(2.8, 2.4, 4.2), eleMat);
      body.position.y = 3.2;
      elephant.add(body);

      const head = new THREE.Mesh(new THREE.SphereGeometry(1.4, 12, 12), eleMat);
      head.position.set(0, 4.0, 2.6);
      elephant.add(head);

      // Trunk
      const trunk = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.5, 2.5, 8), eleMat);
      trunk.position.set(0, 2.8, 3.6);
      trunk.rotation.x = Math.PI / 6;
      elephant.add(trunk);

      elephant.position.set(15 + (Math.random() - 0.5) * 50, 0, 45 + (Math.random() - 0.5) * 40);
      animalGroup.add(elephant);
      elephantList.push(elephant);
    }

    // 4. Leaping Ocean Dolphins
    const dolphins = [];
    const dolphinMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8, roughness: 0.3 });
    for (let dp = 0; dp < 4; dp++) {
      const dolphin = new THREE.Mesh(new THREE.ConeGeometry(0.6, 2.8, 8), dolphinMat);
      dolphin.rotation.x = Math.PI / 2;
      dolphin.position.set(70 + (Math.random() - 0.5) * 40, 0, (Math.random() - 0.5) * 80);
      animalGroup.add(dolphin);
      dolphins.push({ mesh: dolphin, phase: Math.random() * Math.PI * 2 });
    }

    // --- 3D HUMAN NPC PEDESTRIANS (GTA WALKING CROWDS) ---
    const npcList = [];
    const shirtColors = [0xef4444, 0x3b82f6, 0x10b981, 0xfacc15, 0x8b5cf6, 0xf8fafc];
    const pantsMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
    const skinMat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, roughness: 0.6 });

    for (let n = 0; n < 30; n++) {
      const npc = new THREE.Group();

      // Torso / Shirt
      const sCol = shirtColors[Math.floor(Math.random() * shirtColors.length)];
      const torso = new THREE.Mesh(new THREE.BoxGeometry(0.65, 0.85, 0.4), new THREE.MeshStandardMaterial({ color: sCol }));
      torso.position.y = 1.35;
      npc.add(torso);

      // Head
      const head = new THREE.Mesh(new THREE.SphereGeometry(0.24, 12, 12), skinMat);
      head.position.y = 2.05;
      npc.add(head);

      // Legs
      const legL = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.9, 0.25), pantsMat);
      legL.position.set(-0.16, 0.45, 0);
      npc.add(legL);

      const legR = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.9, 0.25), pantsMat);
      legR.position.set(0.16, 0.45, 0);
      npc.add(legR);

      // Arms
      const armL = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.75, 0.2), skinMat);
      armL.position.set(-0.45, 1.3, 0);
      npc.add(armL);

      const armR = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.75, 0.2), skinMat);
      armR.position.set(0.45, 1.3, 0);
      npc.add(armR);

      // Place along city streets & plazas
      const nx = -45 + (Math.random() - 0.5) * 55;
      const nz = -30 + (Math.random() - 0.5) * 55;
      npc.position.set(nx, 0, nz);
      cityGroup.add(npc);

      npcList.push({
        group: npc,
        legL,
        legR,
        armL,
        armR,
        speed: 0.8 + Math.random() * 0.8,
        dir: Math.random() * Math.PI * 2,
        walkCycle: Math.random() * Math.PI * 2
      });
    }
'''

# Find insertion point right before function generateFistPointCloud
idx_fist_marker = text.find('// ==============================================================\n    // --- CINEMATIC 3D CLENCHED FIST POINT CLOUD GENERATOR ---')
if idx_fist_marker != -1:
    text = text[:idx_fist_marker] + wormhole_and_gta_code.strip() + "\n\n    " + text[idx_fist_marker:]
    print("Added Wormhole and Earth Open-World GTA City, Monuments, Jungle, Animals & NPCs!")
else:
    print("Warning: idx_fist_marker not found!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Part 3 complete.")
