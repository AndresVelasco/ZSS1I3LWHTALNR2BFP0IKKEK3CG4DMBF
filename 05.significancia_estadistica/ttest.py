import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos
#gasto_antes = np.array([120, 130, 150, 140, 135, 125, 160, 145, 155, 150])
#gasto_despues = np.array([125, 135, 155, 145, 140, 130, 165, 150, 160, 155])
gasto_antes = np.array([120, 130, 150, 140, 135, 125, 160, 145, 155, 150])
gasto_despues = np.array([124, 130, 150, 142, 137, 130, 158, 150, 160, 150])

# Cálculo de las diferencias
diferencias = gasto_despues - gasto_antes
media_dif = np.mean(diferencias)
std_dif = np.std(diferencias, ddof=1)  # ddof=1 para la desviación estándar muestral
n = len(diferencias)

# Estadístico t
t_stat = media_dif / (std_dif / np.sqrt(n))

# p-value para un test bilateral
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))

# Resultados
print("Resultados de la Prueba t para Datos Pareados:")
print(f"- Media de las diferencias: {media_dif:.2f}")
print(f"- Desviación estándar de las diferencias: {std_dif:.2f}")
print(f"- Estadístico t: {t_stat:.2f}")
print(f"- p-value (bilateral): {p_value:.4f}")

# Visualización de las diferencias
plt.figure(figsize=(8, 5))
plt.bar(range(1, n + 1), diferencias, color='skyblue', edgecolor='black')
plt.axhline(0, color='red', linestyle='--', label='Línea base (sin diferencia)')
plt.title('Diferencias en Gasto Antes y Después de la Campaña')
plt.xlabel('Cliente')
plt.ylabel('Diferencia en Gasto ($)')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
