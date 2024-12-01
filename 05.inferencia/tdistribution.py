import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

# Rango de valores para t
x = np.linspace(-4, 4, 500)

# Grados de libertad a comparar
df_values = [1, 5, 10, 30]

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Añadir las distribuciones t
for df in df_values:
    plt.plot(x, t.pdf(x, df), label=f't-distribution (df={df})')

# Añadir la distribución normal estándar
plt.plot(x, norm.pdf(x, 0, 1), label='Normal estándar', linestyle='--', color='black')

# Personalizar la gráfica
plt.title('Comparación: Distribución t y Normal Estándar', fontsize=14)
plt.xlabel('Valor t', fontsize=12)
plt.ylabel('Densidad de Probabilidad', fontsize=12)
plt.axhline(0, color='gray', linewidth=0.5)
plt.grid(alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()

# Mostrar la gráfica
plt.show()
