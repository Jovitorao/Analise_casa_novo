import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4 * np.pi, 1000)

x_original = np.sin(t)
x_comprimido = np.sin(6 * t)
x_expandido = np.sin(t)

plt.figure(figsize=(10, 5))
plt.plot(t, x_original, label=r'$x(t) = \sin(2t)$ (Original)', linewidth=2)
#plt.plot(t, x_comprimido, label=r'$x_c(t) = \sin(6t)$ (Comprimido x3)', linestyle='--')
#plt.plot(t, x_expandido, label=r'$x_e(t) = \sin(t)$ (Expandido x2)', linestyle='-.')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.title('Efeito do Escalamento Temporal numa Senóide')
plt.xlabel('Tempo (t)')
plt.ylabel('Amplitude')
plt.xticks(
    [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.show()