import numpy as np
import matplotlib.pyplot as plt

# Generar datos para una distribución normal
media = 50  # Media de la distribución original
desviacion_estandar = 10  # Desviación estándar de la distribución original
n = 100000  # Número de puntos de datos

# Generar la distribución normal original
datos_originales = np.random.normal(loc=media, scale=desviacion_estandar, size=n)

# Estandarizar los datos
datos_estandarizados = (datos_originales - np.mean(datos_originales)) / np.std(datos_originales)

# Crear la gráfica
plt.figure(figsize=(12, 6))

# Graficar la distribución original
plt.subplot(1, 2, 1)
plt.hist(datos_originales, bins=30, color='skyblue', edgecolor='black', density=True, alpha=0.7)
plt.title('Distribución Normal Original')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.axvline(media, color='red', linestyle='dashed', linewidth=1, label=f'Media = {media}')
plt.axvline(media + desviacion_estandar, color='green', linestyle='dashed', linewidth=1, label=f'Media ± σ')
plt.axvline(media - desviacion_estandar, color='green', linestyle='dashed', linewidth=1)
plt.legend()

# Graficar la distribución estandarizada
plt.subplot(1, 2, 2)
plt.hist(datos_estandarizados, bins=30, color='lightcoral', edgecolor='black', density=True, alpha=0.7)
plt.title('Distribución Estandarizada')
plt.xlabel('Valores Z')
plt.ylabel('Densidad')
plt.axvline(0, color='red', linestyle='dashed', linewidth=1, label='Media = 0')
plt.axvline(1, color='green', linestyle='dashed', linewidth=1, label='Media ± 1σ')
plt.axvline(-1, color='green', linestyle='dashed', linewidth=1)
plt.legend()

plt.tight_layout()
plt.show()

