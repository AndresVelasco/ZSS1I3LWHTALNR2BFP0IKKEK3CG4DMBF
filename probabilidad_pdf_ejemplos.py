import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, lognorm

# Parámetros para las distribuciones
mu = 1  # Media de la normal
sigma = 0.5  # Desviación estándar de la normal

# Valores para Normal
x_normal = np.linspace(-1, 3, 500)
normal_pdf = norm.pdf(x_normal, mu, sigma)
normal_cdf = norm.cdf(x_normal, mu, sigma)

# Valores para Log-Normal
x_lognormal = np.linspace(0.01, 20, 500)
lognormal_pdf = lognorm.pdf(x_lognormal, s=sigma, scale=np.exp(mu))
lognormal_cdf = lognorm.cdf(x_lognormal, s=sigma, scale=np.exp(mu))

# Gráfico de PDF Normal
plt.figure(figsize=(10, 6))
plt.plot(x_normal, normal_pdf, label="PDF Normal", color="blue", linewidth=2)
plt.title("Distribución Normal - PDF", fontsize=14)
plt.xlabel("Valores", fontsize=12)
plt.ylabel("Densidad de Probabilidad", fontsize=12)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()

# Gráfico de CDF Normal
plt.figure(figsize=(10, 6))
plt.plot(x_normal, normal_cdf, label="CDF Normal", color="red", linewidth=2)
plt.title("Distribución Normal - CDF", fontsize=14)
plt.xlabel("Valores", fontsize=12)
plt.ylabel("Probabilidad Acumulada", fontsize=12)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()

# Gráfico de PDF Log-Normal
plt.figure(figsize=(10, 6))
plt.plot(x_lognormal, lognormal_pdf, label="PDF Log-Normal", color="green", linewidth=2)
plt.title("Distribución Log-Normal - PDF", fontsize=14)
plt.xlabel("Valores", fontsize=12)
plt.ylabel("Densidad de Probabilidad", fontsize=12)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()

# Gráfico de CDF Log-Normal
plt.figure(figsize=(10, 6))
plt.plot(x_lognormal, lognormal_cdf, label="CDF Log-Normal", color="orange", linewidth=2)
plt.title("Distribución Log-Normal - CDF", fontsize=14)
plt.xlabel("Valores", fontsize=12)
plt.ylabel("Probabilidad Acumulada", fontsize=12)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()
