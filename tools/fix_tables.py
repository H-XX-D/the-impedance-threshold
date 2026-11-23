with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'r') as f:
    code = f.read()

# Add longtable formatting to clean_latex
target = "return latex_str.strip()"
replacement = """    # Shrink longtables slightly so they never exceed textwidth
    latex_str = re.sub(r'\\\\begin\\{longtable\\}\\[\\]\\{@\\{\\}(.*?)\\}',
                       r'\\\\begingroup\\\\footnotesize\\\\setlength{\\\\tabcolsep}{2.5pt}\\\\begin{longtable}[]{@{}\\1}',
                       latex_str)
    latex_str = re.sub(r'\\\\end\\{longtable\\}', r'\\\\end{longtable}\\\\endgroup', latex_str)
    return latex_str.strip()"""

code = code.replace(target, replacement)
with open('/Users/hendrixx./The_Impedance_Threshold/tools/build_argonaut_pdf.py', 'w') as f:
    f.write(code)

print("Updated build_argonaut_pdf.py with table margin protection.")
