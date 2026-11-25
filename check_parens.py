filepath = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

in_script = False
balance = 0
for i, line in enumerate(lines):
    if "<script>" in line:
        in_script = True
        continue
    if "</script>" in line:
        in_script = False
        print(f"End of script at line {i+1}, balance: {balance}")
        break
    if in_script:
        delta = line.count("(") - line.count(")")
        balance += delta
        if delta != 0:
            # check if line contains parens inside quotes
            # e.g. SVG path data or text strings
            pass

print(f"Total script balance: {balance}")

# Let's check which lines contain parens inside quotes
for i, line in enumerate(lines):
    if not in_script and "<script>" in line:
        in_script = True
        continue
    if in_script and "</script>" in line:
        break
    if in_script:
        # Check for strings with parens
        if '"' in line or "'" in line or "`" in line:
            # count parens outside quotes
            out = []
            quote = None
            for c in line:
                if quote is None:
                    if c in ('"', "'", '`'):
                        quote = c
                    else:
                        out.append(c)
                else:
                    if c == quote:
                        quote = None
            clean_line = "".join(out)
            d_raw = line.count("(") - line.count(")")
            d_clean = clean_line.count("(") - clean_line.count(")")
            if d_raw != d_clean:
                print(f"Line {i+1} has parens inside string: raw delta={d_raw}, clean delta={d_clean}")
                print("   " + line.strip()[:80])
