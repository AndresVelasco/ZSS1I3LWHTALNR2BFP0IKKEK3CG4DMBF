import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo para los gráficos
sns.set(style="whitegrid")

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Generar datos para cada escenario de correlación
# 1. Correlación lineal positiva moderada
x1 = np.linspace(0, 10, 100)
y1 = 0.8 * x1 + np.random.normal(0, 1, 100)  # Ruido para correlación moderada

# 2. Correlación lineal negativa moderada
x2 = np.linspace(0, 10, 100)
y2 = -0.8 * x2 + np.random.normal(0, 1, 100)  # Ruido para correlación negativa moderada

# 3. Ausencia de correlación
x3 = np.linspace(0, 10, 100)
y3 = np.random.normal(0, 1, 100)  # Valores aleatorios sin relación con x

# 4. Correlación no lineal (cuadrática)
x4 = np.linspace(0, 10, 100)
y4 = 0.5 * (x4 - 5) ** 2 + np.random.normal(0, 1, 100)  # Relación cuadrática con ruido

# Creación de subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico de correlación lineal positiva moderada
axs[0, 0].scatter(x1, y1, color='b', alpha=0.6)
axs[0, 0].set_title("Correlación Lineal Positiva Moderada")
axs[0, 0].set_xlabel("X")
axs[0, 0].set_ylabel("Y")

# Gráfico de correlación lineal negativa moderada
axs[0, 1].scatter(x2, y2, color='r', alpha=0.6)
axs[0, 1].set_title("Correlación Lineal Negativa Moderada")
axs[0, 1].set_xlabel("X")
axs[0, 1].set_ylabel("Y")

# Gráfico de ausencia de correlación
axs[1, 0].scatter(x3, y3, color='g', alpha=0.6)
axs[1, 0].set_title("Ausencia de Correlación")
axs[1, 0].set_xlabel("X")
axs[1, 0].set_ylabel("Y")

# Gráfico de correlación no lineal
axs[1, 1].scatter(x4, y4, color='purple', alpha=0.6)
axs[1, 1].set_title("Correlación No Lineal")
axs[1, 1].set_xlabel("X")
axs[1, 1].set_ylabel("Y")

# Mostrar los gráficos
plt.tight_layout()
plt.show()
