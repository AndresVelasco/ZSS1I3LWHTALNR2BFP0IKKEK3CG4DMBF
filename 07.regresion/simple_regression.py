import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import statsmodels.api as sm
import statsmodels.formula.api as smf
from google.cloud import bigquery

# controlar si se utilizan datos random
use_random_data = True

# Comentado: Código para extraer datos de BigQuery (descomentar si se desea usar)
# from google.cloud import bigquery
# client = bigquery.Client()
# query = """SELECT column_x AS X, column_y AS Y FROM `your_project.your_dataset.your_table`"""
# query_job = client.query(query)
# data = query_job.to_dataframe()
# x = data['X']
# y = data['Y']

# Generar datos de prueba
if use_random_data:
    np.random.seed(42)
    n = 1000
    x = np.random.normal(loc=50, scale=10, size=n)
    y = 0.8 * x + np.random.normal(loc=0, scale=5, size=n)  # Correlación aproximada de 0.65
else:
    client = bigquery.Client()
    query = """
SELECT 
    --culmen_length_mm AS X, 
    --flipper_length_mm AS Y,
    body_mass_g AS X,
    flipper_length_mm AS Y
FROM `bigquery-public-data.ml_datasets.penguins`
    """
    query_job = client.query(query)
    data = query_job.to_dataframe()
    data = data.dropna()
    x = data['X']
    y = data['Y']

# Visualización inicial: histogramas
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(x, bins=30, alpha=0.7, color='blue', label='Variable X')
plt.axvline(np.mean(x), color='red', linestyle='--', label='Media X')
plt.title('Histograma de X')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(y, bins=30, alpha=0.7, color='green', label='Variable Y')
plt.axvline(np.mean(y), color='red', linestyle='--', label='Media Y')
plt.title('Histograma de Y')
plt.legend()
plt.show()

# Scatterplot con línea de la media
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5, label='Datos')
plt.axvline(np.mean(x), color='blue', linestyle='--', label='Media X')
plt.axhline(np.mean(y), color='green', linestyle='--', label='Media Y')
plt.title('Scatterplot de X e Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Cálculo de regresión con scipy.stats.linregress
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Calcular RMSE y R-squared
predictions = slope * x + intercept
rmse = np.sqrt(np.mean((y - predictions) ** 2))
r_squared = r_value ** 2

# Cálculo general de R-squared sin suponer regresión lineal simple
ss_tot = np.sum((y - np.mean(y))**2)
ss_res = np.sum((y - predictions)**2)
r_squared_generic = 1 - (ss_res / ss_tot)

# Imprimir métricas
print(f"Resultados de la Regresión (scipy.stats.linregress):")
print(f"r: {r_value: .4f}")
print(f"Pendiente: {slope:.4f}")
print(f"Intercepto: {intercept:.4f}")
print(f"R-squared (scipy): {r_squared:.4f}")
print(f"R-squared (general): {r_squared_generic:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"p-value: {p_value:.4e}")

# Superponer línea de regresión al scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5, label='Datos')
plt.plot(x, predictions, color='red', label='Línea de Regresión')
plt.title('Scatterplot con Línea de Regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Regresión con statsmodels
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()

# Resumen del modelo
residuals = model.resid
rmse_statsmodels = np.sqrt(np.mean(residuals**2))
print(f"RMSE (statsmodels): {rmse_statsmodels:.4f}")
print(model.summary())


# Visualización de pruebas estadísticas
# Residuals plot
plt.figure(figsize=(8, 6))
plt.scatter(model.fittedvalues, model.resid, alpha=0.5)
plt.axhline(0, color='red', linestyle='--', label='Residual = 0')
plt.title('Gráfico de Residuos')
plt.xlabel('Valores Ajustados')
plt.ylabel('Residuos')
plt.legend()
plt.show()

# Q-Q plot para normalidad de residuos
sm.qqplot(model.resid, line='s')
plt.title('Gráfico Q-Q de los Residuos')
plt.show()

# Histogram of residuals
plt.figure(figsize=(8, 6))
plt.hist(model.resid, bins=30, alpha=0.7, color='purple', edgecolor='black')
plt.title('Histograma de los Residuos')
plt.xlabel('Residuos')
plt.ylabel('Frecuencia')
plt.axvline(0, color='red', linestyle='--', label='Media (0)')
plt.legend()
plt.show()

