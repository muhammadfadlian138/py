import numpy as np
import matplotlib.pyplot as plt

# Create a grid of X and Y coordinates
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# Calculate Z
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Draw the surface
ax.plot_surface(X, Y, Z)

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()