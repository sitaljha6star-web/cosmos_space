filepath = r"C:\Users\Sital Kumar\.gemini\antigravity\scratch\realistic-space-website\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

idx_script_start = text.find("<script>\n") + len("<script>\n")
idx_script_end = text.rfind("</script>")

js_code = text[idx_script_start:idx_script_end]

lines = js_code.split("\n")
balance = 0
for i, line in enumerate(lines):
    # strip comments
    c_idx = line.find("//")
    l = line[:c_idx] if c_idx != -1 else line
    
    # strip string literals
    out = []
    quote = None
    escaped = False
    for c in l:
        if quote is None:
            if c in ('"', "'", '`'):
                quote = c
            else:
                out.append(c)
        else:
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == quote:
                quote = None
    clean = "".join(out)
    delta = clean.count("(") - clean.count(")")
    balance += delta
    if balance < 0:
        print(f"Line {i+1} caused negative balance {balance}: {line.strip()[:80]}")
        break

print(f"Final true JS code parenthesis balance: {balance}")
