import re

filepath = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# Find all getElementById
pattern = r'(?:const|let|var)\s+(\w+)\s*=\s*document\.getElementById\(([\'"])([^\'"]+)\2\)'
matches = re.findall(pattern, text)

print("Found getElementById calls:")
for var, q, el_id in matches:
    present = (f'id="{el_id}"' in text) or (f"id='{el_id}'" in text)
    print(f"  {var} = '{el_id}' -> present in HTML: {present}")

# Find any addEventListener called on variables
lines = text.split("\n")
for i, l in enumerate(lines):
    if ".addEventListener(" in l and "window." not in l and "document." not in l:
        print(f"Line {i+1}: {l.strip()[:90]}")
