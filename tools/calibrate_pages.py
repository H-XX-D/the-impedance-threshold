#!/usr/bin/env python3
import os
import pypdf
import build_argonaut_pdf

for ls in [1.360, 1.365, 1.368, 1.370, 1.372, 1.375, 1.378, 1.380]:
    pages = build_argonaut_pdf.build_pdf_with_params(linespread=ls)
    print(f"linespread={ls:.3f} -> pages={pages}")
    if pages == 420:
        print(f"FOUND EXACT 420 PAGES at linespread={ls:.3f}!")
        break
