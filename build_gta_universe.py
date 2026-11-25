import re

html_path = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# ==============================================================================
# 1. CLEAN UP ALL WRITTEN TEXT ON SCREEN EXCEPT FOR OPEN CAMERA
# ==============================================================================
# In the HTML body: remove nav-hud, blink-notify, planet-card, hint, hold-fist-btn
# Keep top-dock (Open Camera), reentry-overlay, canvas, and audio button.

old_html_ui_pattern = re.compile(
    r'<!-- Cosmic Exploration Navigation HUD -->.*?'
    r'(<div class="top-dock">.*?</div>\s*</div>)',
    re.DOTALL
)

# We want to keep only top-dock, reentry-overlay, and sound-toggle
clean_html_ui = '''
  <div class="top-dock">
    <button class="cam-btn" id="btn-camera" onclick="toggleCamera()">
      <span id="cam-icon">📹</span>
      <span id="cam-label">Open Camera</span>
    </button>
    <div class="pip-wrapper" id="pip-box">
      <video id="pip-video" autoplay playsinline muted></video>
      <div class="pip-status" id="pip-status">Initializing...</div>
    </div>
  </div>

  <div class="reentry-overlay" id="reentry-overlay"></div>

  <button class="sound-toggle" id="btn-audio" title="Toggle sound" onclick="toggleAudio()">
    <svg id="audio-icon-off" viewBox="0 0 24 24">
      <path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27l4.73 4.73H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>
    </svg>
    <svg id="audio-icon-on" viewBox="0 0 24 24" style="display:none;">
      <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
    </svg>
  </button>
'''

# Find the start of the HUD and replace everything until <script>
idx_hud = text.find('<!-- Cosmic Exploration Navigation HUD -->')
idx_script = text.find('<script>')
if idx_hud != -1 and idx_script != -1:
    text = text[:idx_hud] + clean_html_ui.strip() + "\n\n  " + text[idx_script:]
    print("Cleaned all written overlays! Kept ONLY Open Camera and clean viewport.")
else:
    print("Warning: HUD section not matched!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Part 1 complete.")
