# Strip comments from index.html and write back in a human‑style format
import re, sys, pathlib

file_path = pathlib.Path(r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html")
text = file_path.read_text(encoding='utf-8')

# Remove HTML comments (including multiline) but keep line breaks
text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

# Remove line comments that start with // after optional whitespace
lines = []
for line in text.splitlines():
    if re.match(r'^\s*//', line):
        continue
    # Remove trailing // comments that are after code (only if preceded by whitespace and //)
    line = re.sub(r'(?<!http:)//.*', '', line)
    lines.append(line)

clean = "\n".join(lines)
# Write back (overwrites original file)
file_path.write_text(clean, encoding='utf-8')
print('Comments stripped')
