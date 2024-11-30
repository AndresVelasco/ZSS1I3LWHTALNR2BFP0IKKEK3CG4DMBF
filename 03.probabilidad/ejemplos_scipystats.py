import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros de la distribución normal
mu = 0  # Media
sigma = 1  # Desviación estándar

# Valores para graficar
x = np.linspace(-4, 4, 500)
pdf_values = norm.pdf(x, mu, sigma)
cdf_values = norm.cdf(x, mu, sigma)

# 1. Probabilidad acumulada para un valor x
x_value = 1.0
accumulated_prob = norm.cdf(x_value, mu, sigma)

# Gráfico de CDF con zona sombreada
plt.figure(figsize=(10, 6))
plt.plot(x, cdf_values, label="CDF (Normal)", color="orange", linewidth=2)
plt.fill_between(x, 0, norm.cdf(x, mu, sigma), where=(x <= x_value), color="orange", alpha=0.3)
plt.axvline(x=x_value, color="red", linestyle="--", label=f"x = {x_value}")
plt.title(f"Probabilidad Acumulada P(X ≤ {x_value}) = {accumulated_prob:.2%}", fontsize=14)
plt.xlabel("Valores", fontsize=12)
plt.ylabel("Probabilidad Acumulada", fontsize=12)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.show()

# 2. Inversa: calcular el valor x para una probabilidad acumulada dada
q = accumulated_prob  # Probabilidad acumulada deseada
inverse_x = norm.ppf(q, mu, sigma)

# Gráfico de PDF con zona sombreada
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_values, label="PDF (Normal)", color="green", linewidth=2)
plt.fill_between(x, 0, pdf_values, where=(x <= inverse_x), color="green", alpha=0.3)
plt.axvline(x=inverse_x, color="red", linestyle="--", label=f"x = {inverse_x:.2f}")
plt.title(f"Inversa de CDF: P(X ≤ x) = {q:.2%}, x = {inverse_x:.2f}", fontsize=14)
plt.xlabel("Valores", fontsize=12)
plt.ylabel("Densidad de Probabilidad", fontsize=12)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.show()
