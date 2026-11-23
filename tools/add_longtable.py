with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'r') as f:
    code = f.read()

code = code.replace(
    r"\usepackage{booktabs}",
    r"\usepackage{booktabs}" + "\n" + r"\usepackage{longtable,calc,array}"
)
with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'w') as f:
    f.write(code)

print("Added longtable,calc,array to preamble.")
