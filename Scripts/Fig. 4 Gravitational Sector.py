import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(2.1, 15, 400)
r_s = 2.0 # 2GM / c^2 scale

# Temporal metric component g_00
g_00 = -(1.0 - r_s / r)

plt.figure(figsize=(8, 5))
plt.plot(r, g_00, label=r'$g_{00}(r) = -(1 - \frac{2GM}{c^2r})$', color='darkgreen', lw=2)
plt.axvline(r_s, color='red', ls='--', label='Event Horizon Scale ($r_s$)')
plt.title('Gravitational Sector: Temporal Metric Component $g_{00}$')
plt.xlabel('Radial Distance $r$')
plt.ylabel('$g_{00}$ Value')
plt.grid(True, ls=':')
plt.legend()
plt.tight_layout()
plt.show()
