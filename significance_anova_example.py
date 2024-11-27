# Importar bibliotecas necesarias
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Configurar la semilla para reproducibilidad
np.random.seed(42)

# Crear los datos simulados
channels = ['Email', 'App', 'SMS']
n_customers_per_channel = 25

data = {
    "Customer_ID": np.arange(1, n_customers_per_channel * len(channels) + 1),
    "Channel": np.repeat(channels, n_customers_per_channel),
    "Spending": np.concatenate([
        np.random.normal(loc=120, scale=15, size=n_customers_per_channel),  # Email
        np.random.normal(loc=135, scale=20, size=n_customers_per_channel),  # App
        np.random.normal(loc=110, scale=10, size=n_customers_per_channel)   # SMS
    ])
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Visualizar la distribución de los datos por canal
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Channel", y="Spending", palette="Set2")
plt.title("Distribución del gasto por canal")
plt.xlabel("Canal")
plt.ylabel("Gasto")
plt.show()

# Separar los datos por canal
email = df[df["Channel"] == "Email"]["Spending"]
app = df[df["Channel"] == "App"]["Spending"]
sms = df[df["Channel"] == "SMS"]["Spending"]

# Realizar el análisis ANOVA
f_statistic, p_value = stats.f_oneway(email, app, sms)

# Mostrar los resultados
print("\nResultados del ANOVA:")
print(f"Estadístico F: {f_statistic:.2f}")
print(f"Valor p: {p_value:.4f}")

# Interpretación
alpha = 0.05
if p_value < alpha:
    print("\nConclusión: Hay diferencias significativas entre los canales (rechazamos H0).")
else:
    print("\nConclusión: No hay diferencias significativas entre los canales (no se rechaza H0).")

# Visualizar la distribución F
df_between = len(channels) - 1  # Grados de libertad entre grupos
df_within = len(data["Customer_ID"]) - len(channels)  # Grados de libertad dentro de los grupos

# Crear valores para la distribución F
x = np.linspace(0, 5, 500)  # Rango de valores F
y = stats.f.pdf(x, df_between, df_within)  # Función de densidad de probabilidad

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f"Distribución F ({df_between}, {df_within})", color="blue")
plt.axvline(f_statistic, color="red", linestyle="--", label=f"F calculado = {f_statistic:.2f}")
plt.title("Distribución F y valor calculado")
plt.xlabel("F")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.grid()
plt.show()

# Calcular la tabla clásica de ANOVA
k = len(channels)  # Número de grupos
N = len(data["Customer_ID"])  # Total de observaciones

# Grados de libertad
df_between = k - 1
df_within = N - k

# Sumas de cuadrados
grand_mean = df["Spending"].mean()
ss_between = sum(len(df[df["Channel"] == channel]) * (df[df["Channel"] == channel]["Spending"].mean() - grand_mean)**2 for channel in channels)
ss_within = sum(((df[df["Channel"] == channel]["Spending"] - df[df["Channel"] == channel]["Spending"].mean())**2).sum() for channel in channels)

# Promedios de cuadrados
ms_between = ss_between / df_between
ms_within = ss_within / df_within

# Estadístico F
calculated_f = ms_between / ms_within

# Crear la tabla
anova_table = pd.DataFrame({
    "Fuente de Variación": ["Entre grupos", "Dentro de los grupos", "Total"],
    "Suma de cuadrados (SS)": [ss_between, ss_within, ss_between + ss_within],
    "Grados de libertad (df)": [df_between, df_within, df_between + df_within],
    "Promedio de cuadrados (MS)": [ms_between, ms_within, None],
    "Estadístico F": [calculated_f, None, None]
})

# Mostrar resultados
print("\nResultados del ANOVA:")
print(f"Estadístico F: {f_statistic:.2f}")
print(f"Valor p: {p_value:.4f}")

print("\nTabla clásica de ANOVA:")
print(anova_table)

# Tukey HSD
tukey_result = pairwise_tukeyhsd(endog=data['Spending'], groups=data['Channel'], alpha=0.05)
print("\nResultados de Tukey HSD:")
print(tukey_result)

# Visualización de los intervalos de confianza de Tukey
fig = tukey_result.plot_simultaneous()
plt.title('Intervalos de Confianza (Tukey HSD)')
plt.show()

# Visualización adicional: Boxplot de gastos por canal
plt.figure(figsize=(8, 5))
df.boxplot(column='Spending', by='Channel', grid=False, showmeans=True, meanline=True)
plt.title('Distribución de Gastos por Canal')
plt.suptitle('')  # Quita el título general
plt.xlabel('Canal')
plt.ylabel('Gasto Promedio')
plt.show()
