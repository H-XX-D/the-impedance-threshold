#!/usr/bin/env python3
"""
build_web_reader.py
Compiles The_Impedance_Threshold_Master_Manuscript.md into a high-performance,
responsive, standalone HTML5 reader for GitHub Pages with complete navigation,
download buttons (PDF & EPUB), MathJax support, and dark-mode sci-fi telemetry aesthetics.
Author: Todd Hendrixx
"""

import os
import re
import subprocess
from pathlib import Path

ROOT_DIR = Path("/Users/hendrixx./The_Impedance_Threshold")
MANUSCRIPT_MD = ROOT_DIR / "The_Impedance_Threshold_Master_Manuscript.md"
INDEX_HTML = ROOT_DIR / "index.html"

def main():
    print(f"Reading manuscript from {MANUSCRIPT_MD}...")
    if not MANUSCRIPT_MD.exists():
        raise FileNotFoundError(f"Manuscript not found at {MANUSCRIPT_MD}")

    # Step 1: Render markdown to HTML body via pandoc
    print("Executing pandoc with mathjax and gfm extensions...")
    cmd = [
        "pandoc",
        "--mathjax",
        "-f", "markdown+smart+gfm_auto_identifiers",
        "-t", "html5",
        str(MANUSCRIPT_MD)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    body_html = res.stdout

    # Step 2: Build TOC structure by scanning headings
    print("Building structured Table of Contents...")
    with open(MANUSCRIPT_MD, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Define the canonical outline groups
    toc_items = [
        {"id": "the-impedance-threshold-argonaut", "title": "Front Matter & Dramatis Personae", "level": 1, "badge": "PROLOGUE"},
        
        {"id": "act-i-the-pulsar-bench", "title": "Act I: The Pulsar Bench", "level": 1, "badge": "ACT I"},
        {"id": "chapter-one", "title": "Ch 1: The Gridless Sky", "level": 2},
        {"id": "chapter-two", "title": "Ch 2: The Weight of Relations", "level": 2},
        {"id": "chapter-three", "title": "Ch 3: Tides in the Granite", "level": 2},
        {"id": "chapter-four", "title": "Ch 4: The Seven-Watt Partition", "level": 2},
        {"id": "inter-act-dossier-i", "title": "Dossier I: Giles County Sagnac Array", "level": 2, "badge": "DOSSIER"},
        
        {"id": "act-ii-the-cislunar-crucible", "title": "Act II: The Cislunar Crucible", "level": 1, "badge": "ACT II"},
        {"id": "chapter-five", "title": "Ch 5: Flare State", "level": 2},
        {"id": "chapter-six", "title": "Ch 6: The Negative Variance", "level": 2},
        {"id": "chapter-seven", "title": "Ch 7: Dead Man's Trajectory", "level": 2},
        {"id": "chapter-eight", "title": "Ch 8: Light Across the Blind Spot", "level": 2},
        {"id": "inter-act-dossier-ii", "title": "Dossier II: Artemis-7 Recovery Telemetry", "level": 2, "badge": "DOSSIER"},
        
        {"id": "act-iii-the-callisto-staging", "title": "Act III: The Callisto Staging", "level": 1, "badge": "ACT III"},
        {"id": "chapter-nine", "title": "Ch 9: The Ocean Beyond the Ice", "level": 2},
        {"id": "chapter-ten", "title": "Ch 10: Catching Smoke", "level": 2},
        {"id": "chapter-eleven", "title": "Ch 11: Fire on the Water", "level": 2},
        {"id": "chapter-twelve", "title": "Ch 12: The Cold Sanctuary", "level": 2},
        {"id": "inter-act-dossier-iii", "title": "Dossier III: Valhalla Basin Infrastructure", "level": 2, "badge": "DOSSIER"},
        
        {"id": "act-iv-the-europa-skimmer", "title": "Act IV: The Europa Skimmer", "level": 1, "badge": "ACT IV"},
        {"id": "chapter-thirteen", "title": "Ch 13: The Dive into the Belt", "level": 2},
        {"id": "chapter-fourteen", "title": "Ch 14: Forty-Two Seconds", "level": 2},
        {"id": "chapter-fifteen", "title": "Ch 15: The Glass Seam in the Dark", "level": 2},
        {"id": "chapter-sixteen", "title": "Ch 16: The Silent Arc", "level": 2},
        {"id": "chapter-seventeen", "title": "Ch 17: Gravity's Needle", "level": 2},
        {"id": "inter-act-dossier-iv", "title": "Dossier IV: Skimmer Dive Flight Profile", "level": 2, "badge": "DOSSIER"},
        
        {"id": "act-v-the-living-grain", "title": "Act V: The Living Grain", "level": 1, "badge": "ACT V"},
        {"id": "chapter-eighteen", "title": "Ch 18: The Quarantine Gate", "level": 2},
        {"id": "chapter-nineteen", "title": "Ch 19: Life Is Simple", "level": 2},
        {"id": "chapter-twenty", "title": "Ch 20: The Rungs Above the Water", "level": 2},
        {"id": "chapter-twenty-one", "title": "Ch 21: The North Sea Horizon", "level": 2},
        {"id": "inter-act-dossier-v", "title": "Dossier V: Interstellar Keel & Biosignature", "level": 2, "badge": "DOSSIER"},
        
        {"id": "diegetic-exhibits-mathematical-appendices", "title": "Diegetic Exhibits & Mathematical Appendices", "level": 1, "badge": "APPENDIX"}
    ]

    toc_html = []
    for item in toc_items:
        lvl_cls = "toc-l1" if item["level"] == 1 else "toc-l2"
        badge = f'<span class="toc-badge">{item["badge"]}</span>' if "badge" in item else ""
        toc_html.append(f'<a href="#{item["id"]}" class="toc-link {lvl_cls}">{badge}<span class="toc-title">{item["title"]}</span></a>')
    
    toc_nav_str = "\n".join(toc_html)

    # HTML page template
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Impedance Threshold: Argonaut | By Todd Hendrixx</title>
  
  <!-- SEO & Social Meta -->
  <meta name="description" content="The Impedance Threshold: Argonaut — A hard science fiction novel of relational spaceflight, autonomous edge avionics, and first life by Todd Hendrixx. Featuring full 420-page manuscript, diegetic plates, and download links.">
  <meta name="author" content="Todd Hendrixx">
  <meta property="og:title" content="The Impedance Threshold: Argonaut by Todd Hendrixx">
  <meta property="og:description" content="Read online or download the 420-page canonical edition of The Impedance Threshold: Argonaut. Accompanied by the public QRC Pulsar Benchmark framework.">
  <meta property="og:type" content="book">
  <meta property="og:url" content="https://h-xx-d.github.io/the-impedance-threshold/">
  <meta property="og:image" content="https://h-xx-d.github.io/the-impedance-threshold/assets/plate_01_front_matter_architecture.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="The Impedance Threshold: Argonaut by Todd Hendrixx">
  <meta name="twitter:description" content="A hard science fiction novel and operational autonomous avionics framework.">
  <meta name="twitter:image" content="https://h-xx-d.github.io/the-impedance-threshold/assets/plate_01_front_matter_architecture.png">

  <!-- Typography: Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet">

  <!-- MathJax -->
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['\\\\(', '\\\\)'], ['$', '$']],
        displayMath: [['\\\\[', '\\\\]'], ['$$', '$$']]
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

  <style>
    :root {{
      --bg-primary: #0a0e14;
      --bg-surface: #10151d;
      --bg-sidebar: #0d1118;
      --border-color: #242c38;
      --border-highlight: #3b82f6;
      --text-primary: #e6edf3;
      --text-secondary: #8b949e;
      --text-muted: #6e7681;
      --accent-cyan: #38bdf8;
      --accent-blue: #2563eb;
      --accent-amber: #f59e0b;
      --accent-emerald: #10b981;
      --content-font: 'Newsreader', Georgia, serif;
      --ui-font: 'Inter', -apple-system, sans-serif;
      --mono-font: 'Fira Code', Menlo, monospace;
      --reader-max-width: 780px;
      --font-scale: 1.0;
    }}

    /* Themes */
    body.theme-oled {{
      --bg-primary: #000000;
      --bg-surface: #0a0a0a;
      --bg-sidebar: #050505;
      --border-color: #1a1a1a;
      --text-primary: #dcdcdc;
    }}
    body.theme-sepia {{
      --bg-primary: #fbf0d9;
      --bg-surface: #f4e4c1;
      --bg-sidebar: #ede0c4;
      --border-color: #d8c6a0;
      --text-primary: #2c251e;
      --text-secondary: #5c5246;
      --text-muted: #7d7264;
      --accent-cyan: #964800;
      --accent-blue: #0f4c81;
      --accent-amber: #b45309;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      background-color: var(--bg-primary);
      color: var(--text-primary);
      font-family: var(--ui-font);
      line-height: 1.6;
      overflow-x: hidden;
    }}

    /* Reading Progress Bar */
    #progress-container {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: transparent;
      z-index: 1000;
    }}
    #progress-bar {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #38bdf8, #818cf8, #f59e0b);
      transition: width 0.1s ease;
    }}

    /* Top Navigation Header */
    header.site-header {{
      position: sticky;
      top: 0;
      background: rgba(13, 17, 24, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      z-index: 999;
      padding: 0.65rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    .header-branding {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .header-branding h1 {{
      font-family: 'Cinzel', serif;
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: #ffffff;
      white-space: nowrap;
    }}

    .header-branding .author-tag {{
      font-family: var(--ui-font);
      font-size: 0.8rem;
      font-weight: 500;
      color: var(--accent-cyan);
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 2px 8px;
      border-radius: 4px;
      white-space: nowrap;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      flex-wrap: wrap;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 0.85rem;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
      border: 1px solid transparent;
    }}

    .btn-pdf {{
      background: #dc2626;
      color: #ffffff;
      box-shadow: 0 1px 3px rgba(220, 38, 38, 0.3);
    }}
    .btn-pdf:hover {{
      background: #b91c1c;
      transform: translateY(-1px);
    }}

    .btn-epub {{
      background: #2563eb;
      color: #ffffff;
      box-shadow: 0 1px 3px rgba(37, 99, 235, 0.3);
    }}
    .btn-epub:hover {{
      background: #1d4ed8;
      transform: translateY(-1px);
    }}

    .btn-github {{
      background: #1f2937;
      color: #e5e7eb;
      border: 1px solid var(--border-color);
    }}
    .btn-github:hover {{
      background: #374151;
      color: #ffffff;
    }}

    .btn-control {{
      background: var(--bg-surface);
      color: var(--text-secondary);
      border: 1px solid var(--border-color);
      padding: 0.45rem 0.6rem;
    }}
    .btn-control:hover {{
      color: var(--text-primary);
      border-color: var(--text-secondary);
    }}

    /* Main Container Layout */
    .app-container {{
      display: flex;
      min-height: calc(100vh - 58px);
      position: relative;
    }}

    /* Sidebar Navigation */
    aside.sidebar {{
      width: 320px;
      flex-shrink: 0;
      background: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
      height: calc(100vh - 58px);
      position: sticky;
      top: 58px;
      overflow-y: auto;
      padding: 1.25rem 0.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      scrollbar-width: thin;
      scrollbar-color: var(--border-color) transparent;
    }}

    .sidebar-header {{
      padding: 0 0.5rem 0.75rem;
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 0.5rem;
    }}

    .sidebar-header h2 {{
      font-size: 0.75rem;
      font-family: var(--mono-font);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--text-secondary);
      margin-bottom: 0.25rem;
    }}

    .sidebar-search {{
      width: 100%;
      padding: 0.4rem 0.6rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 4px;
      color: var(--text-primary);
      font-size: 0.8rem;
      outline: none;
    }}
    .sidebar-search:focus {{
      border-color: var(--accent-cyan);
    }}

    .toc-link {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 0.6rem;
      border-radius: 5px;
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 0.84rem;
      transition: all 0.12s ease;
      line-height: 1.35;
    }}

    .toc-link:hover {{
      background: rgba(56, 189, 248, 0.08);
      color: var(--text-primary);
    }}

    .toc-link.active {{
      background: rgba(56, 189, 248, 0.16);
      color: var(--accent-cyan);
      font-weight: 600;
      border-left: 3px solid var(--accent-cyan);
    }}

    .toc-l1 {{
      font-weight: 700;
      color: var(--text-primary);
      margin-top: 0.75rem;
      padding-top: 0.5rem;
      border-top: 1px dashed rgba(255, 255, 255, 0.07);
    }}

    .toc-l2 {{
      padding-left: 1.25rem;
      font-size: 0.8rem;
    }}

    .toc-badge {{
      font-family: var(--mono-font);
      font-size: 0.65rem;
      padding: 1px 5px;
      border-radius: 3px;
      background: rgba(255, 255, 255, 0.06);
      color: var(--text-muted);
      letter-spacing: 0.04em;
    }}

    /* Main Content Area */
    main.content-area {{
      flex: 1;
      padding: 3rem 2rem 6rem;
      max-width: 100%;
      display: flex;
      justify-content: center;
    }}

    .manuscript-wrapper {{
      width: 100%;
      max-width: calc(var(--reader-max-width) * var(--font-scale));
      margin: 0 auto;
    }}

    /* Hero / Cover Section */
    .hero-banner {{
      text-align: center;
      padding: 2.5rem 1.5rem 3.5rem;
      margin-bottom: 3.5rem;
      border-bottom: 1px solid var(--border-color);
      background: radial-gradient(circle at center, rgba(37, 99, 235, 0.08) 0%, transparent 70%);
      border-radius: 12px;
    }}

    .hero-tagline {{
      font-family: var(--mono-font);
      font-size: 0.85rem;
      color: var(--accent-cyan);
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin-bottom: 0.75rem;
    }}

    .hero-title {{
      font-family: 'Cinzel', serif;
      font-size: 2.75rem;
      font-weight: 900;
      letter-spacing: 0.06em;
      color: #ffffff;
      line-height: 1.15;
      margin-bottom: 0.75rem;
    }}

    .hero-subtitle {{
      font-family: 'Newsreader', serif;
      font-style: italic;
      font-size: 1.35rem;
      color: var(--text-secondary);
      margin-bottom: 1.5rem;
    }}

    .hero-author {{
      font-family: var(--ui-font);
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 2rem;
    }}

    .hero-specs {{
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }}

    .spec-pill {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      padding: 0.6rem 1.1rem;
      border-radius: 8px;
    }}

    .spec-val {{
      font-family: var(--mono-font);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent-amber);
    }}

    .spec-label {{
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-secondary);
      margin-top: 2px;
    }}

    .hero-buttons {{
      display: flex;
      justify-content: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .hero-buttons .btn {{
      font-size: 0.95rem;
      padding: 0.65rem 1.4rem;
    }}

    /* Manuscript Typography & Formatting */
    article.manuscript {{
      font-family: var(--content-font);
      font-size: calc(1.22rem * var(--font-scale));
      line-height: 1.78;
      color: var(--text-primary);
    }}

    article.manuscript h1 {{
      font-family: 'Cinzel', serif;
      font-size: calc(2.1rem * var(--font-scale));
      font-weight: 800;
      letter-spacing: 0.04em;
      color: #ffffff;
      margin: 4rem 0 1rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border-color);
      line-height: 1.25;
      text-align: center;
    }}

    article.manuscript h1:first-of-type {{
      border-top: none;
      margin-top: 0;
      padding-top: 0;
    }}

    article.manuscript h2 {{
      font-family: 'Cinzel', serif;
      font-size: calc(1.5rem * var(--font-scale));
      font-weight: 700;
      color: var(--accent-cyan);
      margin: 2.5rem 0 1.2rem;
      line-height: 1.3;
      text-align: center;
    }}

    article.manuscript h3 {{
      font-family: var(--ui-font);
      font-size: calc(1.15rem * var(--font-scale));
      font-weight: 600;
      color: var(--accent-amber);
      margin: 2rem 0 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    article.manuscript h4 {{
      font-family: var(--mono-font);
      font-size: calc(0.95rem * var(--font-scale));
      font-weight: 600;
      color: var(--text-secondary);
      margin: 1.5rem 0 0.5rem;
      letter-spacing: 0.04em;
    }}

    article.manuscript p {{
      margin-bottom: 1.35em;
      text-align: justify;
      hyphens: auto;
    }}

    article.manuscript hr {{
      border: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--border-color), transparent);
      margin: 3.5rem 0;
    }}

    article.manuscript ul, article.manuscript ol {{
      margin: 1.2em 0 1.5em 2em;
    }}

    article.manuscript li {{
      margin-bottom: 0.5em;
    }}

    article.manuscript blockquote {{
      border-left: 3px solid var(--accent-cyan);
      padding: 0.75rem 1.25rem;
      margin: 1.5rem 0;
      background: rgba(56, 189, 248, 0.04);
      font-style: italic;
      color: var(--text-secondary);
      border-radius: 0 6px 6px 0;
    }}

    article.manuscript figure {{
      margin: 3rem 0;
      text-align: center;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }}

    article.manuscript img {{
      max-width: 100%;
      height: auto;
      border-radius: 4px;
      cursor: zoom-in;
      transition: transform 0.2s ease;
    }}

    article.manuscript img:hover {{
      transform: scale(1.005);
    }}

    article.manuscript figcaption {{
      font-family: var(--mono-font);
      font-size: 0.8rem;
      color: var(--text-secondary);
      margin-top: 0.8rem;
      padding: 0.4rem;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
    }}

    article.manuscript table {{
      width: 100%;
      border-collapse: collapse;
      margin: 2rem 0;
      font-family: var(--mono-font);
      font-size: 0.85rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      overflow: hidden;
    }}

    article.manuscript th, article.manuscript td {{
      padding: 0.65rem 0.9rem;
      text-align: left;
      border-bottom: 1px solid var(--border-color);
    }}

    article.manuscript th {{
      background: rgba(255, 255, 255, 0.04);
      font-weight: 600;
      color: var(--accent-cyan);
      border-bottom: 2px solid var(--border-color);
    }}

    article.manuscript tr:last-child td {{
      border-bottom: none;
    }}

    article.manuscript pre {{
      background: #05070a;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 1.25rem;
      overflow-x: auto;
      font-family: var(--mono-font);
      font-size: 0.84rem;
      margin: 1.5rem 0;
    }}

    article.manuscript code {{
      font-family: var(--mono-font);
      font-size: 0.88em;
      background: rgba(255, 255, 255, 0.06);
      padding: 2px 5px;
      border-radius: 3px;
      color: var(--accent-cyan);
    }}

    article.manuscript pre code {{
      background: transparent;
      padding: 0;
      color: var(--text-primary);
    }}

    /* Lightbox Modal */
    #lightbox {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.92);
      z-index: 2000;
      justify-content: center;
      align-items: center;
      cursor: zoom-out;
      padding: 2rem;
    }}
    #lightbox img {{
      max-width: 95%;
      max-height: 95%;
      border-radius: 6px;
      box-shadow: 0 0 30px rgba(0, 0, 0, 0.8);
    }}

    /* Mobile Responsive */
    @media (max-width: 900px) {{
      aside.sidebar {{
        display: none;
        position: fixed;
        left: 0;
        top: 58px;
        z-index: 1001;
        width: 80%;
        max-width: 320px;
        box-shadow: 10px 0 30px rgba(0, 0, 0, 0.7);
      }}
      aside.sidebar.mobile-open {{
        display: flex;
      }}
      .mobile-menu-btn {{
        display: inline-flex !important;
      }}
      .hero-title {{
        font-size: 2rem;
      }}
    }}

    .mobile-menu-btn {{
      display: none;
      background: var(--bg-surface);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
      padding: 0.4rem 0.7rem;
      border-radius: 6px;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <!-- Reading Progress Bar -->
  <div id="progress-container"><div id="progress-bar"></div></div>

  <!-- Header -->
  <header class="site-header">
    <div class="header-branding">
      <button class="mobile-menu-btn" id="menuToggle" title="Toggle Navigation">☰</button>
      <h1>THE IMPEDANCE THRESHOLD</h1>
      <span class="author-tag">By Todd Hendrixx</span>
    </div>

    <div class="header-actions">
      <a href="The_Impedance_Threshold.pdf" class="btn btn-pdf" download>
        <span>📥</span> Download PDF (420p)
      </a>
      <a href="The_Impedance_Threshold.epub" class="btn btn-epub" download>
        <span>📖</span> Download EPUB
      </a>
      <a href="qrc_preprint.pdf" class="btn btn-theory" download style="background: #4f46e5; color: #ffffff;">
        <span>📄</span> Theory Preprint (PDF)
      </a>
      <a href="https://github.com/H-XX-D/qrc-pulsar-benchmark" target="_blank" rel="noopener" class="btn btn-github">
        <span>⚡</span> QRC Code (GitHub)
      </a>
      <button class="btn btn-control" id="fontMinus" title="Decrease font size">A-</button>
      <button class="btn btn-control" id="fontPlus" title="Increase font size">A+</button>
      <button class="btn btn-control" id="themeToggle" title="Toggle OLED / Sepia / Dark Theme">🌓</button>
    </div>
  </header>

  <div class="app-container">
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <h2>Table of Contents</h2>
        <input type="text" id="searchTOC" class="sidebar-search" placeholder="Search chapters & dossiers...">
      </div>
      <nav id="tocNav">
        {toc_nav_str}
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="content-area">
      <div class="manuscript-wrapper">
        <!-- Hero Banner -->
        <section class="hero-banner">
          <div class="hero-tagline">Canonical Exospecies Prequel &amp; Autonomous Avionics Framework</div>
          <h1 class="hero-title">THE IMPEDANCE THRESHOLD: ARGONAUT</h1>
          <p class="hero-subtitle">A Novel of Relational Spaceflight, Edge Avionics, and First Life</p>
          <div class="hero-author">By Todd Hendrixx</div>

          <div class="hero-specs">
            <div class="spec-pill">
              <span class="spec-val">420</span>
              <span class="spec-label">Print Pages</span>
            </div>
            <div class="spec-pill">
              <span class="spec-val">38,707</span>
              <span class="spec-label">Words</span>
            </div>
            <div class="spec-pill">
              <span class="spec-val">21</span>
              <span class="spec-label">Chapters</span>
            </div>
            <div class="spec-pill">
              <span class="spec-val">9</span>
              <span class="spec-label">Diegetic Plates</span>
            </div>
            <div class="spec-pill">
              <span class="spec-val">453 / 453</span>
              <span class="spec-label">PyTests Passing</span>
            </div>
          </div>

          <div class="hero-buttons">
            <a href="The_Impedance_Threshold.pdf" class="btn btn-pdf" download>
              <span>📥</span> Download PDF (Locked 420-Page Edition)
            </a>
            <a href="The_Impedance_Threshold.epub" class="btn btn-epub" download>
              <span>📖</span> Download EPUB (E-Reader Edition)
            </a>
            <a href="qrc_preprint.pdf" class="btn btn-theory" download style="background: #4f46e5; color: #ffffff;">
              <span>📄</span> QRC Fundamental Preprint (PDF)
            </a>
            <a href="https://github.com/H-XX-D/qrc-pulsar-benchmark" target="_blank" rel="noopener" class="btn btn-github">
              <span>⚡</span> Inspect QRC Code & Theory Suite
            </a>
          </div>
        </section>

        <!-- Full Manuscript Text -->
        <article class="manuscript" id="manuscriptBody">
          {body_html}
        </article>

        <!-- Footer -->
        <footer style="margin-top: 5rem; padding-top: 2rem; border-top: 1px solid var(--border-color); text-align: center; color: var(--text-muted); font-size: 0.85rem;">
          <p><strong>The Impedance Threshold: Argonaut</strong> &copy; 2026 Todd Hendrixx. All rights reserved.</p>
          <p style="margin-top: 0.5rem;">
            Codebase &amp; Astrodynamics: <a href="https://github.com/H-XX-D/qrc-pulsar-benchmark" style="color: var(--accent-cyan);">github.com/H-XX-D/qrc-pulsar-benchmark</a> &bull;
            Novel Repository: <a href="https://github.com/H-XX-D/the-impedance-threshold" style="color: var(--accent-cyan);">github.com/H-XX-D/the-impedance-threshold</a>
          </p>
        </footer>
      </div>
    </main>
  </div>

  <!-- Lightbox Modal -->
  <div id="lightbox"><img id="lightboxImg" src="" alt="Enlarged Plate"></div>

  <script>
    // Reading Progress Bar
    window.addEventListener('scroll', () => {{
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progress-bar').style.width = scrolled + '%';
    }});

    // Mobile Menu Toggle
    const menuBtn = document.getElementById('menuToggle');
    const sidebar = document.getElementById('sidebar');
    if (menuBtn && sidebar) {{
      menuBtn.addEventListener('click', () => {{
        sidebar.classList.toggle('mobile-open');
      }});
    }}

    // Font Size Controls
    let fontScale = 1.0;
    const fontPlus = document.getElementById('fontPlus');
    const fontMinus = document.getElementById('fontMinus');
    if (fontPlus && fontMinus) {{
      fontPlus.addEventListener('click', () => {{
        if (fontScale < 1.35) {{
          fontScale += 0.08;
          document.documentElement.style.setProperty('--font-scale', fontScale);
        }}
      }});
      fontMinus.addEventListener('click', () => {{
        if (fontScale > 0.8) {{
          fontScale -= 0.08;
          document.documentElement.style.setProperty('--font-scale', fontScale);
        }}
      }});
    }}

    // Theme Toggle (Dark -> OLED -> Sepia)
    const themes = ['', 'theme-oled', 'theme-sepia'];
    let currentThemeIdx = 0;
    const themeBtn = document.getElementById('themeToggle');
    if (themeBtn) {{
      themeBtn.addEventListener('click', () => {{
        document.body.classList.remove(themes[currentThemeIdx]);
        currentThemeIdx = (currentThemeIdx + 1) % themes.length;
        if (themes[currentThemeIdx]) {{
          document.body.classList.add(themes[currentThemeIdx]);
        }}
      }});
    }}

    // Lightbox for figures
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    document.querySelectorAll('article.manuscript img').forEach(img => {{
      img.addEventListener('click', () => {{
        lightboxImg.src = img.src;
        lightbox.style.display = 'flex';
      }});
    }});
    lightbox.addEventListener('click', () => {{
      lightbox.style.display = 'none';
    }});

    // TOC Active ScrollSpy
    const sections = Array.from(document.querySelectorAll('h1[id], h2[id]'));
    const navLinks = Array.from(document.querySelectorAll('.toc-link'));
    window.addEventListener('scroll', () => {{
      let current = '';
      const scrollPos = window.scrollY + 120;
      for (const section of sections) {{
        if (section.offsetTop <= scrollPos) {{
          current = section.getAttribute('id');
        }}
      }}
      navLinks.forEach(link => {{
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {{
          link.classList.add('active');
        }}
      }});
    }});

    // Search TOC Filter
    const searchInput = document.getElementById('searchTOC');
    if (searchInput) {{
      searchInput.addEventListener('input', (e) => {{
        const term = e.target.value.toLowerCase();
        navLinks.forEach(link => {{
          const text = link.innerText.toLowerCase();
          link.style.display = text.includes(term) ? 'flex' : 'none';
        }});
      }});
    }}
  </script>
</body>
</html>
"""

    print(f"Writing index.html to {INDEX_HTML}...")
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    file_size_kb = os.path.getsize(INDEX_HTML) / 1024
    print(f"Generated index.html successfully ({file_size_kb:.1f} KB).")

if __name__ == "__main__":
    main()
