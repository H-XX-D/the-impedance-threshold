with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'r') as f:
    code = f.read()

# Replace the regex with simple string replace
old = """    # Scale down table column widths slightly so row hboxes are strictly within textwidth
    latex_str = re.sub(r'\\real\{0\.2000\}', r'\\real{0.1850}', latex_str)
    latex_str = re.sub(r'\\real\{0\.3333\}', r'\\real{0.3050}', latex_str)
    return latex_str.strip()"""

new = """    # Scale down table column widths slightly so row hboxes are strictly within textwidth
    latex_str = latex_str.replace(r"\\real{0.2000}", r"\\real{0.1800}")
    latex_str = latex_str.replace(r"\\real{0.3333}", r"\\real{0.3000}")
    return latex_str.strip()"""

code = code.replace(old, new)
with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'w') as f:
    f.write(code)

print("Updated with string replace.")
