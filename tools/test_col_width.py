with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'r') as f:
    code = f.read()

# Scale down table column widths slightly so row hboxes are strictly within textwidth
replacement = """    # Scale down table column widths slightly so row hboxes are strictly within textwidth
    latex_str = re.sub(r'\\real\{0\.2000\}', r'\\real{0.1850}', latex_str)
    latex_str = re.sub(r'\\real\{0\.3333\}', r'\\real{0.3050}', latex_str)
    return latex_str.strip()"""

code = code.replace("return latex_str.strip()", replacement)
with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'w') as f:
    f.write(code)

print("Updated table column scaling.")
