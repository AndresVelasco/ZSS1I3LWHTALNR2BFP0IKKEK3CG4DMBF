import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Fijar la semilla para reproducibilidad
np.random.seed(42)

# Generar datos sintéticos de gasto en publicidad (en miles)
advertising_spend = np.random.uniform(50, 200, 100)  # Gasto entre $50k y $200k

# Definir una relación lineal con algo de ruido para los ingresos por ventas (en miles)
sales_revenue = 0.75 * advertising_spend + np.random.normal(0, 20, 100)  # Media = 0, Std = 20

# Crear un DataFrame
df = pd.DataFrame({
    'Advertising Spend (k$)': advertising_spend,
    'Sales Revenue (k$)': sales_revenue
})

# Calcular las medias de cada variable
mean_ad_spend = df['Advertising Spend (k$)'].mean()
mean_sales_revenue = df['Sales Revenue (k$)'].mean()

# 1. Calcular los coeficientes de regresión (a = pendiente, b = intercepto)
X = df['Advertising Spend (k$)']
Y = df['Sales Revenue (k$)']

#b, a = np.polyfit(X, Y, 1)
b, a, r_value, p_value, std_err = linregress(X, Y)

# 2. Calcular el coeficiente de correlación de Pearson
pearson_corr = np.corrcoef(X, Y)[0, 1]

# 3. Calcular las desviaciones estándar de X y Y
std_ad_spend = X.std()
std_sales_revenue = Y.std()

# Imprimir los valores calculados
print(f"Coeficientes de Regresión: b (pendiente) = {a:.4f}, a (intercepto) = {b:.4f}")
print(f"Coeficiente de Correlación de Pearson: {pearson_corr:.4f}")
print(f"Desviación Estándar del Gasto en Publicidad: {std_ad_spend:.4f}")
print(f"Desviación Estándar de los Ingresos por Ventas: {std_sales_revenue:.4f}")
print(f"Media del Gasto en Publicidad: {mean_ad_spend:.4f}")
print(f"Media de los Ingresos por Ventas: {mean_sales_revenue:.4f}")

# Configurar la figura y los ejes para los histogramas y el gráfico de dispersión
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Histograma para Gasto en Publicidad con línea de la media
ax[0].hist(df['Advertising Spend (k$)'], bins=15, color='green', alpha=0.7)
ax[0].axvline(mean_ad_spend, color='red', linestyle='--', linewidth=1.5, label=f'Media: {mean_ad_spend:.2f}')
ax[0].set_title('Histograma del Gasto en Publicidad')
ax[0].set_xlabel('Gasto en Publicidad (k$)')
ax[0].set_ylabel('Frecuencia')
ax[0].legend()
ax[0].grid(True)

# Histograma para Ingresos por Ventas con línea de la media
ax[1].hist(df['Sales Revenue (k$)'], bins=15, color='orange', alpha=0.7)
ax[1].axvline(mean_sales_revenue, color='red', linestyle='--', linewidth=1.5, label=f'Media: {mean_sales_revenue:.2f}')
ax[1].set_title('Histograma de Ingresos por Ventas')
ax[1].set_xlabel('Ingresos por Ventas (k$)')
ax[1].set_ylabel('Frecuencia')
ax[1].legend()
ax[1].grid(True)

# Gráfico de dispersión con línea de regresión y líneas de las medias
ax[2].scatter(df['Advertising Spend (k$)'], df['Sales Revenue (k$)'], color='blue', alpha=0.6)
ax[2].set_title('Dispersión Gasto en Publicidad vs. Ingresos por Ventas')
ax[2].set_xlabel('Gasto en Publicidad (k$)')
ax[2].set_ylabel('Ingresos por Ventas (k$)')
# Línea de regresión
ax[2].plot(df['Advertising Spend (k$)'], b * df['Advertising Spend (k$)'] + a, color='red', linestyle='--')
# Línea de la media del Gasto en Publicidad
ax[2].axvline(mean_ad_spend, color='green', linestyle='--', linewidth=1.5, label=f'Media Gasto: {mean_ad_spend:.2f}')
# Línea de la media de Ingresos por Ventas
ax[2].axhline(mean_sales_revenue, color='orange', linestyle='--', linewidth=1.5, label=f'Media Ingresos: {mean_sales_revenue:.2f}')
ax[2].legend()

# Mostrar los gráficos
plt.tight_layout()
plt.show()
