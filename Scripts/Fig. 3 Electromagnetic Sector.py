import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-3, 3, 400)
rho = np.linspace(0.1, 3, 400)
Z, RHO = np.meshgrid(z, rho)
v0 = 10.0
a = 1.0

# Axial velocity profile magnitude
v_axial = v0 * (a**2) / (RHO**2 + Z**2)

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(Z, RHO, v_axial, cmap='viridis', edgecolor='none', alpha=0.9)
fig.colorbar(surf, shrink=0.5, aspect=10, label='Velocity Magnitude')
ax.set_title('Electromagnetic Sector: Polar Discharge Velocity Field')
ax.set_xlabel('Axis $z$')
ax.set_ylabel(r'Radius $\rho$')
ax.set_zlabel('Velocity $v_{axial}$')
plt.tight_layout()
plt.show()
