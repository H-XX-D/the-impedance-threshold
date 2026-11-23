#!/usr/bin/env python3
import sys
import os

# Let's inspect build_argonaut_pdf.py and run a test compile
import build_argonaut_pdf
pages = build_argonaut_pdf.build_pdf_with_params()
print(f"Current page count with plates: {pages}")
