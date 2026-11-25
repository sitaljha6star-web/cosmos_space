html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the entire animate function (from "function animate() {" to "animate();")
idx_animate = text.find("function animate() {")
idx_animate_call = text.find("animate();", idx_animate) + len("animate();")

new_animate = '''function animate() {
      requestAnimationFrame(animate);

      const delta = clock.getDelta();
      const elapsed = clock.getElapsedTime();

      // ================================================================
      // 2-FINGER FLIGHT & KEYBOARD FLIGHT VELOCITY INTEGRATION
      // ================================================================
      const flightSpeed = 140.0;
      const camDir = new THREE.Vector3();

      // Build flight direction from camera look
      camDir.set(
        -Math.sin(rotationY) * Math.cos(rotationX),
        Math.sin(rotationX),
        -Math.cos(rotationY) * Math.cos(rotationX)
      ).normalize();

      if (isTwoFingerFlying || isKeyboardFlyingForward) {
        flightVelocity.addScaledVector(camDir, flightSpeed * delta);
      }
      if (isKeyboardFlyingBackward) {
        flightVelocity.addScaledVector(camDir, -flightSpeed * 0.7 * delta);
      }

      // Apply flight velocity with inertial damping
      flightVelocity.multiplyScalar(0.93);
      cameraX += flightVelocity.x * delta;
      cameraY += flightVelocity.y * delta;
      cameraZ += flightVelocity.z * delta;

      // Auto-navigation toward blink-selected destination
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
      }

      // Camera smooth damping in all directions (X, Y, Z + rotation tilt/pan)
      rotationX += (targetRotationX - rotationX) * 0.055;
      rotationY += (targetRotationY - rotationY) * 0.055;
      cameraZ += (targetCameraZ - cameraZ) * 0.015;
      cameraX += (targetCameraX - cameraX) * 0.015;
      cameraY += (targetCameraY - cameraY) * 0.015;

      camera.position.set(cameraX, cameraY, cameraZ);
      camera.rotation.x = rotationX;
      camera.rotation.y = rotationY;

      // Dynamic screen shake on asteroid impact
      if (screenShakeIntensity > 0.01) {
        camera.position.x += (Math.random() - 0.5) * screenShakeIntensity * 2.2;
        camera.position.y += (Math.random() - 0.5) * screenShakeIntensity * 2.2;
        camera.position.z += (Math.random() - 0.5) * screenShakeIntensity * 1.2;
        screenShakeIntensity *= 0.86;
      }

      // ================================================================
      // CELESTIAL BODY CONTINUOUS ROTATION & ORBITAL DYNAMICS
      // ================================================================
      // 1. The Sun: Slow majestic axial rotation + Corona pulsation
      sunMesh.rotation.y = elapsed * 0.08;
      sunCorona.scale.setScalar(1.0 + Math.sin(elapsed * 2.5) * 0.06);
      sunCoronaMat.opacity = 0.35 + Math.sin(elapsed * 3.8) * 0.15;

      // 2. Earth: Axial rotation + Cloud drift
      earthMesh.rotation.y = elapsed * 0.22;
      earthClouds.rotation.y = elapsed * 0.08;

      // 3. Moon orbit around Earth
      const moonOrbitRadius = 36;
      const moonAngle = elapsed * 0.35;
      moonMesh.position.set(
        earthMesh.position.x + Math.cos(moonAngle) * moonOrbitRadius,
        earthMesh.position.y + 2,
        earthMesh.position.z + Math.sin(moonAngle) * moonOrbitRadius
      );
      moonMesh.rotation.y = elapsed * 0.1;

      // 4. Mars: Slow rotation
      marsMesh.rotation.y = elapsed * 0.19;

      // 5. Jupiter: Gas band rotation
      jupiterMesh.rotation.y = elapsed * 0.15;

      // 6. Saturn & Rings: Majestic slow axial rotation
      saturnMesh.rotation.y = elapsed * 0.12;

      // 7. Black Hole: Accretion disk spin + lensing halo shimmer
      blackHoleAccretion.rotation.z = elapsed * 0.65;
      blackHoleLensing.rotation.z = -elapsed * 0.3;
      blackHoleLensing.scale.setScalar(1.0 + Math.sin(elapsed * 1.8) * 0.08);

      // 8. VISHVARUPA ASTRAL GOD: Ethereal cosmic breathing & Sudarshana Chakra spin
      astralGodGroup.rotation.y = Math.sin(elapsed * 0.12) * 0.08;
      astralGodGroup.position.y = 140 + Math.sin(elapsed * 0.4) * 4.5;

      // Sudarshana Chakra spinning at divine velocity
      sudarshanaGroup.rotation.z = elapsed * 3.5;
      sudarshanaOuterDisc.rotation.z = elapsed * -1.2;
      chakraOuterMat.opacity = 0.68 + Math.sin(elapsed * 6.0) * 0.18;
      chakraInnerMat.opacity = 0.55 + Math.sin(elapsed * 8.0) * 0.22;
      chakraLight.intensity = 4.0 + Math.sin(elapsed * 7.5) * 2.5;

      // Astral God stardust shimmer
      const aPos = astralGeo.attributes.position.array;
      for (let i = 0; i < astralCount; i += 6) {
        const idx = i * 3;
        aPos[idx]     += Math.sin(elapsed * 2.0 + i * 0.1) * 0.015;
        aPos[idx + 1] += Math.cos(elapsed * 1.5 + i * 0.08) * 0.012;
      }
      astralGeo.attributes.position.needsUpdate = true;

      // ----------------------------------------------------------------
      // UPDATE BOTH FISTS (LEFT & RIGHT) — POSITION, MORPHING, CHAKRA FX
      // ----------------------------------------------------------------
      for (let f = 0; f < dualFists.length; f++) {
        const fist = dualFists[f];

        // Smooth world position interpolation
        fist.currentWorldPos.lerp(fist.targetWorldPos, 0.16);

        // Clench transition factor lerp
        const targetF = fist.isClenched ? 1.0 : 0.0;
        fist.transitionFactor += (targetF - fist.transitionFactor) * (fist.isClenched ? 0.045 : 0.035);
        const factor = fist.transitionFactor;

        // Shockwave on clench crossing 0.95
        if (fist.lastFactor < 0.95 && factor >= 0.95) {
          shockwaveActive = true;
          shockwaveRadius = 1.0;
          shockwaveOpacity = 1.0;
          shockwaveRing.position.copy(fist.currentWorldPos);
          triggerFistSound(true);
        }
        if (fist.lastFactor > 0.1 && factor <= 0.1) {
          triggerFistSound(false);
        }
        fist.lastFactor = factor;

        // Core glow light
        fist.coreLight.intensity = factor * 6.5 + Math.sin(elapsed * 10.0 + f * 3.0) * (factor * 2.0);
        fist.coreLight.position.copy(fist.currentWorldPos);

        // Particle morphing for this fist
        const posArray = fist.geo.attributes.position.array;
        const colArray = fist.geo.attributes.color.array;

        for (let i = 0; i < fist.count; i++) {
          const idx = i * 3;
          const delay = fist.delays[i];

          const rawFactor = factor < 0.001
            ? 0.0
            : Math.max(0, Math.min(1, (factor - delay * 0.42) / 0.58));
          const pFactor = rawFactor * rawFactor * (3 - 2 * rawFactor);

          const origX = fist.originPos[idx];
          const origY = fist.originPos[idx + 1];
          const origZ = fist.originPos[idx + 2];

          const targetX = fist.fistTargets[idx] + fist.currentWorldPos.x;
          const targetY = fist.fistTargets[idx + 1] + fist.currentWorldPos.y;
          const targetZ = fist.fistTargets[idx + 2] + fist.currentWorldPos.z;

          if (pFactor > 0.001) {
            const swirlAngle = (1.0 - pFactor) * 3.5 + elapsed * (fist.isLeft ? -0.5 : 0.5);
            const cosS = Math.cos(swirlAngle * (1.0 - pFactor));
            const sinS = Math.sin(swirlAngle * (1.0 - pFactor));
            const dx = origX - fist.currentWorldPos.x;
            const dz = origZ - fist.currentWorldPos.z;
            const swirledX = fist.currentWorldPos.x + (dx * cosS - dz * sinS);
            const swirledZ = fist.currentWorldPos.z + (dx * sinS + dz * cosS);

            posArray[idx]     = THREE.MathUtils.lerp(swirledX, targetX, pFactor);
            posArray[idx + 1] = THREE.MathUtils.lerp(origY, targetY, pFactor);
            posArray[idx + 2] = THREE.MathUtils.lerp(swirledZ, targetZ, pFactor);

            if (pFactor > 0.88) {
              const jitter = (1.0 - pFactor) * 0.4 + 0.05;
              posArray[idx]     += (Math.random() - 0.5) * jitter;
              posArray[idx + 1] += (Math.random() - 0.5) * jitter;
              posArray[idx + 2] += (Math.random() - 0.5) * jitter;
            }

            const glow = pFactor * pFactor;
            if (fist.isLeft) {
              colArray[idx]     = THREE.MathUtils.lerp(0.6, 0.22, glow);
              colArray[idx + 1] = THREE.MathUtils.lerp(0.75, 0.74, glow);
              colArray[idx + 2] = THREE.MathUtils.lerp(1.0, 0.97, glow);
            } else {
              colArray[idx]     = THREE.MathUtils.lerp(1.0, 1.0, glow);
              colArray[idx + 1] = THREE.MathUtils.lerp(0.6, 0.47, glow);
              colArray[idx + 2] = THREE.MathUtils.lerp(0.3, 0.13, glow);
            }
          } else {
            // Free-floating ambient drift
            posArray[idx]     += (Math.random() - 0.5) * 0.02;
            posArray[idx + 1] += (Math.random() - 0.5) * 0.02;
            posArray[idx + 2] += (Math.random() - 0.5) * 0.02;
            colArray[idx]     = THREE.MathUtils.lerp(colArray[idx], 0.5, 0.02);
            colArray[idx + 1] = THREE.MathUtils.lerp(colArray[idx + 1], 0.55, 0.02);
            colArray[idx + 2] = THREE.MathUtils.lerp(colArray[idx + 2], 0.65, 0.02);
          }
        }

        fist.geo.attributes.position.needsUpdate = true;
        fist.geo.attributes.color.needsUpdate = true;

        // Chakra ring
        const chakraVis = THREE.MathUtils.clamp(factor * 1.4 - 0.35, 0, 1);
        fist.chakraRing.position.copy(fist.currentWorldPos);
        fist.chakraRing.rotation.z = elapsed * (fist.isLeft ? -3.8 : 3.8);
        const chakraScale = 2.5 + factor * 10.0 + Math.sin(elapsed * 7.5 + f) * factor * 2.0;
        fist.chakraRing.scale.setScalar(chakraScale);
        fist.chakraRingMat.opacity = chakraVis * 0.65 + Math.sin(elapsed * 6.0 + f) * chakraVis * 0.15;

        fist.chakraInner.position.copy(fist.currentWorldPos);
        fist.chakraInner.rotation.z = -elapsed * (fist.isLeft ? -4.2 : 4.2);
        fist.chakraInnerMat.opacity = chakraVis * 0.35;
      }

      // Shared expanding shockwave
      if (shockwaveActive) {
        shockwaveRadius += delta * 28;
        shockwaveOpacity = Math.max(0, 1.0 - (shockwaveRadius - 1) / 22);
        shockwaveRing.scale.setScalar(shockwaveRadius);
        shockwaveMat.opacity = shockwaveOpacity * 0.9;
        if (shockwaveOpacity <= 0) {
          shockwaveActive = false;
          shockwaveMat.opacity = 0;
        }
      }

      // ----------------------------------------------------------------
      // BACKGROUND AMBIENT PARTICLES — gentle drift
      // ----------------------------------------------------------------
      const ambPos = ambientGeo.attributes.position.array;
      for (let i = 0; i < ambientCount; i += 4) {
        const idx = i * 3;
        ambPos[idx]     += ambientVel[idx]     * delta * 8;
        ambPos[idx + 1] += ambientVel[idx + 1] * delta * 8;
        ambPos[idx + 2] += ambientVel[idx + 2] * delta * 8;
        if (Math.abs(ambPos[idx]) > 1400) ambPos[idx] *= -0.98;
        if (Math.abs(ambPos[idx + 1]) > 400) ambPos[idx + 1] *= -0.98;
        if (Math.abs(ambPos[idx + 2]) > 1400) ambPos[idx + 2] *= -0.98;
      }
      ambientGeo.attributes.position.needsUpdate = true;

      // ----------------------------------------------------------------
      // EXPLOSIVE DEBRIS PARTICLES UPDATE
      // ----------------------------------------------------------------
      let debrisActive = false;
      for (let i = 0; i < maxDebris; i++) {
        if (debrisLifespans[i] > 0) {
          debrisLifespans[i] -= delta * 1.6;
          debrisPositions[i * 3]     += debrisVelocities[i * 3]     * delta;
          debrisPositions[i * 3 + 1] += debrisVelocities[i * 3 + 1] * delta;
          debrisPositions[i * 3 + 2] += debrisVelocities[i * 3 + 2] * delta;

          debrisVelocities[i * 3]     *= 0.94;
          debrisVelocities[i * 3 + 1] *= 0.94;
          debrisVelocities[i * 3 + 2] *= 0.94;

          if (debrisLifespans[i] <= 0) {
            debrisPositions[i * 3 + 1] = -9999;
          }
          debrisActive = true;
        }
      }
      if (debrisActive) {
        debrisGeo.attributes.position.needsUpdate = true;
      }

      // ----------------------------------------------------------------
      // DUAL FIST ASTEROID COLLISION (keeps impact physics, removes arcade counter)
      // ----------------------------------------------------------------
      for (let f = 0; f < dualFists.length; f++) {
        const fist = dualFists[f];
        const fistEffectiveRadius = THREE.MathUtils.lerp(4.0, 7.8, fist.transitionFactor);

        for (let i = 0; i < interactiveAsteroids.length; i++) {
          const ast = interactiveAsteroids[i];
          if (ast.hitCooldown > 0) continue;

          const toAst = new THREE.Vector3().subVectors(ast.mesh.position, fist.currentWorldPos);
          const dist = toAst.length();
          const hitRadius = ast.radius + fistEffectiveRadius;

          if (dist < hitRadius && ast.hitCooldown <= 0) {
            ast.hitCooldown = 0.32;

            const punchDir = toAst.normalize();
            if (punchDir.lengthSq() < 0.001) punchDir.set(0, 0, -1);

            const isSuperPunch = fist.transitionFactor > 0.45;
            const impulsePower = isSuperPunch ? 72.0 : 30.0;

            ast.velocity.addScaledVector(punchDir, impulsePower);
            ast.angularVel.x += (Math.random() - 0.5) * 0.5;
            ast.angularVel.y += (Math.random() - 0.5) * 0.5;
            ast.angularVel.z += (Math.random() - 0.5) * 0.5;

            ast.material.emissive.setHex(fist.isLeft ? 0x38bdf8 : 0xff7722);
            ast.flashTimer = 0.32;

            const contactPoint = fist.currentWorldPos.clone().addScaledVector(punchDir, fistEffectiveRadius);
            spawnDebris(contactPoint, isSuperPunch ? 35 : 18, punchDir, isSuperPunch ? 1.4 : 0.85);

            triggerImpactSound(isSuperPunch ? 1.0 : 0.6);
            screenShakeIntensity = isSuperPunch ? 1.6 : 0.7;

            shockwaveActive = true;
            shockwaveRadius = 1.0;
            shockwaveOpacity = 1.0;
            shockwaveRing.position.copy(contactPoint);
          }
        }
      }

      // Asteroid physics & gravitational recall
      for (let i = 0; i < interactiveAsteroids.length; i++) {
        const ast = interactiveAsteroids[i];
        if (ast.hitCooldown > 0) ast.hitCooldown -= delta;

        ast.mesh.position.addScaledVector(ast.velocity, delta);
        ast.mesh.rotation.x += ast.angularVel.x;
        ast.mesh.rotation.y += ast.angularVel.y;
        ast.mesh.rotation.z += ast.angularVel.z;

        ast.velocity.multiplyScalar(0.965);
        ast.angularVel.multiplyScalar(0.985);

        const driftFromHome = new THREE.Vector3().subVectors(ast.homePos, ast.mesh.position);
        if (driftFromHome.length() > 0.5) {
          ast.mesh.position.addScaledVector(driftFromHome, delta * 0.85);
        }

        if (ast.flashTimer > 0) {
          ast.flashTimer -= delta;
          if (ast.flashTimer <= 0) {
            ast.material.emissive.setHex(0x000000);
          }
        }
      }

      // Rotate background stars
      deepStarField.rotation.y = elapsed * 0.0003;

      renderer.render(cosmosScene, camera);
    }

    animate();'''

text = text[:idx_animate] + new_animate + text[idx_animate_call:]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Step 4 complete: animate() fully replaced with flight, celestial rotations, and no smash counter!")
