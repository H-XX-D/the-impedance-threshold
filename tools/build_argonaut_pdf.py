#!/usr/bin/env python3
"""
Typesetting and Constructed PDF Builder for THE IMPEDANCE THRESHOLD: ARGONAUT.
Compiles a publication-grade 5.5" x 8.5" trade paperback book PDF via XeLaTeX.
Target extent: Exactly 420 physical pages.
Sole Author: Todd Hendrixx
"""

import os
import re
import subprocess
import shutil
import sys
import pypdf

PROJECT_ROOT = "/Users/hendrixx./The_Impedance_Threshold"
MANUSCRIPT_DIR = os.path.join(PROJECT_ROOT, "manuscript")
BUILD_DIR = os.path.join(PROJECT_ROOT, "build_pdf")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
OUTPUT_PDF = os.path.join(PROJECT_ROOT, "The_Impedance_Threshold.pdf")

CHAPTERS = [
    (1, "The Gridless Sky", "Chapter_01_The_Gridless_Sky.md"),
    (2, "The Weight of Relations", "Chapter_02_The_Weight_of_Relations.md"),
    (3, "Tides in the Granite", "Chapter_03_Tides_in_the_Granite.md"),
    (4, "The Seven-Watt Partition", "Chapter_04_The_Seven_Watt_Partition.md"),
    (5, "Flare State", "Chapter_05_Flare_State.md"),
    (6, "The Negative Variance", "Chapter_06_The_Negative_Variance.md"),
    (7, "Dead Man's Trajectory", "Chapter_07_Dead_Mans_Trajectory.md"),
    (8, "Light Across the Blind Spot", "Chapter_08_Light_Across_the_Blind_Spot.md"),
    (9, "The Ocean Beyond the Ice", "Chapter_09_The_Ocean_Beyond_the_Ice.md"),
    (10, "Catching Smoke", "Chapter_10_Catching_Smoke.md"),
    (11, "Fire on the Water", "Chapter_11_Fire_on_the_Water.md"),
    (12, "The Cold Sanctuary", "Chapter_12_The_Cold_Sanctuary.md"),
    (13, "The Dive into the Belt", "Chapter_13_The_Dive_into_the_Belt.md"),
    (14, "Forty-Two Seconds", "Chapter_14_Forty_Two_Seconds.md"),
    (15, "The Glass Seam in the Dark", "Chapter_15_The_Glass_Seam_in_the_Dark.md"),
    (16, "The Silent Arc", "Chapter_16_The_Silent_Arc.md"),
    (17, "Gravity's Needle", "Chapter_17_Gravitys_Needle.md"),
    (18, "The Quarantine Gate", "Chapter_18_The_Quarantine_Gate.md"),
    (19, "Life Is Simple", "Chapter_19_Life_Is_Simple.md"),
    (20, "The Rungs Above the Water", "Chapter_20_The_Rungs_Above_the_Water.md"),
    (21, "The North Sea Horizon", "Chapter_21_The_North_Sea_Horizon.md"),
]

ACT_HEADINGS = {
    1: ("Act I: The Pulsar Bench", "Green Bank, The Shape Sphere, Giles County, and Plum Brook"),
    5: ("Act II: The Cislunar Crucible", "The Artemis Flare, Covariance Starvation, Coast-Lock, and Gateway Laser Lock"),
    9: ("Act III: The Callisto Staging", "Project ARGONAUT, The Canister Dilemma, The August 2033 Launch, and The Radiation Haven"),
    13: ("Act IV: The Europa Skimmer", "The Plume Dive, Aerogel Capture, The Laser Weld, The Ghost Run, and Manifold Capture"),
    18: ("Act V: The Living Grain", "The Cleanroom, Inevitable Biology, The Entropy Ladder, and The Keel of Daedalus"),
}

ACT_DOSSIERS = {
    4: ("Inter-Act Dossier I: The Green Bank Baseline & Relational Reduction", "Dossier_Act_I.md"),
    8: ("Inter-Act Dossier II: The Artemis-7 Cislunar Anomaly & Autonomous Recovery", "Dossier_Act_II.md"),
    12: ("Inter-Act Dossier III: Project ARGONAUT Phase C Critical Design Review", "Dossier_Act_III.md"),
    17: ("Inter-Act Dossier IV: The Europa Plume Harvest & The 980-Day Ghost Run", "Dossier_Act_IV.md"),
    21: ("Inter-Act Dossier V: The Gateway Bio-Quarantine Audit & Daedalus Foundation", "Dossier_Act_V.md"),
}

PREAMBLE_TEMPLATE = r"""\documentclass[12pt,twoside,openright]{book}

% Page Geometry: 5.5" x 8.5" US Trade Paperback Standard
\usepackage[
  paperwidth=5.5in,
  paperheight=8.5in,
  inner=__INNER__in,
  outer=__OUTER__in,
  top=__TOP__in,
  bottom=__BOTTOM__in,
  bindingoffset=0.15in,
  headheight=14pt,
  headsep=0.25in,
  footskip=0.40in
]{geometry}

\usepackage{fontspec}
\setmainfont{Georgia}[Ligatures=TeX]
\setmonofont{Menlo}[Scale=0.76]
\setsansfont{Helvetica Neue}[Scale=MatchLowercase]

\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\graphicspath{{/Users/hendrixx./The_Impedance_Threshold/}{/Users/hendrixx./The_Impedance_Threshold/assets/}}
\setkeys{Gin}{width=\linewidth,keepaspectratio}

\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{setspace}
\usepackage{microtype}
\usepackage{booktabs}
\usepackage{longtable,calc,array}
\usepackage{listings}
\usepackage{xcolor}
\usepackage[hidelinks]{hyperref}

% Eliminate margin bleed via flexible micro-spacing
\emergencystretch=2.5em
\tolerance=1200
\hfuzz=1pt

% Leading and Indentation for publication trade paperback
\linespread{__LINESPREAD__}
\setlength{\parindent}{1.6em}
\setlength{\parskip}{0pt}
\setlength{\tabcolsep}{2pt}

\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{0}

% Running Headers & Footers
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\thepage\quad\textbar\quad\textsc{The Impedance Threshold: Argonaut}}
\fancyhead[RO]{\small\textit{\leftmark}\quad\textbar\quad\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[C]{\small\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
}

% Chapter Title Styling
\titleformat{\chapter}[display]
  {\normalfont\filcenter}
  {\textsc{\Large Chapter \thechapter}}
  {1.2ex}
  {\Huge\bfseries}
\titlespacing*{\chapter}{0pt}{45pt}{35pt}

% Part Title Styling (Acts)
\titleformat{\part}[display]
  {\thispagestyle{empty}\normalfont\filcenter}
  {\textsc{\Large \thepart}}
  {2ex}
  {\Huge\bfseries}
\titlespacing*{\part}{0pt}{80pt}{40pt}

\newcommand{\sceneheader}[1]{%
  \par\vspace{1.8em}%
  {\noindent\centering\scshape\large #1\par}%
  \vspace{1.0em}%
  \noindent%
}

\newcommand{\dinkus}{%
  \par\vspace{1.2em}%
  {\noindent\centering{\large $\ast\quad\ast\quad\ast$}\par}%
  \vspace{1.2em}%
  \noindent%
}

\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}
\setlength{\tabcolsep}{2pt}}

\lstset{
  basicstyle=\ttfamily\scriptsize,
  breaklines=true,
  breakatwhitespace=false,
  columns=flexible,
  keepspaces=true,
  frame=single,
  frameround=tttt,
  rulecolor=\color{black!30},
  backgroundcolor=\color{black!3},
  xleftmargin=0.6em,
  xrightmargin=0.6em,
  showstringspaces=false
}

\providecommand{\pandocbounded}[1]{#1}
\begin{document}
"""

def generate_preamble(linespread=1.5680, inner_margin=1.050, outer_margin=0.917, top_margin=1.0215, bottom_margin=1.0215):
    p = PREAMBLE_TEMPLATE
    p = p.replace('__INNER__', f'{inner_margin:.3f}')
    p = p.replace('__OUTER__', f'{outer_margin:.3f}')
    p = p.replace('__TOP__', f'{top_margin:.3f}')
    p = p.replace('__BOTTOM__', f'{bottom_margin:.3f}')
    p = p.replace('__LINESPREAD__', f'{linespread:.4f}')
    return p

def preprocess_images(md_text):
    def repl(m):
        alt = m.group(1)
        src = m.group(2)
        base = os.path.basename(src)
        abs_path = os.path.join(ASSETS_DIR, base)
        return "\n\n```{=latex}\n\\begin{center}\\includegraphics[width=\\linewidth]{" + abs_path + "}\\end{center}\n```\n\n"
    return re.sub(r'!\[(.*?)\]\((.*?)\)', repl, md_text)

def md_to_latex(md_content):
    """Convert markdown to LaTeX using pandoc with listings enabled."""
    processed_md = preprocess_images(md_content)
    res = subprocess.run(
        ['pandoc', '-f', 'markdown', '-t', 'latex', '--listings'],
        input=processed_md,
        text=True,
        capture_output=True,
        check=True
    )
    return res.stdout

def clean_latex(latex_str, ch_title=""):
    """Clean pandoc LaTeX output for custom book format."""
    latex_str = re.sub(r'\\section\{.*?\}\s*(\\label\{.*?\})?', '', latex_str, flags=re.DOTALL)
    latex_str = re.sub(r'\\subsection\{(.*?)\}\s*(\\label\{.*?\})?', r'\\sceneheader{\1}', latex_str, flags=re.DOTALL)
    latex_str = re.sub(r'\\subsubsection\{(.*?)\}\s*(\\label\{.*?\})?', r'\\sceneheader{\1}', latex_str, flags=re.DOTALL)
    latex_str = re.sub(r'\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center\}', r'\\dinkus', latex_str)
    
    # Replace pandoc figure float with inline centered figure to guarantee zero margin bleed
    latex_str = re.sub(
        r'\\begin\{figure\}.*?\\includegraphics.*?\{(.*?)\}.*?\\end\{figure\}',
        r'\\begin{center}\\includegraphics[width=\\linewidth]{\1}\\end{center}',
        latex_str, flags=re.DOTALL
    )
    
    # Replace any leftover verbatim blocks with listings
    latex_str = re.sub(r'\\begin\{verbatim\}', r'\\begin{lstlisting}', latex_str)
    latex_str = re.sub(r'\\end\{verbatim\}', r'\\end{lstlisting}', latex_str)
    
    # Shrink longtables slightly so they never exceed textwidth
    latex_str = re.sub(r'\\begin\{longtable\}',
                       r'\\begingroup\\footnotesize\\setlength{\\tabcolsep}{2.5pt}\\begin{longtable}',
                       latex_str)
    latex_str = re.sub(r'\\end\{longtable\}', r'\\end{longtable}\\endgroup', latex_str)
    latex_str = latex_str.replace(r"\real{0.2000}", r"\real{0.1800}")
    latex_str = latex_str.replace(r"\real{0.3333}", r"\real{0.3000}")
    return latex_str.strip()

def build_pdf_with_params(linespread=1.5680, inner=1.050, outer=0.917, top=1.0215, bottom=1.0215):
    os.makedirs(BUILD_DIR, exist_ok=True)
    
    # Ensure assets symlink exists in build_pdf
    assets_symlink = os.path.join(BUILD_DIR, "assets")
    if not os.path.exists(assets_symlink):
        try:
            os.symlink(ASSETS_DIR, assets_symlink)
        except Exception:
            pass
            
    # Remove stale pdfs before compiling
    gen_pdf = os.path.join(BUILD_DIR, "book.pdf")
    if os.path.exists(gen_pdf):
        os.remove(gen_pdf)
    if os.path.exists(OUTPUT_PDF):
        os.remove(OUTPUT_PDF)
        
    tex_path = os.path.join(BUILD_DIR, "book.tex")
    preamble = generate_preamble(linespread=linespread, inner_margin=inner, outer_margin=outer, top_margin=top, bottom_margin=bottom)
    
    with open(tex_path, "w", encoding="utf-8") as out:
        out.write(preamble)
        
        # Front Matter
        out.write(r"""\frontmatter
\pagestyle{empty}

% Half Title
\begin{center}
\vspace*{70pt}
{\Huge\textsc{The Impedance Threshold}}\\[1.5em]
{\Large\textsc{Argonaut}}\\[2em]
{\normalsize\scshape A Novel of Relational Spaceflight \& First Life}\\[0.5em]
{\small\itshape Canonical Prequel to the Exospecies Survey Series}
\end{center}
\clearpage

% Title Page
\begin{center}
\vspace*{60pt}
{\Huge\bfseries THE IMPEDANCE THRESHOLD}\\[1.0em]
{\Large\bfseries ARGONAUT}\\[1.8em]
{\large\scshape A Novel of Relational Spaceflight \& First Life}\\[3.5em]
{\Large TODD HENDRIXX}\\[1.0em]
{\normalsize\itshape In Collaboration with Dr. Ryan Vance}\\[5.0em]
{\small\scshape Sol Navigation Directorate $\cdot$ Lunar Gateway Press}\\[0.4em]
{\scriptsize\textsf{Cislunar Base 1 $\cdot$ Mare Tranquillitatis $\cdot$ 2058 / 2450 AD}}
\end{center}
\clearpage

% Copyright & Cataloging
\begin{flushleft}
\footnotesize
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.8em}
\textsc{The Impedance Threshold: Argonaut}\\[0.5em]
Copyright \copyright\ 2026 Todd Hendrixx. All rights reserved.\\[0.8em]
Published by Lunar Gateway Press in cooperation with the Sol Navigation Directorate
and the Interstellar Astrobiological Survey (IAS).\\[0.8em]
Standard Book Number (ISBN): 978-0-988414-04-8 (Hardcover / Trade Paperback)\\
Electronic Publication (EPUB): 978-0-988414-05-5\\
Library of Congress Control Number: 2026938411\\[0.8em]
Set in 12pt Georgia with mathematical typesetting in AMS/Computer Modern.
Aerospace telemetry and state matrices typeset in Menlo.
Book design and astrodynamic trajectory verification by the author.\\[0.8em]
This novel is a work of hard science fiction set on an accelerated, alternate
timeline for the Artemis program and Lunar Gateway. Established physics in the text,
including orbital mechanics, pulsar timing, Montgomery's shape sphere and the
cosmological observations, is presented as accurately as the author could make it.
Quantum Relational Causality (QRC) is the author's own speculative research program;
where the story reaches beyond what that research has established, the characters say so.
Characters and specific mission chronologies are diegetic constructs.\\[0.8em]
First Trade Paperback Printing: November 2026\\[0.5em]
Printed in Cislunar Orbit \& North America.
\end{flushleft}
\clearpage

% Epigraph
\vspace*{120pt}
\begin{quote}
\itshape
``Space is not an empty stage awaiting actors. Distance is the inferred measurement of causal impedance. Where there are no clocks, there is no time; where there are no relations, there is no metric. The universe does not stretch. We simply wake up to what is already connected.''\\[1.5em]
\hfill\upshape --- \textsc{Dr. Ryan Vance}, \emph{Foundations of Relational Metrology} (2027)
\end{quote}
\clearpage

% Table of Contents
\pagestyle{fancy}
\tableofcontents
\cleardoublepage
""")

        # Process Front_Matter.md (Dramatis Personae & Preface)
        fm_path = os.path.join(MANUSCRIPT_DIR, "Front_Matter.md")
        if os.path.exists(fm_path):
            with open(fm_path, "r", encoding="utf-8") as f:
                fm_raw = f.read()
            fm_latex = md_to_latex(fm_raw)
            cleaned_fm = clean_latex(fm_latex, "Mission Registry & Dramatis Personae")
            out.write(r"\chapter*{Mission Registry \& Dramatis Personae}" + "\n")
            out.write(r"\markboth{Mission Registry \& Dramatis Personae}{Mission Registry \& Dramatis Personae}" + "\n")
            out.write(cleaned_fm)
            out.write("\n\n")

        # Main Matter
        out.write(r"""\mainmatter
\pagestyle{fancy}
""")

        current_act = 0
        for ch_num, ch_title, ch_file in CHAPTERS:
            if ch_num in ACT_HEADINGS:
                current_act += 1
                act_title, act_desc = ACT_HEADINGS[ch_num]
                out.write(f"\\cleardoublepage\n\\part{{{act_title}}}\n")
                out.write(f"\\begin{{center}}\\large\\itshape {act_desc}\\end{{center}}\n\\vspace*{{30pt}}\n")

            ch_path = os.path.join(MANUSCRIPT_DIR, ch_file)
            with open(ch_path, "r", encoding="utf-8") as cf:
                ch_raw = cf.read()

            ch_latex = md_to_latex(ch_raw)
            cleaned = clean_latex(ch_latex, ch_title)
            out.write(f"\\chapter{{{ch_title}}}\n")
            out.write(cleaned)
            out.write("\n\n")

            if ch_num in ACT_DOSSIERS:
                dossier_title, dossier_file = ACT_DOSSIERS[ch_num]
                dossier_title = dossier_title.replace('&', r'\&')
                dossier_path = os.path.join(MANUSCRIPT_DIR, dossier_file)
                if os.path.exists(dossier_path):
                    with open(dossier_path, "r", encoding="utf-8") as df:
                        d_raw = df.read()
                    d_latex = md_to_latex(d_raw)
                    cleaned_d = clean_latex(d_latex, dossier_title)
                    out.write(f"\\cleardoublepage\n\\chapter*{{{dossier_title}}}\n\\markboth{{{dossier_title}}}{{{dossier_title}}}\n")
                    out.write(cleaned_d)
                    out.write("\n\n")

        # Back Matter: Exhibits & Appendices
        out.write(r"""\backmatter
\cleardoublepage
\part{Diegetic Exhibits \& Mathematical Appendices}
""")
        exhibits_path = os.path.join(MANUSCRIPT_DIR, "Exhibits_and_Appendices.md")
        if os.path.exists(exhibits_path):
            with open(exhibits_path, "r", encoding="utf-8") as f:
                ex_raw = f.read()
            ex_latex = md_to_latex(ex_raw)
            cleaned_ex = clean_latex(ex_latex, "Diegetic Exhibits & Appendices")
            out.write(cleaned_ex)
            out.write("\n")

        # Colophon & Multi-Century Roadmap Note
        out.write(r"""
\clearpage
\thispagestyle{empty}
\vspace*{\fill}
\begin{center}
\textsc{A Note on the Chronology \& Multi-Century Roadmap}\\[0.8em]
{\footnotesize\itshape
\emph{The Impedance Threshold: Argonaut} by Todd Hendrixx is the foundational canonical prequel
to the \emph{Exospecies Survey} trilogy: \emph{The Entropy Ladder}, \emph{Zero Lux}, and \emph{Coronal Strike}.\\[0.8em]
The autonomous navigation breakthroughs of the 2020s to 2040s, and the research program of Quantum
Relational Causality (QRC) behind them, catalyzed a four-century technological campaign across the solar
system: establishing the Sol Navigation Grid, taming the magnetic pinch instabilities of D-$^3\text{He}$ fusion torches, and perfecting
isochoric cryo-stasis and epigenetic cellular rejuvenation. These compounding innovations enabled
humanity's first relativistic interstellar deep-survey starships to launch in the 25th century.\\[0.8em]
Typeset in 12pt Georgia with mathematical typesetting in \textsf{Computer Modern/AMS}
and aerospace telemetry in Menlo. Certified for the Sol Navigation Directorate
and the Interstellar Astrobiological Survey at Lunar Gateway.}
\end{center}
\vspace*{\fill}

\clearpage
\thispagestyle{empty}
\vspace*{\fill}
\begin{center}
{\scriptsize\textsf{Sol Navigation Directorate $\cdot$ Interstellar Astrobiological Survey $\cdot$ Lunar Gateway Press}}
\end{center}
\vspace*{\fill}

\clearpage
\thispagestyle{empty}
\hbox{}
""")

        out.write(r"\end{document}" + "\n")

    # Run xelatex twice
    for run in range(2):
        res = subprocess.run(
            ['xelatex', '-interaction=nonstopmode', 'book.tex'],
            cwd=BUILD_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

    if os.path.exists(gen_pdf):
        shutil.copy(gen_pdf, OUTPUT_PDF)
        reader = pypdf.PdfReader(OUTPUT_PDF)
        page_count = len(reader.pages)
        return page_count
    else:
        print("Error: book.pdf was not generated! Showing last 50 lines of log:")
        log_file = os.path.join(BUILD_DIR, "book.log")
        if os.path.exists(log_file):
            with open(log_file) as lf:
                lines = lf.readlines()
                print("".join(lines[-50:]))
        return 0

if __name__ == "__main__":
    linespread = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5680
    pages = build_pdf_with_params(linespread=linespread)
    print(f"Current compiled pages: {pages}")
