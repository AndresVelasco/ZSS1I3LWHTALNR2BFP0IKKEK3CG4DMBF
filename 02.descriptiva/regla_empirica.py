import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Crear datos para una distribución normal estándar
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, loc=0, scale=1)  # PDF de una normal estándar (media=0, desviación estándar=1)

# Crear el gráfico de la curva normal estándar
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Curva Normal Estándar', color='blue')

# Colorear el área bajo la curva para 1 desviación estándar (34% de cada lado)
plt.fill_between(x, y, where=(x >= -1) & (x <= 1), color='skyblue', alpha=0.5, label='34% (1 desviación)')

# Colorear el área bajo la curva para 2 desviaciones estándar (95% total)
plt.fill_between(x, y, where=( x >= -2) & ( x < -1 ), color='lightgreen', alpha=0.5, label='95% (2 desviaciones)')
plt.fill_between(x, y, where=( x > 1 ) & ( x < 2 ), color='lightgreen', alpha=0.5, label='95% (2 desviaciones)')

# Colorear el área bajo la curva para 3 desviaciones estándar (99.7% total)
plt.fill_between(x, y, where=(x >= -3) & ( x < -2), color='lightcoral', alpha=0.5, label='99.7% (3 desviaciones)')
plt.fill_between(x, y, where=(x > 2) & ( x <= 3 ), color='lightcoral', alpha=0.5, label='99.7% (3 desviaciones)')

# Dibujar las líneas verticales en 1, 2, y 3 desviaciones estándar
plt.axvline(x=1, color='red', linestyle='--')
plt.axvline(x=-1, color='red', linestyle='--')
plt.axvline(x=2, color='green', linestyle='--')
plt.axvline(x=-2, color='green', linestyle='--')
plt.axvline(x=3, color='orange', linestyle='--')
plt.axvline(x=-3, color='orange', linestyle='--')

# Añadir título y etiquetas
plt.title('Curva Normal Estándar con Áreas Representando el 34%, 95% y 99.7%')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')

# Leyenda
plt.legend()

# Mostrar gráfico
plt.grid(True)
plt.show()
