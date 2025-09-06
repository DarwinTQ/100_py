
import numpy as np
import matplotlib.pyplot as plt
nt = 1024
T = 2.0

t = np.linspace(-2 * T, 2 * T, nt)

f0 = 8 / T

ui = np.maximum(1 - np.abs(t / T), 0)

uq = 2 * np.maximum(1 - np.abs(t / T - 0.5), 0)

uicos = ui * np.cos(2 * np.pi * f0 * t)
uqsin = -uq * np.sin(2 * np.pi * f0 * t)

up = uicos + uqsin


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
fig.suptitle('Señales graficadas ', fontsize=16)

# Gráfica 1, 2 y 3: ui(t) 
ax1.plot(t, ui, color='b', linestyle='-', label='ui(t) ')
ax1.plot(t, uicos, color='c', alpha=0.8, label='uicos(t) = ui(t) * cos(ωt)')
ax1.set_title('Componente I y su Modulación')
ax1.set_ylabel('Amplitud')
ax1.grid(True)
ax1.legend() 

ax2.plot(t, uq, color='r', linestyle='-', label='uq(t) ')
ax2.plot(t, uqsin, color='m', alpha=0.8, label='uqsin(t) = -uq(t) * sin(ωt)')
ax2.set_title('Componente Q y su Modulación')
ax2.set_ylabel('Amplitud')
ax2.grid(True)
ax2.legend() 

ax3.plot(t, up, color='g', label='up(t) = uicos(t) + uqsin(t)')
ax3.set_title('Señal Modulada Final')
ax3.set_xlabel('Tiempo (t)')
ax3.set_ylabel('Amplitud')
ax3.grid(True)
ax3.legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()