import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
# Discrete point spectrum envelope anchored by dual-dilation operator D_k
envelope = np.exp(-0.2 * x**2)
spectrum_peaks = envelope * np.cos(5 * x)

plt.figure(figsize=(8, 5))
plt.plot(x, spectrum_peaks, label='Discrete Point Spectrum $\hat{D}_{k}$', color='purple', lw=1.5)
plt.plot(x, envelope, label='Topological Boundary Envelope $a$', color='orange', ls='--', lw=2)
plt.plot(x, -envelope, color='orange', ls='--', lw=2)
plt.title('Dual-Dilation Operator Domain & Spectral Cutoff')
plt.xlabel('Manifold Coordinate Space')
plt.ylabel('Operator Eigenvalue Response')
plt.grid(True, ls=':')
plt.legend()
plt.tight_layout()
plt.show()
