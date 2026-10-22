import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = np.linspace(0.1, 5.0, 500)
g_s_sq = 1.0
m_0 = 1.5
sigma_s = 0.8

# Cornell Potential: V(r) = - (g_s^2 / 4*pi*r) * exp(-m_0 * r) + sigma_s * r
V = - (g_s_sq / (4 * np.pi * r)) * np.exp(-m_0 * r) + sigma_s * r

plt.figure(figsize=(8, 5))
plt.plot(r, V, label=r'$V_{strong}(r)$', color='navy', lw=2)
plt.axhline(0, color='gray', ls='--')
plt.title('Strong Interaction Sector: Cornell-Type Potential')
plt.xlabel('Spatial Separation $r$')
plt.ylabel('Potential Energy $V(r)$')
plt.grid(True, ls=':')
plt.legend()
plt.tight_layout()
plt.show()
