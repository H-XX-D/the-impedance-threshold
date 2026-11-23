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

def setup_figure(title, doc_id, width=6.8, height=5.0, dpi=300):
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    fig.patch.set_facecolor('#ffffff')
    
    ax_bg = fig.add_axes([0, 0, 1, 1])
    ax_bg.axis('off')
    
    ax_bg.plot([0.03, 0.97, 0.97, 0.03, 0.03], [0.03, 0.03, 0.97, 0.97, 0.03], color='#0f172a', lw=1.2)
    ax_bg.plot([0.035, 0.965, 0.965, 0.035, 0.035], [0.035, 0.035, 0.965, 0.965, 0.035], color='#94a3b8', lw=0.5)
    
    ax_bg.add_patch(Rectangle((0.035, 0.915), 0.93, 0.05, facecolor='#0f172a', edgecolor='none'))
    ax_bg.text(0.05, 0.938, "SOL NAVIGATION DIRECTORATE // TECHNICAL PLATE", 
               color='#ffffff', fontsize=7.5, weight='bold', fontname='DejaVu Sans', va='center')
    ax_bg.text(0.95, 0.938, f"DOC: {doc_id}", 
               color='#94a3b8', fontsize=7.0, fontname='DejaVu Sans Mono', va='center', ha='right')
    
    ax_bg.add_patch(Rectangle((0.035, 0.035), 0.93, 0.035, facecolor='#f1f5f9', edgecolor='none'))
    ax_bg.text(0.05, 0.052, title.upper(), 
               color='#1e293b', fontsize=7.0, weight='bold', fontname='DejaVu Sans', va='center')
    ax_bg.text(0.95, 0.052, "STATUS: CERTIFIED FLIGHT RECORD", 
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
        y_pos -= 0.095
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_01_front_matter_architecture.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 01.")

# Plate 2: Dossier I - Pulsar Bench & Montgomery Shape Sphere
def make_plate_02():
    fig = setup_figure("PSR J0337+1715 Timing & Montgomery Shape Sphere", "QRC-GBO-0226")
    ax1 = fig.add_axes([0.08, 0.50, 0.40, 0.33])
    ax2 = fig.add_axes([0.55, 0.50, 0.38, 0.33])
    ax3 = fig.add_axes([0.08, 0.12, 0.85, 0.34])
    
    # Montgomery Shape Sphere S^2 (Equilateral L4/L5, Collinear Equator)
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    # 2D projection
    circle = plt.Circle((0, 0), 1.0, color='#f1f5f9', ec='#0f172a', lw=1.2)
    ax1.add_patch(circle)
    # Equator (collinear syzygies)
    ax1.plot([-1, 1], [0, 0], color='#dc2626', lw=1.2, ls='--', label='Syzygy Equator')
    ax1.scatter([0, 0], [0.85, -0.85], color='#0284c7', s=60, zorder=5)
    ax1.text(0.08, 0.85, "L4 (Lagrange +)", fontsize=6.5, color='#0284c7', weight='bold')
    ax1.text(0.08, -0.85, "L5 (Lagrange -)", fontsize=6.5, color='#0284c7', weight='bold')
    ax1.scatter([0], [0], color='#059669', s=40, zorder=5)
    ax1.text(0.08, 0.02, "Triple Collision", fontsize=6.0, color='#059669')
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title("Montgomery Shape Sphere S² Projection", fontsize=8, weight='bold', color='#0f172a')
    ax1.legend(loc='lower left', fontsize=6)
    
    # Timing Residuals across bands (P, L, S) showing zero dispersion
    bands = ['P-Band\n(820 MHz)', 'L-Band\n(1400 MHz)', 'S-Band\n(2100 MHz)']
    res_meas = [3.712, 3.711, 3.713]
    res_err = [0.024, 0.008, 0.012]
    ax2.errorbar(bands, res_meas, yerr=res_err, fmt='o', color='#0284c7', ecolor='#dc2626', elinewidth=1.5, capsize=4, markersize=6)
    ax2.axhline(3.712, color='#64748b', ls=':', lw=1, label='QRC Geometric Baseline (3.712 µs)')
    ax2.set_ylabel("Inferred Residual (µs)", fontsize=7, color='#1e293b')
    ax2.set_title("Multi-Frequency Residual Coherence", fontsize=8, weight='bold', color='#0f172a')
    ax2.tick_params(labelsize=6.5)
    ax2.grid(True, color='#e2e8f0', ls='--', lw=0.5)
    ax2.legend(fontsize=6, loc='lower right')
    
    # Specs Table
    ax3.axis('off')
    specs = [
        ("OBSERVATIONAL TARGET:", "PSR J0337+1715 (27,110 TOAs / 5.23 yr stream; hierarchical triple 1.6d / 327d)"),
        ("STREAM DATA TELEMETRY:", "246 instrumental anomalies scrubbed (187 pointing offsets, 40 plasma steps, 18 RFI bursts)"),
        ("TIMING MODEL & FIT:", "Archibald 1PN 3-body dynamics; zero unmodeled leakage (dipole residual < 0.25 µs @ 0.12σ)"),
        ("SHAPE COORDINATES:", "Mass-weighted Jacobi vectors ρ_1, ρ_2 normalized by moment of inertia I = Σ m_i r_i²"),
        ("ACHROMATIC RESIDUAL:", "Δt ∝ f^0 across 820, 1400, 2100 MHz (plasma dispersion Δt ∝ f^-2 ruled out)"),
    ]
    y_pos = 0.85
    for label, val in specs:
        ax3.text(0.02, y_pos, label, fontsize=6.8, weight='bold', color='#0f172a', fontname='DejaVu Sans Mono')
        ax3.text(0.38, y_pos, val, fontsize=6.8, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.17
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_02_dossier_1_pulsar_bench.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 02.")

# Plate 3: Dossier II - Artemis-7 Anomaly & Recovery
def make_plate_03():
    fig = setup_figure("Artemis-7 (Prometheus) Cislunar Anomaly & Autonomous Recovery", "ART-REC-0711")
    ax1 = fig.add_axes([0.08, 0.47, 0.42, 0.36])
    ax2 = fig.add_axes([0.55, 0.47, 0.38, 0.36])
    ax3 = fig.add_axes([0.08, 0.10, 0.85, 0.34])
    
    # Trajectory comparison (Hyperbolic escape vs QRC Invariant Manifold insertion)
    theta = np.linspace(-np.pi/2, np.pi/2, 100)
    r_moon = 1737.4  # km
    ax1.plot(r_moon * np.cos(theta), r_moon * np.sin(theta), color='#94a3b8', lw=1.5, label='Lunar Limb')
    ax1.fill_betweenx(r_moon * np.sin(theta), 0, r_moon * np.cos(theta), color='#f1f5f9')
    
    # Coast after the bad 28.8 m/s burn: perilune 38.5 km below the surface (impact)
    th_dead = np.linspace(np.pi/2, 0.18, 60)
    r_dead = 1737.4 - 38.5 + 900.0 * (th_dead / (np.pi/2))**2
    ax1.plot(r_dead * np.cos(th_dead), r_dead * np.sin(th_dead), color='#dc2626', lw=1.5, ls='--', label='Coast-lock path (impact)')
    ax1.scatter([1737.4 * np.cos(0.18)], [1737.4 * np.sin(0.18)], marker='x', color='#dc2626', s=40, zorder=6)
    
    # Recovery: signed takeover burn, 49.5 m/s, perilune 112.4 km
    th_rec = np.linspace(-np.pi/3, np.pi/2, 80)
    r_rec = 1849.8  # 1737.4 + 112.4 km
    ax1.plot(r_rec * np.cos(th_rec), r_rec * np.sin(th_rec), color='#059669', lw=2.0, label='Recovery burn (49.5 m/s)')
    ax1.scatter([r_rec * np.cos(0)], [0], color='#059669', s=50, zorder=5)
    ax1.text(r_rec * np.cos(0) + 100, 50, "Perilune\n112.4 km", fontsize=6.5, color='#059669', weight='bold')
    
    ax1.set_xlim(0, 4800)
    ax1.set_ylim(-1500, 2500)
    ax1.set_aspect('equal')
    ax1.set_title("Lunar Approach: Impact vs Recovery", fontsize=8, weight='bold', color='#0f172a')
    ax1.legend(loc='lower left', fontsize=6.0)
    ax1.axis('off')
    
    # Overconfidence: GEONS reported 3-sigma collapses while its real error jumps;
    # the square-root filter's 3-sigma stays honest. Minutes after 00:02 UTC.
    t_min = np.linspace(0, 300, 300)
    geons_sigma = 0.05 + 1.95 * np.exp(-t_min / 60.0)
    geons_err = np.where(t_min < 242, 1.0 + 0.004 * t_min, 221.8)
    sqrt_sigma = 1.5 + 0.02 * t_min
    ax2.plot(t_min, geons_sigma, color='#dc2626', lw=1.5, label='GEONS reported 3σ (collapsed)')
    ax2.plot(t_min, geons_err, color='#dc2626', lw=1.0, ls='--', label='GEONS actual error')
    ax2.plot(t_min, sqrt_sigma, color='#0284c7', lw=1.8, label='Square-root filter 3σ')
    ax2.axvline(242, color='#ea580c', ls=':', label='Phantom fix accepted (04:03:51)')
    ax2.set_yscale('log')
    ax2.set_xlabel("Minutes after 00:02 UTC", fontsize=7, color='#1e293b')
    ax2.set_ylabel("Position error / reported 3σ (km)", fontsize=7, color='#1e293b')
    ax2.set_title("Filter Honesty During the Blackout", fontsize=8, weight='bold', color='#0f172a')
    ax2.set_ylim(0.03, 500)
    ax2.tick_params(labelsize=6.5)
    ax2.grid(True, color='#e2e8f0', ls='--', lw=0.5)
    ax2.legend(fontsize=6.0, loc='upper left')
    
    # Event Log Table
    ax3.axis('off')
    events = [
        ("00:02:00 UTC", "SOLAR RADIO BURST", "Burst near new Moon swamps DSN receivers; commanding lost."),
        ("00:24:00 UTC", "PROTON EVENT", "Protons hit optical-nav and star-tracker detectors; noise spikes."),
        ("04:03:51 UTC", "NEGATIVE NIS ACCEPTED", "GEONS accepts a phantom 221.8 km jump; bad burn issued."),
        ("04:48:30 UTC", "SIGNED TAKEOVER", "Laser TAKEOVER: 49.5 m/s burn; perilune 112.4 km; CAPSTONE 58.7% tidal shear held."),
    ]
    y_pos = 0.85
    for t_str, ev_str, desc in events:
        ax3.text(0.02, y_pos, t_str, fontsize=6.5, weight='bold', color='#0284c7', fontname='DejaVu Sans Mono')
        ax3.text(0.20, y_pos, ev_str, fontsize=6.5, weight='bold', color='#0f172a', fontname='DejaVu Sans')
        ax3.text(0.48, y_pos, desc, fontsize=6.2, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.22
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_03_dossier_2_artemis_recovery.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 03.")

# Plate 4: Project ARGONAUT Jovian Radiation & Flight Plan
def make_plate_04():
    fig = setup_figure("Project ARGONAUT Jovian Radiation Profile & Mission Stages", "ARG-CDR-0933")
    ax1 = fig.add_axes([0.08, 0.47, 0.42, 0.36])
    ax2 = fig.add_axes([0.55, 0.47, 0.38, 0.36])
    ax3 = fig.add_axes([0.08, 0.10, 0.85, 0.34])
    
    # Radiation profile bar chart
    moons = ['Io\n(Inner)', 'Europa\n(Plume)', 'Ganymede\n(Mid)', 'Callisto\n(Depot)']
    doses = [3600.0, 540.0, 8.0, 0.01]
    colors = ['#dc2626', '#ea580c', '#eab308', '#059669']
    bars = ax1.bar(moons, doses, color=colors, width=0.55, edgecolor='#0f172a', lw=0.8)
    ax1.set_yscale('log')
    ax1.set_ylabel("Surface Dose Rate (rad/day)", fontsize=7, color='#1e293b')
    ax1.set_title("Jovian Trapped Radiation Environment", fontsize=8, weight='bold', color='#0f172a')
    ax1.tick_params(labelsize=6.5)
    ax1.grid(True, color='#e2e8f0', ls='--', lw=0.5, axis='y')
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval * 1.3, f"{yval:g}", ha='center', va='bottom', fontsize=6.5, weight='bold')
    
    # Skimmer Schematic Diagram
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title("Autonomous Skimmer Cross-Section", fontsize=8, weight='bold', color='#0f172a')
    # Hull
    ax2.add_patch(Rectangle((0.1, 0.35), 0.8, 0.3, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.2))
    # Aerogel collector
    ax2.add_patch(Rectangle((0.02, 0.40), 0.08, 0.2, facecolor='#38bdf8', edgecolor='#0284c7', lw=1.0))
    ax2.text(0.06, 0.65, "Aerogel\nCassette", fontsize=6, ha='center', color='#0284c7', weight='bold')
    # Canister 1 bay
    ax2.add_patch(Circle((0.5, 0.5), 0.12, facecolor='#e2e8f0', edgecolor='#dc2626', lw=1.2))
    ax2.text(0.5, 0.5, "Canister 1\nTi-6Al-4V", fontsize=5.5, ha='center', va='center', color='#dc2626', weight='bold')
    # Engine nozzle
    ax2.add_patch(Polygon([[0.9, 0.42], [1.05, 0.35], [1.05, 0.65], [0.9, 0.58]], facecolor='#64748b', edgecolor='#0f172a', lw=1.0))
    ax2.text(0.98, 0.5, "RCS", fontsize=6, ha='center', va='center', color='#ffffff', weight='bold')
    ax2.set_xlim(-0.05, 1.15)
    ax2.set_ylim(0.2, 0.8)
    
    # Mass & Trajectory Table
    ax3.axis('off')
    specs = [
        ("TOTAL LAUNCH MASS:", "42,180 kg depot with Skimmer, Return Stack and JOI module (SLS Block 2, Aug 2033)"),
        ("CALLISTO DEPOT INSERTION:", "June 2037 (nuclear-electric depot; Callisto surface dose about 0.01 rad/day)"),
        ("SKIMMER PLUME PASS:", "May 4, 2040: 50.2 km periapsis, 2,214 m/s relative velocity, 42 s through Plume #3"),
        ("RETURN STACK:", "4.80 km/s departure (Jan 20, 2041); 3.86 km/s Earth capture; 47 cold-gas firings"),
        ("LUNAR GATEWAY RECOVERY:", "September 27, 2043: captured in NRHO by Canadarm3; exterior kept behind clean cover."),
    ]
    y_pos = 0.85
    for label, val in specs:
        ax3.text(0.02, y_pos, label, fontsize=6.8, weight='bold', color='#0f172a', fontname='DejaVu Sans Mono')
        ax3.text(0.35, y_pos, val, fontsize=6.8, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.17
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_04_ch09_argonaut_flight_plan.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 04.")

# Plate 5: Dossier IV - Plume Flyby & 980-Day Ghost Run
def make_plate_05():
    fig = setup_figure("Europa Plume Encounter & 980-Day Autonomous Ghost Run", "ARG-ENC-1443")
    ax1 = fig.add_axes([0.08, 0.47, 0.42, 0.36])
    ax2 = fig.add_axes([0.55, 0.47, 0.38, 0.36])
    ax3 = fig.add_axes([0.08, 0.10, 0.85, 0.34])
    
    # Plume encounter density profile
    t_sec = np.linspace(-30, 30, 200)
    density = 7.5e8 * np.exp(-(t_sec/7.5)**2)  # H2O molecules per cm^3 (column ~1.5e16 cm^-2 over ~200 km)
    ax1.plot(t_sec, density / 1e8, color='#0284c7', lw=2.0, label='Cryo-Plume Density')
    ax1.axvspan(-21, 21, color='#e0f2fe', alpha=0.5, label='Aerogel Cassette Open')
    ax1.set_xlabel("Time from Periapsis (seconds)", fontsize=7, color='#1e293b')
    ax1.set_ylabel("Plume Density (x10⁸ molecules/cm³)", fontsize=7, color='#1e293b')
    ax1.set_title("Plume Ingress & Collection Profile", fontsize=8, weight='bold', color='#0f172a')
    ax1.tick_params(labelsize=6.5)
    ax1.grid(True, color='#e2e8f0', ls='--', lw=0.5)
    ax1.legend(fontsize=6.0, loc='upper right')
    
    # Cumulative delta-V across 980-day ghost run
    days = np.linspace(0, 980, 100)
    dv = 3.66 * (1.0 - np.exp(-days / 350.0)) / (1.0 - np.exp(-980.0 / 350.0))
    ax2.plot(days, dv, color='#059669', lw=1.8, label='Cumulative cold-gas Δv (m/s)')
    ax2.axhline(3.66, color='#64748b', ls=':', label='Cold-gas total: 3.66 m/s')
    ax2.set_xlabel("Cruise Flight Day", fontsize=7, color='#1e293b')
    ax2.set_ylabel("Expenditure (m/s)", fontsize=7, color='#1e293b')
    ax2.set_title("980-Day Cold-Gas Trim Ledger", fontsize=8, weight='bold', color='#0f172a')
    ax2.tick_params(labelsize=6.5)
    ax2.grid(True, color='#e2e8f0', ls='--', lw=0.5)
    ax2.legend(fontsize=6.0, loc='lower right')
    
    # Specs Table
    ax3.axis('off')
    specs = [
        ("PERIAPSIS ALTITUDE:", "50.2 km above the Europa ice shell (Manannán region plume)"),
        ("CAPTURE MATRIX:", "Graded silica aerogel (0.002 to 0.050 g/cm³); grains captured at 2.2 km/s"),
        ("HERMETIC CRYOGENIC SEAL:", "Fiber-laser seam weld; cassette at 71.4 K; leak < 1.2e-12 mbar L/s"),
        ("DEEP-SPACE GHOST RUN:", "Zero ground commands for 980 days; 2 autonomous main burns, 47 cold-gas firings"),
        ("TOTAL MASS BUDGET:", "Nitrogen: 0.85 kg of 2.0 kg used; 1.15 kg remaining at Gateway capture."),
    ]
    y_pos = 0.85
    for label, val in specs:
        ax3.text(0.02, y_pos, label, fontsize=6.8, weight='bold', color='#0f172a', fontname='DejaVu Sans Mono')
        ax3.text(0.35, y_pos, val, fontsize=6.8, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.17
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_05_dossier_4_plume_ghost_run.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 05.")

# Plate 6: Chapter 20 - The Entropy Ladder & Two-Tier Pregeometry
def make_plate_06():
    fig = setup_figure("The Thermodynamic Entropy Ladder & Two-Tier QRC Pregeometry", "ENT-LAD-2043")
    ax1 = fig.add_axes([0.08, 0.47, 0.42, 0.36])
    ax2 = fig.add_axes([0.55, 0.47, 0.38, 0.36])
    ax3 = fig.add_axes([0.08, 0.10, 0.85, 0.34])
    
    # Dissipation rate bar chart across Entropy Ladder levels
    levels = ['Level 0\nInorganic', 'Level 1\nAutotroph', 'Level 2\nMetazoan', 'Level 3\nNeural', 'Level 4\nTechno']
    rates = [1e-4, 2.5, 45.0, 850.0, 1.2e5]
    colors = ['#94a3b8', '#059669', '#0284c7', '#ea580c', '#dc2626']
    bars = ax1.bar(levels, rates, color=colors, width=0.55, edgecolor='#0f172a', lw=0.8)
    ax1.set_yscale('log')
    ax1.set_ylabel("Specific Dissipation (erg / s / g)", fontsize=7, color='#1e293b')
    ax1.set_title("Entropy Export Across Structural Tiers", fontsize=8, weight='bold', color='#0f172a')
    ax1.tick_params(labelsize=6.5)
    ax1.grid(True, color='#e2e8f0', ls='--', lw=0.5, axis='y')
    
    # Diagram of Causal Diamond Dissipation & Two-Tier Refractive Spacetime
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title("Two-Tier Pregeometry & Causal Diamond", fontsize=8, weight='bold', color='#0f172a')
    # Diamond
    ax2.add_patch(Polygon([[0.5, 0.85], [0.85, 0.5], [0.5, 0.15], [0.15, 0.5]], facecolor='#f8fafc', edgecolor='#0f172a', lw=1.2))
    # Interior coherent state
    ax2.add_patch(Circle((0.5, 0.5), 0.12, facecolor='#dcfce7', edgecolor='#059669', lw=1.0))
    ax2.text(0.5, 0.5, "Tier 1: Markov\nDiscrete State\n[E ≥ 0, 2√2]", fontsize=5.0, ha='center', va='center', color='#059669', weight='bold')
    # Arrows of entropy export
    ax2.annotate("", xy=(0.8, 0.7), xytext=(0.6, 0.58), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=1.5))
    ax2.annotate("", xy=(0.2, 0.7), xytext=(0.4, 0.58), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=1.5))
    ax2.text(0.5, 0.75, "dS/dt > 0 (Boundary Export)", fontsize=6.2, ha='center', color='#dc2626', weight='bold')
    ax2.text(0.5, 0.22, "Tier 2: Refractive Spacetime n(r) = 1 + 2GM/c²r\nZero Gravitons // Pure Transverse Tensor Waves (+, ×)", fontsize=5.2, ha='center', color='#0284c7', weight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    
    # Specs Table
    ax3.axis('off')
    specs = [
        ("TWO-TIER QRC PREGEOMETRY:", "Tier 1: Discrete Markov generator & sharp ground state; Tier 2: Emergent refractive spacetime"),
        ("REFRACTIVE METRIC n(r):", "Space behaves as optical medium; light bends via Fermat principle; no graviton quanta exist"),
        ("GRAVITATIONAL DYNAMICS:", "Continuous bound field to mass sources; accelerating masses emit transverse tensor waves (+ and ×)"),
        ("QUANTUM RECONCILIATION:", "Born rule Tr(ρE), Tsirelson bound 2√2; unimodular volume det(g)=-1 decouples vacuum energy Λ_eff=0"),
        ("ENTROPY LADDER RUNGS:", "Rung 0: Inorganic -> 1: Autotroph -> 2: Metazoan -> 3: Cognitive -> 4: Causal Impedance Threshold (c)"),
    ]
    y_pos = 0.85
    for label, val in specs:
        ax3.text(0.02, y_pos, label, fontsize=6.8, weight='bold', color='#0f172a', fontname='DejaVu Sans Mono')
        ax3.text(0.35, y_pos, val, fontsize=6.8, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.17
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_06_ch20_entropy_ladder.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 06.")

# Plate 7: Dossier V - The 400-Year Cascade & Daedalus Keel
def make_plate_07():
    fig = setup_figure("IAS Daedalus Architecture & 400-Year Technology Cascade", "IAS-048-D-KEEL")
    ax1 = fig.add_axes([0.08, 0.49, 0.85, 0.35])
    ax2 = fig.add_axes([0.08, 0.10, 0.85, 0.36])
    
    # Starship schematic (IAS Daedalus - 1.8 km overall length)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title("IAS Daedalus (Registry IAS-048-D) // 1.8 km Deep-Survey Hull", fontsize=8, weight='bold', color='#0f172a')
    
    # Forward Whipple Shield
    ax1.add_patch(Polygon([[0.05, 0.5], [0.18, 0.32], [0.18, 0.68]], facecolor='#334155', edgecolor='#0f172a', lw=1.2))
    ax1.text(0.12, 0.5, "Whipple\nShield", fontsize=5.5, color='#ffffff', ha='center', va='center', weight='bold')
    # Primary Bridge & Canister 1 shrine
    ax1.add_patch(Rectangle((0.18, 0.44), 0.08, 0.12, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.0))
    ax1.text(0.22, 0.5, "Bridge\n[Can. 1]", fontsize=5.0, color='#0284c7', ha='center', va='center', weight='bold')
    # Habitation Centrifuges
    ax1.add_patch(Circle((0.32, 0.5), 0.16, facecolor='none', edgecolor='#0284c7', lw=1.2, ls='--'))
    ax1.add_patch(Circle((0.32, 0.5), 0.05, facecolor='#64748b', edgecolor='#0f172a'))
    ax1.text(0.32, 0.72, "Grav-Rings (0.38g)", fontsize=5.5, color='#0284c7', ha='center', weight='bold')
    # Stasis Vaults (135 K isochoric vitrification)
    ax1.add_patch(Rectangle((0.38, 0.42), 0.12, 0.16, facecolor='#e0f2fe', edgecolor='#0284c7', lw=1.0))
    ax1.text(0.44, 0.5, "135K Stasis\nVaults", fontsize=5.0, color='#0369a1', ha='center', va='center', weight='bold')
    # Truss & Liquid Droplet Radiators
    ax1.add_patch(Rectangle((0.50, 0.47), 0.22, 0.06, facecolor='#64748b', edgecolor='#0f172a', lw=1.0))
    ax1.add_patch(Polygon([[0.54, 0.47], [0.68, 0.25], [0.70, 0.25], [0.56, 0.47]], facecolor='#ea580c', alpha=0.3, edgecolor='#ea580c', lw=0.8))
    ax1.add_patch(Polygon([[0.54, 0.53], [0.68, 0.75], [0.70, 0.75], [0.56, 0.53]], facecolor='#ea580c', alpha=0.3, edgecolor='#ea580c', lw=0.8))
    ax1.text(0.62, 0.80, "Liquid Droplet Radiators", fontsize=5.5, color='#ea580c', ha='center', weight='bold')
    # Fusion Torch Engine
    ax1.add_patch(Polygon([[0.72, 0.40], [0.88, 0.30], [0.88, 0.70], [0.72, 0.60]], facecolor='#1e293b', edgecolor='#0f172a', lw=1.2))
    ax1.text(0.80, 0.5, "D-³He Fusion\nTorch Engine", fontsize=5.5, color='#ffffff', ha='center', va='center', weight='bold')
    # Exhaust plume
    ax1.add_patch(Polygon([[0.88, 0.35], [0.98, 0.20], [0.98, 0.80], [0.88, 0.65]], facecolor='#38bdf8', alpha=0.4, edgecolor='none'))
    ax1.text(0.94, 0.5, "v_e ≈ 0.08c", fontsize=5.5, color='#0284c7', ha='center', va='center', weight='bold')
    
    ax1.set_xlim(0, 1.02)
    ax1.set_ylim(0.15, 0.85)
    
    # 400-Year Timeline Cascade Table
    ax2.axis('off')
    cascade = [
        ("EPOCH 1 (2024–2100):", "Relational Metrology: Pulsar Bench, Artemis-7, Project ARGONAUT, Sol Navigation Grid."),
        ("EPOCH 2 (2100–2250):", "Fusion Epoch: magnetic confinement tamed; D-³He torch drives, v_e ≈ 0.08c."),
        ("EPOCH 3 (2250–2400):", "Biogerontology & Stasis: Cyclic OSK rejuvenation (1,000-yr lifespan); 135 K isochoric stasis."),
        ("EPOCH 4 (2450+ AD):", "The Deep-Survey Era: IAS Daedalus commissions at Luna L2; 160-year voyage to Acheron-Prime."),
    ]
    y_pos = 0.85
    for epoch, desc in cascade:
        ax2.text(0.02, y_pos, epoch, fontsize=6.8, weight='bold', color='#0f172a', fontname='DejaVu Sans Mono')
        ax2.text(0.32, y_pos, desc, fontsize=6.8, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.22
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_07_dossier_5_daedalus_cascade.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 07.")

# Plate 8: Exhibits - Navigation Algorithm & State Flow
def make_plate_08():
    fig = setup_figure("Relational State Estimator & Autonomous Control Flow", "SNG-ALG-0402")
    ax1 = fig.add_axes([0.08, 0.45, 0.85, 0.39])
    ax2 = fig.add_axes([0.08, 0.10, 0.85, 0.32])
    
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title("Autonomous Relational Navigation Execution Pipeline", fontsize=8, weight='bold', color='#0f172a')
    
    # Draw block flowchart
    blocks = [
        (0.05, 0.45, 0.16, 0.25, "1. SENSORS\nOptical Fixes\nMoon Bearings, IMU"),
        (0.25, 0.45, 0.16, 0.25, "2. JACOBI STATE\n18-State\nRelational EKF"),
        (0.45, 0.45, 0.16, 0.25, "3. SQRT GATE\nNIS Test +\nReacquisition"),
        (0.65, 0.45, 0.16, 0.25, "4. QP PLANNER\n3 Channels Vote\n+ Diverse Verifier"),
        (0.85, 0.45, 0.13, 0.25, "5. JOURNAL\nPrepare, Then\nIssue Burn"),
    ]
    for x, y, w, h, text in blocks:
        ax1.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", facecolor='#f8fafc', edgecolor='#0f172a', lw=1.2))
        ax1.text(x + w/2.0, y + h/2.0, text, ha='center', va='center', fontsize=5.8, weight='bold', color='#1e293b')
        if x < 0.8:
            ax1.annotate("", xy=(x + w + 0.04, y + h/2.0), xytext=(x + w, y + h/2.0),
                         arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.5))
            
    ax1.set_xlim(0, 1.02)
    ax1.set_ylim(0.2, 0.8)
    
    # Algorithm Logic Table
    ax2.axis('off')
    specs = [
        ("STATE VECTOR:", "18 states: Moon rel. Earth; spacecraft and Sun rel. Earth-Moon barycenter (pos + vel)"),
        ("STREAM RESONANCES:", "LRO mascon periodic resonance 0.9757 @ 118.00 min (Lat -10°, Lon -11°) tracked"),
        ("SQUARE-ROOT UPDATE:", "S_k = L_S L_S^T from QR, never inverted; NIS = |L_S^-1 y_k|² ≥ 0 by construction"),
        ("FAULT ISOLATION (FDIR):", "NIS > 16.8 (6-dof, p=0.01): mark suspect, hold commit, begin causal reacquisition."),
    ]
    y_pos = 0.85
    for label, val in specs:
        ax2.text(0.02, y_pos, label, fontsize=6.8, weight='bold', color='#0f172a', fontname='DejaVu Sans Mono')
        ax2.text(0.35, y_pos, val, fontsize=6.8, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.22
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_08_exhibits_navigation_algorithm.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 08.")

# Plate 9: Exhibits - Canister 1 Qualification
def make_plate_09():
    fig = setup_figure("Canister 1 Cryogenic Laser Hermetic Seal Qualification", "BIO-QUAL-1801")
    ax1 = fig.add_axes([0.08, 0.47, 0.42, 0.36])
    ax2 = fig.add_axes([0.55, 0.47, 0.38, 0.36])
    ax3 = fig.add_axes([0.08, 0.10, 0.85, 0.34])
    
    # Thermal profile during laser weld
    t_sec = np.linspace(0, 60, 100)
    temp_weld = 40.0 + 1900.0 * np.exp(-((t_sec - 20)/4.0)**2)  # Weld pool, 1,940 K peak in a 0.4 mm zone
    temp_sample = 71.4 + 0.0 * t_sec  # Cassette core: no measurable change
    ax1.plot(t_sec, temp_weld, color='#dc2626', lw=1.5, label='Laser Weld Joint (K)')
    ax1.plot(t_sec, temp_sample, color='#0284c7', lw=2.0, label='Sample Core Temp (K)')
    ax1.set_yscale('log')
    ax1.axhline(76.4, color='#059669', ls=':', label='Curation red line (+5 K)')
    ax1.set_xlabel("Weld Execution Time (seconds)", fontsize=7, color='#1e293b')
    ax1.set_ylabel("Temperature (Kelvin)", fontsize=7, color='#1e293b')
    ax1.set_title("Thermal Dissipation During Hermetic Weld", fontsize=8, weight='bold', color='#0f172a')
    ax1.set_yscale('log')
    ax1.tick_params(labelsize=6.5)
    ax1.grid(True, color='#e2e8f0', ls='--', lw=0.5)
    ax1.legend(fontsize=6.0, loc='center right')
    
    # Cross-section schematic of Canister 1
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title("Canister 1 Ti-6Al-4V Cross-Section", fontsize=8, weight='bold', color='#0f172a')
    # Titanium wall
    ax2.add_patch(Rectangle((0.15, 0.2), 0.7, 0.6, facecolor='#f1f5f9', edgecolor='#0f172a', lw=1.2))
    # Aerogel sample chamber
    ax2.add_patch(Rectangle((0.25, 0.3), 0.5, 0.4, facecolor='#e0f2fe', edgecolor='#0284c7', lw=1.0))
    ax2.text(0.5, 0.5, "Silica Aerogel\nMatrix\n[Sample]", fontsize=6, color='#0369a1', ha='center', va='center', weight='bold')
    # Weld lip
    ax2.add_patch(Rectangle((0.15, 0.78), 0.7, 0.06, facecolor='#dc2626', edgecolor='#0f172a', lw=1.0))
    ax2.text(0.5, 0.81, "Fiber-Laser Seam Weld", fontsize=5.5, color='#ffffff', ha='center', va='center', weight='bold')
    ax2.set_xlim(0.05, 0.95)
    ax2.set_ylim(0.1, 0.9)
    
    # Specs Table
    ax3.axis('off')
    specs = [
        ("STRUCTURAL ALLOY:", "Titanium grade Ti-6Al-4V, electron-beam melted, ultra-high vacuum pre-baked"),
        ("VACUUM SEAL INTEGRITY:", "Helium mass spectrometry leak rate < 1.2 x 10^-12 mbar L/s (Ultra-High Vacuum standard)"),
        ("SAMPLE INTEGRITY ASSURANCE:", "Cassette core 71.4 K throughout weld (red line +5 K); chill block peaked at 46.6 K"),
        ("BIOLOGICAL RECOVERY:", "41 intact chemosynthetic autotroph cells extracted in Gateway Class-10 cleanroom (2043)"),
        ("HISTORICAL LINEAGE:", "Canister kept in Gateway quarantine; a prism from the guidance truss flies on IAS Daedalus."),
    ]
    y_pos = 0.85
    for label, val in specs:
        ax3.text(0.02, y_pos, label, fontsize=6.8, weight='bold', color='#0f172a', fontname='DejaVu Sans Mono')
        ax3.text(0.35, y_pos, val, fontsize=6.8, color='#334155', fontname='DejaVu Sans')
        y_pos -= 0.17
        
    fig.savefig(os.path.join(ASSETS_DIR, "plate_09_exhibits_canister_qualification.png"), dpi=300)
    plt.close(fig)
    print("Generated Plate 09.")

if __name__ == '__main__':
    make_plate_01()
    make_plate_02()
    make_plate_03()
    make_plate_04()
    make_plate_05()
    make_plate_06()
    make_plate_07()
    make_plate_08()
    make_plate_09()
    print("All 9 diegetic plates generated successfully.")
