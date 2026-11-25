import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect where cycleDestination is defined
idx_cycle = text.find('function cycleDestination() {')
print("cycleDestination found at:", idx_cycle)

new_interactivity_code = '''
    // ==============================================================
    // --- PLANETARY ENTRY, RAYCASTER & HYPERDRIVE WARP SYSTEM ---
    // Click any planet to scan and fly directly into its atmosphere!
    // ==============================================================
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    const planetCardEl = document.getElementById('planet-card');
    const pcTypeEl = document.getElementById('pc-type');
    const pcNameEl = document.getElementById('pc-name');
    const pcSurfaceEl = document.getElementById('pc-surface');
    const pcAtmosEl = document.getElementById('pc-atmos');
    const pcBioEl = document.getElementById('pc-bio');
    const reentryOverlayEl = document.getElementById('reentry-overlay');
    const targetReticleEl = document.getElementById('target-reticle');

    let currentTargetPlanet = celestialDestinations[0];
    let isLandingMode = false;
    let landingProgress = 0.0;
    let landingTargetPos = new THREE.Vector3();

    function updatePlanetCard(dest) {
      currentTargetPlanet = dest;
      if (pcTypeEl) pcTypeEl.textContent = dest.type || "CELESTIAL OBJECT";
      if (pcNameEl) pcNameEl.textContent = dest.name;
      if (pcSurfaceEl) pcSurfaceEl.textContent = `${dest.r} Radii • ${dest.name}`;
      if (pcAtmosEl) pcAtmosEl.textContent = dest.atmos || "Vacuum / Exotic Radiation";
      if (pcBioEl) pcBioEl.textContent = dest.bio || "Inorganic Cosmic Matter";
      if (planetCardEl) planetCardEl.style.opacity = '1';
    }

    // Direct Hyperdrive Warp Jump (instant smooth travel to planet)
    function hyperdriveWarp() {
      if (!currentTargetPlanet) return;
      const approachDistance = Math.max(18, currentTargetPlanet.r * 2.2);
      const camPos = new THREE.Vector3(cameraX, cameraY, cameraZ);
      const dir = new THREE.Vector3().subVectors(camPos, currentTargetPlanet.pos).normalize();
      if (dir.lengthSq() < 0.001) dir.set(0, 0, 1);

      // Set target position just outside the planet's atmosphere
      landingTargetPos.copy(currentTargetPlanet.pos).addScaledVector(dir, approachDistance);
      autoNavTarget.copy(landingTargetPos);
      isAutoNavigating = true;
      autoNavTimer = 4.5;
      isLandingMode = false;

      triggerWarpChime();
      if (blinkNotifyEl) {
        blinkNotifyEl.textContent = `⚡ HYPERDRIVE JUMP: ${currentTargetPlanet.name}`;
        blinkNotifyEl.classList.add('visible');
        setTimeout(() => blinkNotifyEl.classList.remove('visible'), 2400);
      }
    }

    // Atmospheric Entry & Surface Landing (flies right into the planet's atmosphere/surface!)
    function landOnPlanet() {
      if (!currentTargetPlanet) return;
      const surfaceAltitude = currentTargetPlanet.r * 1.08; // Just above the surface!
      const camPos = new THREE.Vector3(cameraX, cameraY, cameraZ);
      const dir = new THREE.Vector3().subVectors(camPos, currentTargetPlanet.pos).normalize();
      if (dir.lengthSq() < 0.001) dir.set(0, 0.4, 0.9).normalize();

      landingTargetPos.copy(currentTargetPlanet.pos).addScaledVector(dir, surfaceAltitude);
      autoNavTarget.copy(landingTargetPos);
      isAutoNavigating = true;
      isLandingMode = true;
      autoNavTimer = 5.0;

      // Re-entry heat burst sound & visual
      triggerWarpChime();
      if (reentryOverlayEl) {
        reentryOverlayEl.style.opacity = '0.85';
        setTimeout(() => { reentryOverlayEl.style.opacity = '0.15'; }, 1800);
      }

      if (blinkNotifyEl) {
        blinkNotifyEl.textContent = `🚀 ENTERING ATMOSPHERE: ${currentTargetPlanet.name}`;
        blinkNotifyEl.classList.add('visible');
        setTimeout(() => blinkNotifyEl.classList.remove('visible'), 3200);
      }
    }

    // Raycast: Click on ANY planet in 3D space to select and inspect it!
    window.addEventListener('pointerdown', (e) => {
      // Ignore clicks on UI buttons
      if (e.target.closest('button') || e.target.closest('.nav-badge') || e.target.closest('.planet-card')) return;

      mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);

      // Collect all interactive celestial objects
      const candidates = [];
      celestialDestinations.forEach(d => {
        if (d.mesh) candidates.push({ dest: d, obj: d.mesh });
      });

      const meshesToCheck = candidates.map(c => c.obj);
      const intersects = raycaster.intersectObjects(meshesToCheck, true);

      if (intersects.length > 0) {
        const hitObj = intersects[0].object;
        // Find matching destination
        let match = candidates.find(c => c.obj === hitObj || c.obj.children.includes(hitObj));
        if (!match) {
          // Check by distance to hit point
          const hitPoint = intersects[0].point;
          match = celestialDestinations.reduce((closest, curr) => {
            const d = curr.pos.distanceTo(hitPoint);
            return (!closest || d < closest.dist) ? { dest: curr, dist: d } : closest;
          }, null);
        }

        if (match && match.dest) {
          const dest = match.dest;
          currentDestIndex = celestialDestinations.indexOf(dest);
          if (navDestNameEl) navDestNameEl.textContent = dest.name;
          updatePlanetCard(dest);

          // Update Target Reticle on screen
          if (targetReticleEl) {
            targetReticleEl.style.left = `${e.clientX}px`;
            targetReticleEl.style.top = `${e.clientY}px`;
            targetReticleEl.style.opacity = '1';
          }

          // If double clicked or clicked directly, initiate smooth approach
          hyperdriveWarp();
        }
      }
    });

    window.addEventListener('keydown', (e) => {
      if (e.code === 'KeyL') {
        landOnPlanet(); // Shortcut 'L' to land on planet!
      } else if (e.code === 'KeyH') {
        hyperdriveWarp(); // Shortcut 'H' for Hyperdrive!
      }
    });
'''

# Update cycleDestination to also call updatePlanetCard
old_cycle = '''function cycleDestination() {
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
    }'''

new_cycle = '''function cycleDestination() {
      currentDestIndex = (currentDestIndex + 1) % celestialDestinations.length;
      const target = celestialDestinations[currentDestIndex];
      if (navDestNameEl) navDestNameEl.textContent = target.name;
      updatePlanetCard(target);

      const approachDist = Math.max(22, target.r * 2.4);
      const camPos = new THREE.Vector3(cameraX, cameraY, cameraZ);
      const dir = new THREE.Vector3().subVectors(camPos, target.pos).normalize();
      if (dir.lengthSq() < 0.001) dir.set(0, 0, 1);
      autoNavTarget.copy(target.pos).addScaledVector(dir, approachDist);

      isAutoNavigating = true;
      isLandingMode = false;
      autoNavTimer = 4.0;

      if (blinkNotifyEl) {
        blinkNotifyEl.textContent = `👁️ COURSE LOCKED: ${target.name}`;
        blinkNotifyEl.classList.add('visible');
        setTimeout(() => blinkNotifyEl.classList.remove('visible'), 2400);
      }

      triggerWarpChime();
    }'''

if old_cycle in text:
    text = text.replace(old_cycle, new_interactivity_code + "\n\n    " + new_cycle)
    print("Replaced cycleDestination and added Interactive Raycaster & Landing System!")
else:
    print("Warning: old_cycle not found!")

# Update auto-navigation logic in animate() to allow flying close to/into planets
old_autonav = '''      // Auto-navigation toward blink-selected destination
      if (isAutoNavigating && autoNavTimer > 0) {
        autoNavTimer -= delta;
        const toCelestial = new THREE.Vector3().subVectors(autoNavTarget, new THREE.Vector3(cameraX, cameraY, cameraZ));
        const celestialDist = toCelestial.length();
        if (celestialDist > 25) {
          toCelestial.normalize();
          const navThrust = Math.min(240.0, 50.0 + celestialDist * 0.5);
          flightVelocity.addScaledVector(toCelestial, navThrust * delta);

          // Gently rotate camera to look toward target
          const targetYaw = Math.atan2(-toCelestial.x, -toCelestial.z);
          const targetPitch = Math.asin(toCelestial.y);
          targetRotationY += (targetYaw - targetRotationY) * 0.015;
          targetRotationX += (targetPitch - targetRotationX) * 0.015;
        }
        if (autoNavTimer <= 0 || celestialDist < 60) {
          isAutoNavigating = false;
        }
      }'''

new_autonav = '''      // Auto-navigation & Atmospheric Entry Descent toward destination
      if (isAutoNavigating && autoNavTimer > 0) {
        autoNavTimer -= delta;
        const toCelestial = new THREE.Vector3().subVectors(autoNavTarget, new THREE.Vector3(cameraX, cameraY, cameraZ));
        const celestialDist = toCelestial.length();
        const minApproachDist = isLandingMode ? 2.0 : 8.0;

        if (celestialDist > minApproachDist) {
          toCelestial.normalize();
          // High speed hyperdrive warp with smooth atmospheric deceleration
          const warpSpeed = isLandingMode
            ? Math.min(320.0, 30.0 + celestialDist * 0.8)
            : Math.min(480.0, 45.0 + celestialDist * 0.9);
          flightVelocity.addScaledVector(toCelestial, warpSpeed * delta);

          // Gently align camera to look toward target
          const targetYaw = Math.atan2(-toCelestial.x, -toCelestial.z);
          const targetPitch = Math.asin(toCelestial.y);
          targetRotationY += (targetYaw - targetRotationY) * 0.035;
          targetRotationX += (targetPitch - targetRotationX) * 0.035;
        }

        // Atmospheric Entry FX: Re-entry plasma glow when skimming atmosphere!
        if (currentTargetPlanet) {
          const distToCenter = new THREE.Vector3(cameraX, cameraY, cameraZ).distanceTo(currentTargetPlanet.pos);
          const atmosRadius = currentTargetPlanet.r * 2.2;
          if (distToCenter < atmosRadius) {
            const entryFactor = 1.0 - (distToCenter - currentTargetPlanet.r) / (atmosRadius - currentTargetPlanet.r);
            if (reentryOverlayEl) {
              reentryOverlayEl.style.opacity = Math.max(0, Math.min(0.65, entryFactor * 0.75)).toString();
            }
          } else {
            if (reentryOverlayEl && !isLandingMode) {
              reentryOverlayEl.style.opacity = '0';
            }
          }
        }

        if (autoNavTimer <= 0 || celestialDist <= minApproachDist) {
          isAutoNavigating = false;
        }
      }'''

if old_autonav in text:
    text = text.replace(old_autonav, new_autonav)
    print("Updated autoNav logic in animate() with atmospheric entry and hyperdrive!")
else:
    print("Warning: old_autonav not found!")

# Add continuous rotations for the new exoplanets in animate()
target_rotations_end = "astralGodGroup.rotation.y = Math.sin(elapsed * 0.12) * 0.08;"
new_exoplanet_rotations = '''
      // 19. Exoplanets & Alien Biomes rotation
      keplerMesh.rotation.y = elapsed * 0.18;
      keplerMesh.rotation.x = Math.sin(elapsed * 0.05) * 0.08;
      proximaMesh.rotation.y = 0; // Tidally locked!
      trappistMesh.rotation.y = elapsed * 0.11;
      waspMesh.rotation.y = elapsed * 0.28; // Rapid molten spin!
      ceresMesh.rotation.y = elapsed * 0.22;
      erisMesh.rotation.y = elapsed * 0.07;
      haumeaMesh.rotation.z = elapsed * 0.85; // High speed 4-hour football spin!
      makemakeMesh.rotation.y = elapsed * 0.09;
'''

if target_rotations_end in text:
    text = text.replace(target_rotations_end, new_exoplanet_rotations + "\n      " + target_rotations_end)
    print("Added rotations for all exoplanets in animate()!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Step C complete.")
