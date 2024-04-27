
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

ax.axhline(0, color='black')
ax.axvline(0, color='black')

ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()