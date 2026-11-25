import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# ------------------------------------------------------------------------------
# 4. UPDATE GESTURE: RAISED INDEX FINGER TO FLY
# ------------------------------------------------------------------------------
# Let's locate the 2-finger check in onHandResults and change it to RAISED INDEX FINGER!

old_gesture_code = '''        // 2-Finger Flight Gesture:
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
        });'''

new_gesture_code = '''        // RAISED INDEX FINGER FLIGHT GESTURE:
        // Moving by raising your index finger skyward/forward (#8 extended high),
        // while middle, ring, and pinky fingers are lowered or curled!
        const indexRaised  = dist(lm[8], wrist) > dist(lm[6], wrist) * 1.25;
        const middleLowered = dist(lm[12], wrist) < dist(lm[10], wrist) * 1.15;
        const ringLowered   = dist(lm[16], wrist) < dist(lm[14], wrist) * 1.15;
        const pinkyLowered  = dist(lm[20], wrist) < dist(lm[18], wrist) * 1.15;

        // Active if index finger is raised high
        const indexFingerFlight = indexRaised && (middleLowered || ringLowered || pinkyLowered);

        if (indexFingerFlight) {
          anyTwoFingerActive = true;
        }

        detected.push({
          lm,
          handNormX,
          handNormY,
          punchDepth,
          fistClenched,
          indexFingerFlight
        });'''

if old_gesture_code in text:
    text = text.replace(old_gesture_code, new_gesture_code)
    print("Updated flight gesture to RAISED INDEX FINGER!")
else:
    print("Warning: old_gesture_code not found!")

# Update status text in onHandResults
text = text.replace('"🚀 2-Finger Flight Thrust!"', '"🚀 Index Finger Flying!"')

# ------------------------------------------------------------------------------
# 5. ANIMATIONS IN ANIMATE() FOR BIRDS, ANIMALS, NPCS, WORMHOLE, SCATTERED ASTEROIDS
# ------------------------------------------------------------------------------

target_anim_marker = "astralGodGroup.rotation.y = Math.sin(elapsed * 0.12) * 0.08;"

anim_gta_and_wormhole = '''
      // 20. INTERSTELLAR WORMHOLE DYNAMICS & DIMENSIONAL TELEPORT
      wormholeRing.rotation.z = elapsed * 1.8;
      wormholeThroat.scale.setScalar(1.0 + Math.sin(elapsed * 4.0) * 0.06);

      // Infalling vortex particles
      const vPos = vortexGeo.attributes.position.array;
      for (let i = 0; i < vortexCount; i++) {
        const idx = i * 3;
        vortexAngles[i] += delta * 2.5;
        vortexRadii[i] -= delta * 12;
        if (vortexRadii[i] < 4) vortexRadii[i] = 88;
        vPos[idx]     = Math.cos(vortexAngles[i]) * vortexRadii[i];
        vPos[idx + 2] = Math.sin(vortexAngles[i]) * vortexRadii[i];
      }
      vortexGeo.attributes.position.needsUpdate = true;

      // Wormhole Proximity Teleport: Flying into the wormhole warps you directly to Earth's Open World!
      const distToWormhole = new THREE.Vector3(cameraX, cameraY, cameraZ).distanceTo(wormholeGroup.position);
      if (distToWormhole < 48) {
        // Teleport right into Earth's city and monuments!
        cameraX = 180;
        cameraY = 55;
        cameraZ = -100;
        flightVelocity.set(0, 0, -20);
        triggerWarpChime();
        if (reentryOverlayEl) {
          reentryOverlayEl.style.opacity = '1.0';
          setTimeout(() => { reentryOverlayEl.style.opacity = '0'; }, 1500);
        }
      }

      // 21. LIVING EARTH GROUND WORLD: ANIMALS, BIRDS, NPCS & CITY
      // A) Birds flapping wings and circling in the sky
      for (let b = 0; b < birds.length; b++) {
        const bird = birds[b];
        bird.angle += delta * bird.speed;
        bird.group.position.x = Math.cos(bird.angle) * bird.radius;
        bird.group.position.z = Math.sin(bird.angle) * bird.radius;
        bird.group.rotation.y = -bird.angle + Math.PI / 2;
        const wingFlap = Math.sin(elapsed * 14.0 + b) * 0.45;
        bird.wingL.rotation.z = wingFlap;
        bird.wingR.rotation.z = -wingFlap;
      }

      // B) Deer walking and grazing on the meadows
      for (let d = 0; d < deerList.length; d++) {
        const deer = deerList[d];
        const walk = Math.sin(elapsed * 4.0 + d);
        deer.legs[0].rotation.x = walk * 0.35;
        deer.legs[1].rotation.x = -walk * 0.35;
        deer.legs[2].rotation.x = -walk * 0.35;
        deer.legs[3].rotation.x = walk * 0.35;
      }

      // C) Dolphins leaping out of coastal ocean water
      for (let dp = 0; dp < dolphins.length; dp++) {
        const dol = dolphins[dp];
        const leap = Math.sin(elapsed * 2.2 + dol.phase);
        dol.mesh.position.y = Math.max(0, leap * 4.5);
        dol.mesh.rotation.x = Math.PI / 2 - (leap * 0.6);
      }

      // D) Human NPCs walking along city streets with swinging limbs
      for (let n = 0; n < npcList.length; n++) {
        const npc = npcList[n];
        npc.walkCycle += delta * npc.speed * 4.5;
        const legSwing = Math.sin(npc.walkCycle);
        npc.legL.rotation.x = legSwing * 0.45;
        npc.legR.rotation.x = -legSwing * 0.45;
        npc.armL.rotation.x = -legSwing * 0.4;
        npc.armR.rotation.x = legSwing * 0.4;

        // Slow walking along street grid
        npc.group.position.x += Math.cos(npc.dir) * delta * npc.speed * 1.5;
        npc.group.position.z += Math.sin(npc.dir) * delta * npc.speed * 1.5;
        if (Math.abs(npc.group.position.x + 45) > 35 || Math.abs(npc.group.position.z + 30) > 35) {
          npc.dir += Math.PI * 0.8;
          npc.group.rotation.y = npc.dir;
        }
      }

      // 22. Scattered Asteroids Continuous Omnidirectional Drift
      const sPos = beltGeo.attributes.position.array;
      for (let i = 0; i < beltCount; i++) {
        const idx = i * 3;
        sPos[idx]     += beltVelocities[idx]     * delta * 12;
        sPos[idx + 1] += beltVelocities[idx + 1] * delta * 12;
        sPos[idx + 2] += beltVelocities[idx + 2] * delta * 12;

        // Wrap around when reaching distant universe boundary
        if (Math.abs(sPos[idx]) > 13000) sPos[idx] *= -0.96;
        if (Math.abs(sPos[idx + 1]) > 9000) sPos[idx + 1] *= -0.96;
        if (Math.abs(sPos[idx + 2]) > 13000) sPos[idx + 2] *= -0.96;
      }
      beltGeo.attributes.position.needsUpdate = true;
'''

if target_anim_marker in text:
    text = text.replace(target_anim_marker, anim_gta_and_wormhole + "\n      " + target_anim_marker)
    print("Added animations for Wormhole, Animals, Birds, NPCs & Scattered Asteroids in animate()!")
else:
    print("Warning: target_anim_marker not found!")

# Add Wormhole to celestialDestinations
if '{ name: "THE INTERSTELLAR WORMHOLE"' not in text:
    dest_find = '{ name: "THE SUN"'
    new_wormhole_dest = '{ name: "THE INTERSTELLAR WORMHOLE", pos: new THREE.Vector3(450, 180, -520), r: 36, type: "DIMENSIONAL WARP GATE", atmos: "Gravitational Lensing Distortion", bio: "Direct Gateway to Earth Surface", mesh: wormholeGroup },\n      { name: "EARTH (CITY, MONUMENTS & JUNGLE)", pos: new THREE.Vector3(180, 35, -120), r: 24, type: "OPEN-WORLD PLANETARY CAPITAL", atmos: "N2, O2, Clouds", bio: "Skyscrapers, Animals, Jungle & Humans", mesh: earthMesh },\n      '
    text = text.replace(dest_find, new_wormhole_dest + dest_find)
    print("Added Wormhole and Earth Open World to celestial destinations!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Part 4 complete.")
