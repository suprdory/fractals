# %%
cmaps = ["inferno", "plasma", "magma", "cividis", "viridis"]
cmaps = [
    "flag",
    "prism",
    "ocean",
    "gist_earth",
    "terrain",
    "gist_stern",
    "gnuplot",
    "gnuplot2",
    "CMRmap",
    "cubehelix",
    "brg",
    "gist_rainbow",
    "rainbow",
    "jet",
    "turbo",
    "nipy_spectral",
    "gist_ncar",
]
cmaps = [
    "binary",
    "gist_yarg",
    "gist_gray",
    "gray",
    "bone",
    "pink",
    "spring",
    "summer",
    "autumn",
    "winter",
    "cool",
    "Wistia",
    "hot",
    "afmhot",
    "gist_heat",
    "copper",
]

import numpy as np
import matplotlib.pyplot as plt

# %%


def clifford(x, y, a=2, b=2, c=1, d=-1):
    x1 = np.sin(a * y) + c * np.cos(a * x)
    y1 = np.sin(b * x) + d * np.cos(b * y)
    return x1, y1


n = 5000000
x = np.tile(np.nan, n)
y = np.tile(np.nan, n)


tx = 0
x0 = 1
y0 = 0

x[0] = x0
y[0] = y0
for i in range(n - 1):
    x[i + 1], y[i + 1] = clifford(x[i], y[i])

# %%
scl = 2.5
res = 800
bins = np.linspace(-scl, scl, res)
c, bx, by = np.histogram2d(x, y, bins=bins)


# %%
fig, ax = plt.subplots(1, 1, facecolor="black", figsize=(10, 10), dpi=res/10,frameon=False)
ax.imshow(np.log(c + 1), cmap='binary')
ax.axis("off")

# %%

scl = 2.5
fig, ax = plt.subplots(1, 1, facecolor="black", figsize=(10, 10), dpi=100)
ax.plot(x, y, ".", ms=0.1, alpha=0.2)
ax.axis("off")
ax.set_ylim(-scl, scl)
ax.set_xlim(-scl, scl)
