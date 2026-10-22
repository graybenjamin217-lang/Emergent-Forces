import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 1.0 / 137.036
E_core = np.linspace(0, 500, 400)
threshold = alpha * E_core

# Simulated shear work scaling with core energy
W_shear = 0.008 * E_core**1.05

plt.figure(figsize=(8, 5))
plt.plot(E_core, W_shear, label=r'Integrated Shear Work $W_{shear}$', color='crimson', lw=2)
plt.plot(E_core, threshold, label=r'Critical Threshold $\alpha E_{core}$', color='black', ls='--', lw=1.5)
plt.fill_between(E_core, threshold, W_shear, where=(W_shear >= threshold), color='crimson', alpha=0.15, label='Phase-Lock Rupture Zone')
plt.title('Weak Interaction Sector: Boundary Shearing Threshold')
plt.xlabel('Core Energy $E_{core}$')
plt.ylabel('Energy / Work')
plt.grid(True, ls=':')
plt.legend()
plt.tight_layout()
plt.show()
