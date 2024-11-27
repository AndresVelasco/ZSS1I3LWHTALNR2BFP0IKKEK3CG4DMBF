import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos del A/B test
n_A, n_B = 1000, 1000  # Tamaños de las muestras
x_A, x_B = 40, 65      # Conversiones observadas
p_A, p_B = x_A / n_A, x_B / n_B  # Proporciones observadas

# Proporción agrupada (pooled proportion)
p_pooled = (x_A + x_B) / (n_A + n_B)

# Error estándar combinado
se_pooled = np.sqrt(p_pooled * (1 - p_pooled) * (1 / n_A + 1 / n_B))

# Estadístico Z
z = (p_B - p_A) / se_pooled

# p-value para un test bilateral
p_value_bilateral = 2 * (1 - stats.norm.cdf(abs(z)))

# p-value para un test unilateral (asumiendo p_B > p_A)
p_value_unilateral = 1 - stats.norm.cdf(z)

# Gráfica para test bilateral
x = np.linspace(-4, 4, 1000)  # Valores de Z
y = stats.norm.pdf(x, 0, 1)  # Distribución normal estándar

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Distribución normal estándar', color='blue')
plt.fill_between(x, y, where=(x <= -abs(z)) | (x >= abs(z)), color='red', alpha=0.3, label='Región crítica (Bilateral)')
plt.axvline(z, color='black', linestyle='--', label=f'Estadístico Z: {z:.2f}')
plt.title('Prueba A/B: Visualización del Estadístico Z (Test Bilateral)')
plt.xlabel('Valor Z')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Gráfica para test unilateral
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Distribución normal estándar', color='blue')
plt.fill_between(x, y, where=(x >= stats.norm.ppf(0.95)), color='red', alpha=0.3, label='Región crítica (Z > 1.645)')
plt.axvline(z, color='black', linestyle='--', label=f'Estadístico Z: {z:.2f}')
plt.title('Prueba A/B: Visualización del Estadístico Z (Test Unilateral)')
plt.xlabel('Valor Z')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Resultados
print(f"Resultados:")
print(f"- Estadístico Z: {z:.2f}")
print(f"- p-value (Test Bilateral): {p_value_bilateral:.4f}")
print(f"- p-value (Test Unilateral): {p_value_unilateral:.4f}")
