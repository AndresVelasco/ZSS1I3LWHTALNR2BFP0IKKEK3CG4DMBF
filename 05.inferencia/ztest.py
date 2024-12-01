import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos
n = 1000           # Tamaño de la muestra
x = 32             # Número de éxitos observados
p_obs = x / n      # Proporción observada
p_0 = 0.025         # Tasa de conversión hipotética (poblacional bajo H0)

# Cálculo del error estándar
se = np.sqrt(p_0 * (1 - p_0) / n)

# Estadístico Z
z = (p_obs - p_0) / se

# p-value para un test bilateral
p_value_bilateral = 2 * (1 - stats.norm.cdf(abs(z)))

# p-value para un test unilateral (p_obs > p_0)
p_value_unilateral = 1 - stats.norm.cdf(z)

# Visualización para test bilateral
x_values = np.linspace(-4, 4, 1000)  # Valores de Z
y_values = stats.norm.pdf(x_values, 0, 1)  # Distribución normal estándar

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label='Distribución normal estándar', color='blue')
plt.fill_between(x_values, y_values, where=(x_values <= stats.norm.ppf(0.025)) | (x_values >= stats.norm.ppf(0.975)), color='red', alpha=0.3, label='Región crítica (Bilateral)')
plt.axvline(z, color='black', linestyle='--', label=f'Estadístico Z: {z:.2f}')
plt.title('Z-Test de Una Sola Muestra: Visualización del Estadístico Z (Test Bilateral)')
plt.xlabel('Valor Z')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Visualización para test unilateral
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label='Distribución normal estándar', color='blue')
plt.fill_between(x_values, y_values, where=(x_values >= stats.norm.ppf(0.95)), color='red', alpha=0.3, label='Región crítica (Z > 1.645)')
plt.axvline(z, color='black', linestyle='--', label=f'Estadístico Z: {z:.2f}')
plt.title('Z-Test de Una Sola Muestra: Visualización del Estadístico Z (Test Unilateral)')
plt.xlabel('Valor Z')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Resultados
print(f"Resultados del Z-Test de Una Sola Muestra:")
print(f"- Estadístico Z: {z:.2f}")
print(f"- p-value (Test Bilateral): {p_value_bilateral:.4f}")
print(f"- p-value (Test Unilateral): {p_value_unilateral:.4f}")
