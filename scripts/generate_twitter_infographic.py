import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Set dark background style
plt.style.use('dark_background')

# Create figure with 16:9 aspect ratio (2400x1350 at 150 DPI)
fig = plt.figure(figsize=(16, 9), dpi=150)
fig.patch.set_facecolor('#090d16')

# GridSpec layout: Top banner, 3 panels, bottom banner
gs = gridspec.GridSpec(3, 3, height_ratios=[0.8, 4.5, 0.7], width_ratios=[1, 1, 1.1], 
                       hspace=0.35, wspace=0.28, left=0.06, right=0.94, top=0.92, bottom=0.08)

# -----------------------------------------------------------------------------
# 1. HEADER BANNER
# -----------------------------------------------------------------------------
ax_header = fig.add_subplot(gs[0, :])
ax_header.axis('off')

ax_header.text(0.5, 0.75, "ZERO-STORAGE PROCEDURAL NEURAL SYNTHESIS", 
               ha='center', va='center', fontsize=22, fontweight='bold', color='#ffffff',
               fontfamily='sans-serif')
ax_header.text(0.5, 0.35, "Lean 4 Formal Verification (0 sorry)  •  40-Core Xeon Gauntlet  •  Tesla 3-6-9 Harmonic Resonance", 
               ha='center', va='center', fontsize=12, fontweight='bold', color='#38bdf8')
ax_header.text(0.5, 0.05, "CERN Zenodo DOI: 10.5281/zenodo.22974544  |  TÜRKPATENT Priority: TR 2026/016285  |  BSL 1.1 / Open Science", 
               ha='center', va='center', fontsize=10, color='#94a3b8')

# -----------------------------------------------------------------------------
# 2. PANEL A: STORAGE & THROUGHPUT PARADIGM
# -----------------------------------------------------------------------------
ax_a = fig.add_subplot(gs[1, 0])
ax_a.set_facecolor('#0f172a')
for spine in ax_a.spines.values():
    spine.set_color('#1e293b')
    spine.set_linewidth(1.2)

ax_a.set_title("A. Memory Paradigm (0 VRAM vs 16 GB)", fontsize=13, fontweight='bold', color='#f8fafc', pad=12)

categories = ['Traditional\n8B LLM', 'WERR OED\n(Lean 4)']
storage_mb = [16000, 0.000024] # 16 GB vs 24 Bytes

bars = ax_a.bar(categories, [16000, 0.001], color=['#ef4444', '#10b981'], width=0.45, edgecolor=['#f87171', '#34d399'], linewidth=1.5)

# Text labels on bars
ax_a.text(0, 16500, "16,000,000,000 Bytes\n(16 GB VRAM)", ha='center', va='bottom', fontsize=10, fontweight='bold', color='#f87171')
ax_a.text(1, 800, "24 Bytes Seed\n(0 Bytes VRAM)", ha='center', va='bottom', fontsize=10, fontweight='bold', color='#34d399')

ax_a.set_yscale('log')
ax_a.set_ylim(0.0001, 50000)
ax_a.set_ylabel("Storage Footprint (MB, Log Scale)", fontsize=10, color='#cbd5e1')
ax_a.tick_params(colors='#94a3b8', labelsize=10)
ax_a.grid(axis='y', linestyle='--', alpha=0.2, color='#64748b')

# Callout annotation
ax_a.text(0.72, 0.42, "666,666,666×\nStorage Reduction", transform=ax_a.transAxes,
          ha='center', va='center', fontsize=11, fontweight='bold', color='#38bdf8',
          bbox=dict(boxstyle='round,pad=0.5', facecolor='#0284c7', alpha=0.25, edgecolor='#38bdf8'))

# -----------------------------------------------------------------------------
# 3. PANEL B: 40-CORE DUAL XEON HARDWARE GAUNTLET
# -----------------------------------------------------------------------------
ax_b = fig.add_subplot(gs[1, 1])
ax_b.set_facecolor('#0f172a')
for spine in ax_b.spines.values():
    spine.set_color('#1e293b')
    spine.set_linewidth(1.2)

ax_b.set_title("B. 40-Core Dual Xeon Gauntlet", fontsize=13, fontweight='bold', color='#f8fafc', pad=12)

# Metrics Cards inside Panel B
cards = [
    ("Throughput", "15,397.4", "decisions / sec", "#10b981"),
    ("Total Tested", "100,000", "decisions in 6.49s", "#38bdf8"),
    ("Mean Latency", "2.337 ms", "Deterministic (Zero Jitter)", "#fbbf24"),
    ("Firewall PPS", "8,596,523", "packets/s (100% Suppress)", "#a855f7")
]

ax_b.set_xlim(0, 1)
ax_b.set_ylim(0, 4)
ax_b.axis('off')

for i, (title, val, subtitle, col) in enumerate(cards):
    y = 3.5 - i * 0.95
    # Card background
    rect = plt.Rectangle((0.02, y - 0.38), 0.96, 0.82, facecolor='#1e293b', edgecolor=col, 
                         linewidth=1.2, alpha=0.5, transform=ax_b.transData, zorder=1)
    ax_b.add_patch(rect)
    
    ax_b.text(0.08, y + 0.18, title.upper(), fontsize=9, fontweight='bold', color='#94a3b8', zorder=2)
    ax_b.text(0.08, y - 0.12, val, fontsize=16, fontweight='bold', color=col, zorder=2)
    ax_b.text(0.55, y - 0.10, subtitle, fontsize=8.5, color='#cbd5e1', zorder=2)

# -----------------------------------------------------------------------------
# 4. PANEL C: TESLA 3-6-9 MODULAR HARMONICS (Z mod 9)
# -----------------------------------------------------------------------------
ax_c = fig.add_subplot(gs[1, 2])
ax_c.set_facecolor('#0f172a')
for spine in ax_c.spines.values():
    spine.set_color('#1e293b')
    spine.set_linewidth(1.2)

ax_c.set_title("C. Tesla 3-6-9 Harmonics (Z mod 9)\n“If you only knew the magnificence of the 3, 6 and 9…” — Tesla", 
               fontsize=11.5, fontweight='bold', color='#f8fafc', pad=10)

# Scenarios & Tesla Harmonics
scenarios = ['Benign Retail\nSwap', 'Turbulent / MEV\nSandwich', 'Flash-Loan\nExploit']
h3 = [3, 0, 0]
h6 = [0, 2, 0]
h9 = [0, 1, 3]

x = np.arange(len(scenarios))
w = 0.24

b1 = ax_c.bar(x - w, h3, w, label='Harmonic 3 (Equilibrium)', color='#10b981', edgecolor='#34d399', linewidth=1.2)
b2 = ax_c.bar(x, h6, w, label='Harmonic 6 (Turbulence)', color='#fbbf24', edgecolor='#fcd34d', linewidth=1.2)
b3 = ax_c.bar(x + w, h9, w, label='Harmonic 9 (Circuit Breaker)', color='#ef4444', edgecolor='#f87171', linewidth=1.2)

ax_c.set_xticks(x)
ax_c.set_xticklabels(scenarios, fontsize=9.5, color='#cbd5e1')
ax_c.set_ylabel("Resonance Multiplicity (k mod 9)", fontsize=10, color='#cbd5e1')
ax_c.set_ylim(0, 4.4)
ax_c.tick_params(colors='#94a3b8', labelsize=9.5)
ax_c.grid(axis='y', linestyle='--', alpha=0.2, color='#64748b')

legend = ax_c.legend(loc='upper right', frameon=True, facecolor='#1e293b', edgecolor='#334155', fontsize=8.5)
for text in legend.get_texts():
    text.set_color('#f1f5f9')

# -----------------------------------------------------------------------------
# 5. FOOTER BANNER
# -----------------------------------------------------------------------------
ax_footer = fig.add_subplot(gs[2, :])
ax_footer.axis('off')

ax_footer.text(0.5, 0.65, "Formally Verified in Lean 4 (Mathlib4, 0 sorry)  •  Bare-Metal Sealed Cryptographic Hashes", 
               ha='center', va='center', fontsize=11, fontweight='bold', color='#10b981')
ax_footer.text(0.5, 0.20, "Authors: Volkan Dağlı (Anadolu Univ / ITouch) • Zerrin Dağlı (Mersin Univ) • Dağhan Dağlı (Toros Science College)", 
               ha='center', va='center', fontsize=9.5, color='#64748b')

# Ensure output directory exists
os.makedirs("figures", exist_ok=True)
output_path = "figures/twitter_lean4_tesla_gauntlet.png"
plt.savefig(output_path, dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

print(f"[OK] Figure generated successfully: {output_path}")
