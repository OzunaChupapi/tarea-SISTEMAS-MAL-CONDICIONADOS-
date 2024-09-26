import numpy as np
import matplotlib.pyplot as plt

# Definición de la matriz A
A = np.array([[1, 1, 1],
              [1, 1, 1.0001],
              [1, 1, 1]])

# Definición de los vectores b
b1 = np.array([1, 1.0001, 1])
b2 = np.array([1, 1.0002, 1])

# Resolver el sistema usando la pseudoinversa
x1 = np.linalg.pinv(A) @ b1
x2 = np.linalg.pinv(A) @ b2

# Crear una gráfica
plt.figure(figsize=(10, 6))

# Graficar la solución para b1
plt.scatter(x1[0], x1[1], color='blue', label='Solución para b1', s=100)
plt.text(x1[0], x1[1], f'  x1: {x1[0]:.4f}, x2: {x1[1]:.4f}', fontsize=12)

# Graficar la solución para b2
plt.scatter(x2[0], x2[1], color='red', label='Solución para b2', s=100)
plt.text(x2[0], x2[1], f'  x1: {x2[0]:.4f}, x2: {x2[1]:.4f}', fontsize=12)

# Configurar la gráfica
plt.title('Soluciones del Sistema Mal Condicionado')
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.xlim(-1, 2)
plt.ylim(-1, 2)
plt.legend()
plt.show()
