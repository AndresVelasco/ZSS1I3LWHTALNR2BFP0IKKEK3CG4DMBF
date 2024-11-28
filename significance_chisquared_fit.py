import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Datos iniciales
categories = ['Electrónica', 'Ropa', 'Hogar']
observed_before = np.array([200, 150, 100])
observed_after = np.array([220, 160, 120])
total_visits_before = np.array([1000, 1000, 1000])
total_visits_after = np.array([1000, 1000, 1000])

# Cálculo del pooling (promedio ponderado de tasas de conversión)
total_purchases = observed_before + observed_after
total_visits = total_visits_before + total_visits_after
pooled_rates = total_purchases / total_visits

# Valores esperados bajo la hipótesis nula
expected_before = pooled_rates * total_visits_before
expected_after = pooled_rates * total_visits_after

# Chi-squared estadístico
chi_squared = np.sum((observed_before - expected_before) ** 2 / expected_before)

# Grados de libertad
df = (len(categories) - 1) * (2 - 1)  # (filas - 1) * (columnas - 1)

# Visualización de la curva chi-squared
x = np.linspace(0, 10, 500)
y = chi2.pdf(x, df)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f'Chi-squared PDF (df={df})', color='blue')
plt.axvline(chi_squared, color='red', linestyle='--', label=f'Chi-squared = {chi_squared:.2f}')
critical_value = chi2.ppf(0.95, df)
plt.axvline(critical_value, color='green', linestyle='--', label=f'Critical value (0.05): {critical_value:.2f}')
plt.fill_between(x, 0, y, where=(x >= critical_value), color='green', alpha=0.3, label='Rejection region (alpha=0.05)')

plt.title('Chi-squared Distribution and Test Statistic')
plt.xlabel('Chi-squared value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Mostrar resultados
chi_squared, critical_value, chi_squared < critical_value
