import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update camera far plane to 80,000 units
text = text.replace("0.1, 24000);", "0.1, 80000);")

# 2. Add CSS for Planetary Card, Re-entry FX, and Surface Controls
css_to_add = '''
    /* Planetary Scanner & Landing HUD */
    .planet-card {
      position: fixed;
      bottom: 24px;
      left: 24px;
      z-index: 25;
      background: rgba(10, 15, 28, 0.75);
      border: 1px solid rgba(56, 189, 248, 0.35);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border-radius: 14px;
      padding: 16px 20px;
      width: 290px;
      color: #fff;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6), 0 0 20px rgba(56, 189, 248, 0.15);
      transition: all 0.35s ease;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    .planet-card-header {
      display: flex;
      flex-direction: column;
      margin-bottom: 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 8px;
    }

    .planet-card-type {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 2px;
      color: #38bdf8;
      text-transform: uppercase;
    }

    .planet-card-title {
      font-size: 18px;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #ffffff;
      text-transform: uppercase;
      margin-top: 2px;
    }

    .planet-card-body {
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 11px;
      margin-bottom: 14px;
    }

    .pc-stat {
      display: flex;
      justify-content: space-between;
      color: rgba(255, 255, 255, 0.65);
    }

    .pc-stat strong {
      color: #f8fafc;
      font-weight: 600;
      text-align: right;
    }

    .planet-card-actions {
      display: flex;
      gap: 8px;
    }

    .pc-btn {
      flex: 1;
      padding: 8px 10px;
      border-radius: 8px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      cursor: pointer;
      border: none;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
    }

    .pc-btn.land-btn {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #ffffff;
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.45);
    }

    .pc-btn.land-btn:hover {
      background: linear-gradient(135deg, #0ea5e9, #0284c7);
      transform: translateY(-2px);
      box-shadow: 0 0 22px rgba(14, 165, 233, 0.65);
    }

    .pc-btn.warp-btn {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #f1f5f9;
    }

    .pc-btn.warp-btn:hover {
      background: rgba(255, 255, 255, 0.22);
      transform: translateY(-2px);
    }

    /* Atmospheric Re-entry Plasma Burn Overlay */
    .reentry-overlay {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 5;
      opacity: 0;
      background: radial-gradient(ellipse at center, transparent 40%, rgba(249, 115, 22, 0.25) 75%, rgba(239, 68, 68, 0.55) 100%);
      transition: opacity 0.5s ease;
    }

    /* Target Reticle on Selected Celestial Body */
    .target-reticle {
      position: fixed;
      width: 44px;
      height: 44px;
      border: 1px dashed #38bdf8;
      border-radius: 50%;
      pointer-events: none;
      z-index: 15;
      transform: translate(-50%, -50%);
      opacity: 0;
      transition: opacity 0.3s ease;
      animation: rotateReticle 12s linear infinite;
    }
    @keyframes rotateReticle {
      from { transform: translate(-50%, -50%) rotate(0deg); }
      to { transform: translate(-50%, -50%) rotate(360deg); }
    }
'''

# Insert CSS before </style>
if "</style>" in text:
    text = text.replace("</style>", css_to_add + "\n  </style>")
    print("Added Planetary Card, Reentry, and Reticle CSS!")

# 3. Insert HTML for Planetary Card and Reentry Overlay
html_to_add = '''
  <div class="reentry-overlay" id="reentry-overlay"></div>
  <div class="target-reticle" id="target-reticle"></div>

  <!-- Interactive Planetary Scanner & Surface Landing HUD -->
  <div class="planet-card" id="planet-card">
    <div class="planet-card-header">
      <span class="planet-card-type" id="pc-type">TERRESTRIAL HABITABLE</span>
      <span class="planet-card-title" id="pc-name">EARTH</span>
    </div>
    <div class="planet-card-body">
      <div class="pc-stat"><span>CLASSIFICATION:</span> <strong id="pc-surface">Oceans & Continents</strong></div>
      <div class="pc-stat"><span>ATMOSPHERE:</span> <strong id="pc-atmos">N2, O2, H2O (1.0 atm)</strong></div>
      <div class="pc-stat"><span>BIOSPHERE / PLANTS:</span> <strong id="pc-bio">Lush Flora & Vegetation</strong></div>
    </div>
    <div class="planet-card-actions">
      <button class="pc-btn land-btn" onclick="landOnPlanet()">🚀 ENTER PLANET / LAND</button>
      <button class="pc-btn warp-btn" onclick="hyperdriveWarp()">⚡ HYPERDRIVE</button>
    </div>
  </div>
'''

if '<div class="interaction-hint"' in text:
    text = text.replace('<div class="interaction-hint"', html_to_add + '\n  <div class="interaction-hint"')
    print("Added Planetary Scanner Card and Reentry Overlay HTML!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Step A complete.")
