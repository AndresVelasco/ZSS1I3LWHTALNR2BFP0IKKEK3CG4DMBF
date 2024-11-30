import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parámetros de la distribución binomial
N = 10       # Número de lanzamientos en cada experimento
p = 0.5      # Probabilidad de que salga cara (moneda justa)
experimentos = 100000  # Número de experimentos

# Simulación: cuántas veces sale cara en cada experimento
resultados = binom.rvs(N, p, size=experimentos)

# Graficamos los resultados
plt.figure(figsize=(8, 6))
plt.hist(resultados, bins=range(N+2), color="skyblue", edgecolor="black", alpha=0.7)
plt.xlabel("Número de veces que sale cara")
plt.ylabel("Frecuencia")
plt.title(f"Distribución Binomial: {experimentos} experimentos de {N} lanzamientos")
plt.xticks(range(N+1))
plt.show()




