import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parámetros de la distribución binomial
N = 50         # Número de lanzamientos por experimento
p = 0.5        # Probabilidad de éxito (p)
experimentos = 10000  # Número de experimentos

# Simulación: número de éxitos en cada experimento
resultados = binom.rvs(N, p, size=experimentos)

# Histograma de la distribución binomial
plt.figure(figsize=(8, 6))
cuentas, bins, _ = plt.hist(resultados, bins=range(N+2), density=True, color="skyblue", edgecolor="black", alpha=0.7, label="Binomial")

# Parámetros para la aproximación normal
mu = N * p  # Media de la aproximación normal
sigma = np.sqrt(N * p * (1 - p))  # Desviación estándar de la aproximación normal

# Distribución normal (aproximación)
x = np.linspace(0, N, 100)  # Valores del eje X para la curva normal
y = norm.pdf(x, mu, sigma)  # Función de densidad de la normal

# Superponemos la aproximación normal
plt.plot(x, y, 'r-', lw=2, label='Aproximación Normal')

# Ajustamos los ticks del eje X para que solo se muestren de 5 en 5
plt.xticks(np.arange(0, N+1, 5))  # Valores de 5 en 5

# Etiquetas y título
plt.xlabel("Número de éxitos")
plt.ylabel("Densidad de probabilidad")
plt.title(f"Distribución Binomial vs Aproximación Normal\n{experimentos} experimentos de {N} lanzamientos (p = {p})")
plt.legend()

plt.show()

