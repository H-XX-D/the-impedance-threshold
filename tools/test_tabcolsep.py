with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'r') as f:
    code = f.read()

# Add \setlength{\tabcolsep}{2pt} in PREAMBLE_TEMPLATE
code = code.replace(
    r"\setlength{\parskip}{0pt}",
    r"\setlength{\parskip}{0pt}" + "\n" + r"\setlength{\tabcolsep}{2pt}"
)
with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'w') as f:
    f.write(code)

print("Added global tabcolsep to build_argonaut_pdf.py")
