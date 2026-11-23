#!/usr/bin/env python3
"""
Generates high-resolution diegetic technical plates for THE IMPEDANCE THRESHOLD.
Eliminates margin bleeds by replacing wide ASCII/verbatim blocks with crisp,
publication-grade aerospace engineering diagrams.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle, Arrow
import matplotlib.patches as mpatches

ASSETS_DIR = "/Users/hendrixx./The_Impedance_Threshold/assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def setup_figure(title, doc_id, width=7.0, height=5.2, dpi=300):
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    fig.patch.set_facecolor('#ffffff')
    
    # Outer border and header
    ax_bg = fig.add_axes([0, 0, 1, 1])
    ax_bg.axis('off')
    
    # Draw engineering border
    ax_bg.plot([0.03, 0.97, 0.97, 0.03, 0.03], [0.03, 0.03, 0.97, 0.97, 0.03], color='#0f172a', lw=1.2)
    ax_bg.plot([0.035, 0.965, 0.965, 0.035, 0.035], [0.035, 0.035, 0.965, 0.965, 0.035], color='#94a3b8', lw=0.5)
    
    # Top banner
    ax_bg.add_patch(Rectangle((0.035, 0.915), 0.93, 0.05, facecolor='#0f172a', edgecolor='none'))
    ax_bg.text(0.05, 0.938, "SOL NAVIGATION DIRECTORATE // AEROSPACE TECHNICAL PLATE", 
               color='#ffffff', fontsize=7.5, weight='bold', fontname='DejaVu Sans', va='center')
    ax_bg.text(0.95, 0.938, f"DOC: {doc_id}", 
               color='#94a3b8', fontsize=7.0, fontname='DejaVu Sans Mono', va='center', ha='right')
    
    # Bottom banner
    ax_bg.add_patch(Rectangle((0.035, 0.035), 0.93, 0.035, facecolor='#f1f5f9', edgecolor='none'))
    ax_bg.text(0.05, 0.052, title.upper(), 
               color='#1e293b', fontsize=7.0, weight='bold', fontname='DejaVu Sans', va='center')
    ax_bg.text(0.95, 0.052, "CLASSIFICATION: DECLASSIFIED FLIGHT RECORD", 
               color='#64748b', fontsize=6.5, fontname='DejaVu Sans Mono', va='center', ha='right')
    
    return fig

# -------------------------------------------------------------
# Plate 1: Front Matter - Master Architecture Card
# -------------------------------------------------------------
def make_plate_01():
    fig = setup_figure("Project ARGONAUT & Sol Navigation Architecture", "ARG-ARCH-2033", width=6.8, height=5.2)
    
    # Grid of subplots
    ax1 = fig.add_axes([0.07, 0.50, 0.40, 0.33])
    ax2 = fig.add_axes([0.53, 0.50, 0.40, 0.33])
    ax3 = fig.add_axes([0.07, 0.12, 0.86, 0.34])
    
    # Plot 1: Jovian System Trajectory
    theta = np.linspace(0, 2*np.pi, 200)
    ax1.plot(1.8*np.cos(theta), 1.8*np.sin(theta), color='#94a3b8', lw=0.8, ls='--', label='Callisto (Depot)')
    ax1.plot(1.0*np.cos(theta), 1.0*np.sin(theta), color='#38bdf8', lw=1.0, ls='-', label='Europa (Plume)')
    # Skimmer dive
    r_dive = np.linspace(1.8, 1.0, 50)
    th_dive = np.linspace(0, np.pi*1.2, 50)
    ax1.plot(r_dive*np.cos(th_dive), r_dive*np.sin(th_dive), color='#dc2626', lw=1.5, label='Skimmer Dive')
    ax1.scatter([0], [0], color='#ea580c', s=120, label='Jupiter')
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.legend(loc='lower left', fontsize=6.5, frameon=True, framealpha=0.9)
    ax1.set_title("Jovian Trajectory Architecture", fontsize=8, weight='bold', color='#0f172a', pad=4)
    
    # Plot 2: 980-Day Ghost Run Heliocentric Transfer
    th_h = np.linspace(0, 1.4*np.pi, 100)
    r_h = np.linspace(5.2, 1.0, 100)
    ax2.plot(r_h*np.cos(th_h), r_h*np.sin(th_h), color='#0284c7', lw=1.5, label='Heliocentric Return')
    ax2.scatter([5.2*np.cos(0)], [0], color='#ea580c', s=50, label='Jupiter Egress')
    ax2.scatter([1.0*np.cos(1.4*np.pi)], [1.0*np.sin(1.4*np.pi)], color='#059669', s=50, label='Lunar Gateway')
    ax2.scatter([0], [0], color='#eab308', s=100, label='Sun')
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.legend(loc='lower right', fontsize=6.5, frameon=True, framealpha=0.9)
    ax2.set_title("980-Day Ghost Run Transfer", fontsize=8, weight='bold', color='#0f172a', pad=4)
    
    # Table / Specs in ax3
    ax3.axis('off')
    specs = [
        ("MISSION LIFESPAN:", "2026 – 2058 (Pulsar Bench to Multi-Century IAS Transition)"),
        ("PRIMARY TARGET:", "Europa (Jupiter II) Plume #3, Manannán region"),
        ("MOTHERSHIP DEPOT:", "Callisto Carrier Depot (nuclear-electric; low-radiation haven)"),
        ("PLUME PASS:", "Autonomous Europa Skimmer (50.2 km periapsis @ 2,214 m/s, May 4, 2040)"),
        ("SAMPLE RECEPTACLE:", "Canister 1 (10 kg Ti-6Al-4V, fiber-laser sealed, cassette near 71 K)"),
        ("INTERPLANETARY RUN:", "980-day ghost run, Jan 2041 to Sep 2043 (2 main burns, 47 cold-gas firings)"),
        ("GUIDANCE CORE:", "18-state Jacobi navigation, QP planner, verifier; X-ray pulsars in deep space"),
        ("CAPTURE FACILITY:", "Lunar Gateway Station (Near-Rectilinear Halo Orbit, 9:2 Resonance)"),
        ("ASTROBIOLOGY RESULT:", "Chemosynthetic Autotrophic Genesis: 'Life is Simple.'"),
    ]
    y_pos = 0.90
    for label, val in specs:
        ax3.text(0.02, y_pos, label, fontsize=7.0, weight='bold', color='#0f172a', fontname='DejaVu Sans Mono')
        ax3.text(0.35, y_pos, val, fontsize=7.0, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.105
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_01_front_matter_architecture.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 01.")

make_plate_01()
