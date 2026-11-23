#!/usr/bin/env python3
import sys
import os
sys.path.append('/Users/hendrixx./The_Impedance_Threshold/tools')
from build_argonaut_pdf import build_pdf_with_params

print("Searching for EXACTLY 420 pages...")
found = False

# Fine sweep over linespread and margins
for ls in [1.5680, 1.5685, 1.5690, 1.5695]:
    for top in [1.02, 1.01, 1.00, 1.03]:
        pages = build_pdf_with_params(linespread=ls, top=top, bottom=top)
        print(f"ls={ls:.4f}, top={top:.2f} -> {pages} pages")
        if pages == 420:
            print(f"*** SUCCESS: EXACTLY 420 PAGES with ls={ls:.4f}, top={top:.2f} ***")
            found = True
            break
    if found:
        break

if not found:
    for ls in [1.560, 1.565, 1.570, 1.575]:
        for outer in [0.90, 0.92, 0.94, 0.96]:
            pages = build_pdf_with_params(linespread=ls, outer=outer)
            print(f"ls={ls:.3f}, outer={outer:.2f} -> {pages} pages")
            if pages == 420:
                print(f"*** SUCCESS: EXACTLY 420 PAGES with ls={ls:.3f}, outer={outer:.2f} ***")
                found = True
                break
        if found:
            break
