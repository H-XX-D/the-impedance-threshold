import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 4.2), dpi=300)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#161b22')

# Draw test plot
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), color='#58a6ff', lw=1.5, label='QRC Wave')
ax.set_title('SOL NAVIGATION DIRECTORATE: TEST PLATE', color='#f0f6fc', fontsize=10, fontname='DejaVu Sans', pad=10)
ax.tick_params(colors='#8b949e', labelsize=8)
for spine in ax.spines.values():
    spine.set_color('#30363d')
ax.grid(True, color='#21262d', linestyle='--', lw=0.5)

plt.tight_layout()
plt.savefig('/Users/hendrixx./The_Impedance_Threshold/assets/test_plate.png', dpi=300, facecolor=fig.get_facecolor())
print("Test plate saved successfully.")
