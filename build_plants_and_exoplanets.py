import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect where celestial bodies end in index.html
target_after_astral = "astralGodGroup.add(new THREE.Mesh(godAuraGeo, godAuraMat));"

new_exoplanets_and_plants = '''
    // ==============================================================
    // --- 21. EXOPLANETS, ALIEN PLANTS & EXPANDED DEEP COSMOS ---
    // Habitable alien worlds with 3D bioluminescent vegetation!
    // ==============================================================

    // --- ALIEN TEXTURE GENERATORS ---
    function createKeplerTexture() {
      const c = document.createElement('canvas'); c.width = 1024; c.height = 512;
      const ctx = c.getContext('2d');
      ctx.fillStyle = '#064e3b'; ctx.fillRect(0, 0, 1024, 512); // Deep emerald alien oceans
      // Alien continents with purple, cyan and neon-green flora biomes
      const biomes = ['#831843', '#047857', '#4c1d95', '#0e7490', '#065f46'];
      for (let i = 0; i < 400; i++) {
        const x = Math.random() * 1024, y = Math.random() * 512;
        ctx.beginPath();
        ctx.arc(x, y, Math.random() * 38 + 12, 0, Math.PI * 2);
        ctx.fillStyle = biomes[Math.floor(Math.random() * biomes.length)];
        ctx.fill();
      }
      return new THREE.CanvasTexture(c);
    }

    function createProximaBTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      const grad = ctx.createLinearGradient(0, 0, 512, 0);
      grad.addColorStop(0.0, '#451a03'); grad.addColorStop(0.45, '#78350f');
      grad.addColorStop(0.55, '#065f46'); grad.addColorStop(1.0, '#0f172a'); // Tidally locked day/night!
      ctx.fillStyle = grad; ctx.fillRect(0, 0, 512, 256);
      return new THREE.CanvasTexture(c);
    }

    function createWaspTexture() {
      const c = document.createElement('canvas'); c.width = 512; c.height = 256;
      const ctx = c.getContext('2d');
      ctx.fillStyle = '#1c1917'; ctx.fillRect(0, 0, 512, 256);
      // Molten lava fissures
      for (let i = 0; i < 45; i++) {
        ctx.beginPath();
        const y = Math.random() * 256;
        ctx.ellipse(256, y, 260, Math.random() * 8 + 2, 0.1, 0, Math.PI * 2);
        ctx.fillStyle = Math.random() < 0.5 ? 'rgba(239, 68, 68, 0.8)' : 'rgba(249, 115, 22, 0.85)';
        ctx.fill();
      }
      return new THREE.CanvasTexture(c);
    }

    // --- PROCEDURAL 3D BIOLUMINESCENT ALIEN PLANTS & TREES ---
    // Creates living alien flora that can be explored on planetary surfaces!
    function createAlienPlantBiome(planetMesh, planetRadius, plantCount = 70) {
      const floraGroup = new THREE.Group();
      planetMesh.add(floraGroup);

      const trunkMat = new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.85 });
      const bioCyanMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, blending: THREE.AdditiveBlending });
      const bioVioletMat = new THREE.MeshBasicMaterial({ color: 0xc084fc, blending: THREE.AdditiveBlending });
      const bioEmeraldMat = new THREE.MeshBasicMaterial({ color: 0x34d399, blending: THREE.AdditiveBlending });

      for (let i = 0; i < plantCount; i++) {
        const plant = new THREE.Group();

        // Distribute around the planet's sphere surface
        const u = Math.random(), v = Math.random();
        const theta = u * 2.0 * Math.PI, phi = Math.acos(2.0 * v - 1.0);
        const normal = new THREE.Vector3(
          Math.sin(phi) * Math.cos(theta),
          Math.sin(phi) * Math.sin(theta),
          Math.cos(phi)
        );

        plant.position.copy(normal).multiplyScalar(planetRadius);
        plant.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), normal);

        const plantType = Math.random();
        if (plantType < 0.35) {
          // 1. Giant Bioluminescent Spore Tree
          const trunkGeo = new THREE.CylinderGeometry(0.12, 0.35, 2.8, 6);
          const trunk = new THREE.Mesh(trunkGeo, trunkMat);
          trunk.position.y = 1.4;
          plant.add(trunk);

          const canopyGeo = new THREE.SphereGeometry(1.2, 12, 12);
          const canopy = new THREE.Mesh(canopyGeo, Math.random() < 0.5 ? bioCyanMat : bioVioletMat);
          canopy.position.y = 2.8;
          canopy.scale.set(1.4, 0.7, 1.4);
          plant.add(canopy);
        } else if (plantType < 0.70) {
          // 2. Phosphorescent Alien Mushroom
          const stalkGeo = new THREE.CylinderGeometry(0.18, 0.28, 1.8, 6);
          const stalk = new THREE.Mesh(stalkGeo, trunkMat);
          stalk.position.y = 0.9;
          plant.add(stalk);

          const capGeo = new THREE.ConeGeometry(1.1, 0.8, 12);
          const cap = new THREE.Mesh(capGeo, bioEmeraldMat);
          cap.position.y = 1.8;
          plant.add(cap);
        } else {
          // 3. Glowing Spiral Tendril Plant
          const tendrilGeo = new THREE.TorusGeometry(0.8, 0.15, 8, 16, Math.PI * 1.5);
          const tendril = new THREE.Mesh(tendrilGeo, bioCyanMat);
          tendril.position.y = 0.8;
          tendril.rotation.x = Math.PI / 2;
          plant.add(tendril);
        }

        floraGroup.add(plant);
      }
      return floraGroup;
    }

    // --- KEPLER-452B (EARTH'S SUPER-EARTH COUSIN WITH ALIEN FLORA) ---
    const keplerTex = createKeplerTexture();
    const keplerGeo = new THREE.SphereGeometry(22, 54, 54);
    const keplerMat = new THREE.MeshStandardMaterial({ map: keplerTex, roughness: 0.65, metalness: 0.08 });
    const keplerMesh = new THREE.Mesh(keplerGeo, keplerMat);
    keplerMesh.position.set(1400, 520, -980);
    cosmosScene.add(keplerMesh);

    // Glowing emerald atmosphere shell
    const keplerAtmos = new THREE.Mesh(
      new THREE.SphereGeometry(22.9, 32, 32),
      new THREE.MeshBasicMaterial({ color: 0x10b981, transparent: true, opacity: 0.24, blending: THREE.AdditiveBlending, side: THREE.BackSide })
    );
    keplerMesh.add(keplerAtmos);

    // Populate Kepler-452b with lush 3D alien plants & trees!
    const keplerFlora = createAlienPlantBiome(keplerMesh, 22, 120);

    // Also populate Earth with plant groves
    const earthFlora = createAlienPlantBiome(earthMesh, 14, 80);

    // --- PROXIMA CENTAURI B (TIDALLY LOCKED NEAREST EXOPLANET) ---
    const proximaTex = createProximaBTexture();
    const proximaMesh = new THREE.Mesh(
      new THREE.SphereGeometry(15, 48, 48),
      new THREE.MeshStandardMaterial({ map: proximaTex, roughness: 0.85 })
    );
    proximaMesh.position.set(-1200, -350, 720);
    cosmosScene.add(proximaMesh);

    // --- TRAPPIST-1E (WATERWORLD OCEAN EXOPLANET) ---
    const trappistMesh = new THREE.Mesh(
      new THREE.SphereGeometry(13.5, 48, 48),
      new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.25, metalness: 0.35 })
    );
    trappistMesh.position.set(-920, 680, -1250);
    cosmosScene.add(trappistMesh);

    // --- WASP-12B (THE TIDALLY DISTORTED MOLTEN EGG) ---
    const waspTex = createWaspTexture();
    const waspGeo = new THREE.SphereGeometry(26, 48, 48);
    // Stretch into an egg shape!
    waspGeo.scale(1.5, 0.9, 0.9);
    const waspMesh = new THREE.Mesh(waspGeo, new THREE.MeshStandardMaterial({ map: waspTex, roughness: 0.5 }));
    waspMesh.position.set(1700, -620, 1500);
    cosmosScene.add(waspMesh);

    // --- CERES (DWARF PLANET & OCCATOR CRATER) ---
    const ceresMesh = new THREE.Mesh(
      new THREE.SphereGeometry(4.8, 32, 32),
      new THREE.MeshStandardMaterial({ color: 0x52525b, roughness: 0.92 })
    );
    ceresMesh.position.set(390, 18, -310);
    cosmosScene.add(ceresMesh);

    // Bright reflective salt deposits of Occator Crater
    const occatorSpot = new THREE.Mesh(
      new THREE.SphereGeometry(0.8, 12, 12),
      new THREE.MeshBasicMaterial({ color: 0xffffff, blending: THREE.AdditiveBlending })
    );
    occatorSpot.position.set(0, 0, 4.7);
    ceresMesh.add(occatorSpot);

    // --- ERIS & DYSNOMIA (EXTREME ICY DWARF MONARCH) ---
    const erisMesh = new THREE.Mesh(
      new THREE.SphereGeometry(4.5, 32, 32),
      new THREE.MeshStandardMaterial({ color: 0xf1f5f9, roughness: 0.35 })
    );
    erisMesh.position.set(2600, 920, -1900);
    cosmosScene.add(erisMesh);

    // --- HAUMEA (FAST-SPINNING FOOTBALL DWARF & RING) ---
    const haumeaGeo = new THREE.SphereGeometry(5.2, 32, 32);
    haumeaGeo.scale(1.8, 0.9, 0.9); // Elongated ellipsoid!
    const haumeaMesh = new THREE.Mesh(haumeaGeo, new THREE.MeshStandardMaterial({ color: 0xd4d4d8, roughness: 0.4 }));
    haumeaMesh.position.set(-2100, -820, -1700);
    cosmosScene.add(haumeaMesh);

    // Haumea's thin ring
    const haumeaRing = new THREE.Mesh(
      new THREE.RingGeometry(8, 10.5, 48),
      new THREE.MeshBasicMaterial({ color: 0x94a3b8, side: THREE.DoubleSide, transparent: true, opacity: 0.5 })
    );
    haumeaRing.rotation.x = Math.PI / 2.2;
    haumeaMesh.add(haumeaRing);

    // --- MAKEMAKE (RED METHANE ICE DWARF) ---
    const makemakeMesh = new THREE.Mesh(
      new THREE.SphereGeometry(4.0, 32, 32),
      new THREE.MeshStandardMaterial({ color: 0x9a3412, roughness: 0.75 })
    );
    makemakeMesh.position.set(1950, -1050, -1300);
    cosmosScene.add(makemakeMesh);

    // --- COSMIC WEB SUPERCLUSTER FILAMENTS (Spanning 60,000 units!) ---
    const webCount = 10000;
    const webGeo = new THREE.BufferGeometry();
    const webPositions = new Float32Array(webCount * 3);
    const webColors = new Float32Array(webCount * 3);
    const cDeepWeb = new THREE.Color(0x3b82f6);
    const cVioletWeb = new THREE.Color(0xa855f7);

    for (let i = 0; i < webCount; i++) {
      const idx = i * 3;
      const angle = Math.random() * Math.PI * 2;
      const phi = (Math.random() - 0.5) * Math.PI;
      const dist = 3500 + Math.random() * 26000;

      webPositions[idx]     = Math.cos(phi) * Math.cos(angle) * dist;
      webPositions[idx + 1] = Math.sin(phi) * dist;
      webPositions[idx + 2] = Math.cos(phi) * Math.sin(angle) * dist;

      const col = Math.random() < 0.6 ? cDeepWeb : cVioletWeb;
      webColors[idx] = col.r * 0.7;
      webColors[idx + 1] = col.g * 0.7;
      webColors[idx + 2] = col.b * 0.7;
    }
    webGeo.setAttribute('position', new THREE.BufferAttribute(webPositions, 3));
    webGeo.setAttribute('color', new THREE.BufferAttribute(webColors, 3));
    const cosmicWebPoints = new THREE.Points(webGeo, new THREE.PointsMaterial({
      size: 2.8, vertexColors: true, transparent: true, opacity: 0.45, blending: THREE.AdditiveBlending
    }));
    cosmosScene.add(cosmicWebPoints);
'''

# Insert exoplanets and plants
if target_after_astral in text:
    text = text.replace(target_after_astral, target_after_astral + "\n" + new_exoplanets_and_plants)
    print("Added Exoplanets, Alien Plants Biomes, and Cosmic Web!")
else:
    print("Warning: target_after_astral not found!")

# 4. Update celestialDestinations array to include Exoplanets & Alien Worlds
mega_destinations = '''const celestialDestinations = [
      { name: "THE SUN", pos: new THREE.Vector3(0, 0, -350), r: 45, type: "G2V YELLOW DWARF STAR", atmos: "H, He Plasma Corona", bio: "Solar Convection", mesh: sunMesh },
      { name: "MERCURY", pos: new THREE.Vector3(55, 14, -305), r: 5.2, type: "SCORCHED IRON WORLD", atmos: "Trace Exosphere", bio: "None", mesh: mercuryMesh },
      { name: "VENUS", pos: new THREE.Vector3(115, -28, -250), r: 13.2, type: "GREENHOUSE PLANET", atmos: "96% CO2, H2SO4 Clouds", bio: "Supercritical Fluid", mesh: venusMesh },
      { name: "EARTH & MOON", pos: new THREE.Vector3(180, 20, -120), r: 14, type: "TERRESTRIAL HABITABLE", atmos: "78% N2, 21% O2, H2O", bio: "Rich Flora & Ecosystems", mesh: earthMesh },
      { name: "MARS & MOONS", pos: new THREE.Vector3(290, -35, -220), r: 8.5, type: "RED DESERT WORLD", atmos: "95% CO2 (Thin)", bio: "Fossilized Microbes", mesh: marsMesh },
      { name: "CERES (ASTEROID QUEEN)", pos: new THREE.Vector3(390, 18, -310), r: 4.8, type: "DWARF PLANET", atmos: "Trace Water Vapor", bio: "Subsurface Ocean Salts", mesh: ceresMesh },
      { name: "MAIN ASTEROID BELT", pos: new THREE.Vector3(380, 0, -350), r: 40, type: "TOROIDAL DEBRIS RING", atmos: "Hard Vacuum", bio: "Prebiotic Carbonaceous", mesh: asteroidBeltPoints },
      { name: "JUPITER & 4 MOONS", pos: new THREE.Vector3(-340, 60, -420), r: 32, type: "GAS GIANT LEVIATHAN", atmos: "H2, He, Ammonia Storms", bio: "Atmospheric Layers", mesh: jupiterMesh },
      { name: "SATURN & RINGS", pos: new THREE.Vector3(-240, -50, -220), r: 24, type: "RINGED GAS GIANT", atmos: "Hydrogen, Methane Haze", bio: "Enceladus Ice Plumes", mesh: saturnMesh },
      { name: "URANUS & RINGS", pos: new THREE.Vector3(-160, 260, 320), r: 18, type: "TILTED ICE GIANT", atmos: "Hydrogen, Methane Ice", bio: "Diamond Rains", mesh: uranusMesh },
      { name: "NEPTUNE & TRITON", pos: new THREE.Vector3(360, -220, 380), r: 17, type: "STORM ICE GIANT", atmos: "Methane, Hydrogen Storms", bio: "Triton Cryovolcanism", mesh: neptuneMesh },
      { name: "PLUTO & CHARON", pos: new THREE.Vector3(580, 160, 520), r: 4.2, type: "BINARY DWARF SYSTEM", atmos: "Nitrogen Ice Sublimation", bio: "Tombaugh Glacier Heart", mesh: plutoMesh },
      { name: "KEPLER-452B (ALIEN FLORA)", pos: new THREE.Vector3(1400, 520, -980), r: 22, type: "SUPER-EARTH EXOPLANET", atmos: "N2, O2, Water Vapor", bio: "Bioluminescent Alien Forests", mesh: keplerMesh },
      { name: "PROXIMA CENTAURI B", pos: new THREE.Vector3(-1200, -350, 720), r: 15, type: "TIDALLY LOCKED EXOPLANET", atmos: "Carbonate Atmosphere", bio: "Twilight Zone Vegetation", mesh: proximaMesh },
      { name: "TRAPPIST-1E WATERWORLD", pos: new THREE.Vector3(-920, 680, -1250), r: 13.5, type: "OCEAN EXOPLANET", atmos: "Superdense Steam & Oxygen", bio: "Abyssal Marine Life", mesh: trappistMesh },
      { name: "WASP-12B (MOLTEN EGG)", pos: new THREE.Vector3(1700, -620, 1500), r: 26, type: "TIDAL CARBON EGG", atmos: "Vaporized Silicates & Iron", bio: "Molten Magma Surface", mesh: waspMesh },
      { name: "ERIS & DYSNOMIA", pos: new THREE.Vector3(2600, 920, -1900), r: 4.5, type: "DISTANT ICE MONARCH", atmos: "Frozen Methane Crust", bio: "Extreme Deep Space", mesh: erisMesh },
      { name: "HAUMEA (FOOTBALL DWARF)", pos: new THREE.Vector3(-2100, -820, -1700), r: 5.2, type: "FAST-SPINNING ELLIPSOID", atmos: "Pure Crystalline Ice", bio: "4-Hour High Speed Spin", mesh: haumeaMesh },
      { name: "MAKEMAKE (RED ICE)", pos: new THREE.Vector3(1950, -1050, -1300), r: 4.0, type: "RED THOLIN DWARF", atmos: "Trace Methane Frost", bio: "Kuiper Belt Outpost", mesh: makemakeMesh },
      { name: "HALLEY\\'S COMET", pos: new THREE.Vector3(-220, 340, -180), r: 12, type: "PERIODIC COMET", atmos: "Cyanogen, Water Gas Coma", bio: "Interplanetary Wanderer", mesh: cometGroup },
      { name: "JWST TELESCOPE", pos: new THREE.Vector3(195, 24, -95), r: 6, type: "SPACE OBSERVATORY", atmos: "Lagrange L2 Vacuum", bio: "Deep Field Infrared Vision", mesh: jwstGroup },
      { name: "VOYAGER 1 PROBE", pos: new THREE.Vector3(240, 380, -520), r: 6, type: "INTERSTELLAR PROBE", atmos: "Interstellar Medium", bio: "The Golden Record", mesh: voyagerGroup },
      { name: "PILLARS OF CREATION", pos: new THREE.Vector3(-720, 420, -820), r: 110, type: "STAR NURSERY NEBULA", atmos: "Cool Molecular Hydrogen", bio: "Proto-stellar Embryos", mesh: eagleGroup },
      { name: "CRAB NEBULA SUPERNOVA", pos: new THREE.Vector3(780, -360, -680), r: 80, type: "SUPERNOVA REMNANT", atmos: "Ionized Oxygen & Hydrogen", bio: "Relativistic Synchrotron Core", mesh: crabGroup },
      { name: "PULSAR PSR B1919+21", pos: new THREE.Vector3(-520, -450, 480), r: 40, type: "SPINNING NEUTRON STAR", atmos: "Relativistic Beams", bio: "Hyperdense Nuclear Matter", mesh: pulsarGroup },
      { name: "GARGANTUA BLACK HOLE", pos: new THREE.Vector3(0, -150, -1100), r: 45, type: "SUPERMASSIVE SINGULARITY", atmos: "Relativistic Accretion Plasma", bio: "Gravitational Light Lensing", mesh: blackHoleGroup },
      { name: "ANDROMEDA GALAXY", pos: new THREE.Vector3(920, 680, -1050), r: 220, type: "BARRED SPIRAL GALAXY", atmos: "Trillion Star Systems", bio: "Galactic Supercluster", mesh: andromedaGroup },
      { name: "VISHVARUPA ASTRAL GOD", pos: new THREE.Vector3(260, 280, -780), r: 50, type: "COSMIC STARDUST DEITY", atmos: "Divine Sudarshana Radiance", bio: "Supreme Celestial Entity", mesh: astralGodGroup }
    ];'''

dest_start = text.find('const celestialDestinations = [')
dest_end = text.find('];', dest_start) + 2

if dest_start != -1 and dest_end != -1:
    text = text[:dest_start] + mega_destinations + text[dest_end:]
    print("Updated celestialDestinations with 28 cosmic targets!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Step B complete.")
