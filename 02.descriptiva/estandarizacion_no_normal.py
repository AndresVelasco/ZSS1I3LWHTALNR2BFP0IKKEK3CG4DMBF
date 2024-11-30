import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generar datos para una distribución log-normal (no normal)
media_log = 3.0  # Media en la escala logarítmica
sigma_log = 0.5  # Desviación estándar en la escala logarítmica
n = 10000  # Número de puntos de datos

# Generar la distribución log-normal original
datos_no_normales = np.random.lognormal(mean=media_log, sigma=sigma_log, size=n)

# Estandarizar los datos no normales
datos_estandarizados = (datos_no_normales - np.mean(datos_no_normales)) / np.std(datos_no_normales)

# Crear la gráfica
plt.figure(figsize=(12, 6))

# Graficar la distribución no normal original
plt.subplot(1, 2, 1)
plt.hist(datos_no_normales, bins=30, color='lightblue', edgecolor='black', density=True, alpha=0.7)
plt.title('Distribución No Normal Original (Log-normal)')
plt.xlabel('Valores')
plt.ylabel('Densidad')

# Superponer la curva de la distribución log-normal
x = np.linspace(min(datos_no_normales), max(datos_no_normales), 100)
pdf = stats.lognorm.pdf(x, s=sigma_log, scale=np.exp(media_log))
plt.plot(x, pdf, color='darkblue', linestyle='dashed', linewidth=1, label='Curva log-normal teórica')
plt.legend()

# Graficar la distribución estandarizada
plt.subplot(1, 2, 2)
plt.hist(datos_estandarizados, bins=30, color='salmon', edgecolor='black', density=True, alpha=0.7)
plt.title('Distribución Estandarizada (No Normal)')
plt.xlabel('Valores Z')
plt.ylabel('Densidad')

# Superponer la curva normal estándar para comparar
x_z = np.linspace(-3, 3, 100)
pdf_z = stats.norm.pdf(x_z)
plt.plot(x_z, pdf_z, color='darkred', linestyle='dashed', linewidth=1, label='Curva normal estándar')
plt.legend()

plt.tight_layout()
plt.show()
