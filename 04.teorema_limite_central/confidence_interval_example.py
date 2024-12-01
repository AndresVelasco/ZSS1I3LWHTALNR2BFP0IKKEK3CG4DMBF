import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Datos iniciales
n_visitors = 500  # Número total de visitantes
n_conversions = 45  # Número de conversiones (compras)
conversion_rate = n_conversions / n_visitors  # Tasa de conversión observada

# Nivel de confianza original
confidence_level = 0.95
z = stats.norm.ppf(1 - (1 - confidence_level) / 2)  # Z para el nivel de confianza del 95%

# Error estándar
std_error = np.sqrt((conversion_rate * (1 - conversion_rate)) / n_visitors)
margin_of_error = z * std_error

# Intervalo de confianza original
ci_lower = conversion_rate - margin_of_error
ci_upper = conversion_rate + margin_of_error

print(f"Tasa de conversión observada: {conversion_rate:.4f}")
print(f"Intervalo de confianza del {confidence_level*100:.0f}%: [{ci_lower:.4f}, {ci_upper:.4f}]")

# 1) Calcular el tamaño de muestra necesario para dividir por 2 el ancho del intervalo
new_margin_of_error = margin_of_error / 2
new_n = n_visitors * 4  # Cuadruplicar el tamaño de la muestra
print(f"\nPara reducir el margen de error a la mitad, el nuevo tamaño de muestra requerido es: {new_n:.0f} visitantes.")

# 2) Calcular el nuevo nivel de confianza para dividir por 2 el ancho del intervalo sin cambiar el tamaño de muestra
new_z = z / 2  # El nuevo valor Z es la mitad del original
new_confidence_level = 2 * (stats.norm.cdf(new_z) - 0.5)  # Convertir Z en nivel de confianza

print(f"\nPara reducir el margen de error a la mitad con el mismo tamaño de muestra ({n_visitors}), el nuevo nivel de confianza sería: {new_confidence_level*100:.2f}%")

# Graficar los resultados iniciales
fig, ax = plt.subplots(figsize=(8, 6))

# Mostrar la tasa de conversión observada como un punto
ax.errorbar(1, conversion_rate, yerr=margin_of_error, fmt='o', color='red', label='Tasa de conversión observada')

# Agregar el intervalo de confianza original
ax.fill_between([0, 2], ci_lower, ci_upper, color='blue', alpha=0.2, label=f'IC del {confidence_level*100:.0f}%')

# Etiquetas
ax.set_xlim(0, 2)
ax.set_ylim(0, 0.2)
ax.set_xticks([])
ax.set_ylabel('Tasa de conversión')
ax.set_title(f'Intervalo de confianza para la tasa de conversión\n{confidence_level*100:.0f}% de confianza')

# Mostrar el gráfico
plt.legend()
plt.show()

# Gráfico 1: Amplitud del intervalo en función del tamaño de muestra
# Array con tamaños de muestra desde 500 hasta 10,000 en pasos de 100
sample_sizes = np.arange(500, 10001, 100)

# Lista para almacenar los anchos del intervalo de confianza
ci_widths_sample_size = []

# Calcular el ancho del intervalo de confianza para cada tamaño de muestra
for n in sample_sizes:
    # Error estándar para el tamaño de muestra actual
    std_error = np.sqrt((conversion_rate * (1 - conversion_rate)) / n)
    # Margen de error
    margin_of_error = z * std_error
    # Ancho del intervalo de confianza (2 * margen de error)
    ci_width = 2 * margin_of_error
    # Almacenar el ancho del intervalo
    ci_widths_sample_size.append(ci_width)

# Graficar el tamaño de muestra vs. ancho del intervalo de confianza
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, ci_widths_sample_size, color='blue', label=f'IC del {confidence_level*100:.0f}%')
plt.title('Ancho del intervalo de confianza en función del tamaño de muestra', fontsize=14)
plt.xlabel('Tamaño de muestra', fontsize=12)
plt.ylabel('Ancho del intervalo de confianza', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()

# Gráfico 2: Amplitud del intervalo en función del nivel de confianza
# Array con niveles de confianza desde 0.5 hasta 0.99
confidence_levels = np.arange(0.5, 0.991, 0.01)

# Lista para almacenar los anchos del intervalo de confianza
ci_widths_confidence = []

# Calcular el ancho del intervalo de confianza para cada nivel de confianza, fijando n=500
for cl in confidence_levels:
    # Z para el nivel de confianza actual
    z_cl = stats.norm.ppf(1 - (1 - cl) / 2)
    # Margen de error
    margin_of_error = z_cl * std_error
    # Ancho del intervalo de confianza (2 * margen de error)
    ci_width = 2 * margin_of_error
    # Almacenar el ancho del intervalo
    ci_widths_confidence.append(ci_width)

# Graficar el nivel de confianza vs. ancho del intervalo de confianza
plt.figure(figsize=(10, 6))
plt.plot(confidence_levels, ci_widths_confidence, color='green', label=f'Tamaño de muestra fijado en n=500')
plt.title('Ancho del intervalo de confianza en función del nivel de confianza', fontsize=14)
plt.xlabel('Nivel de confianza', fontsize=12)
plt.ylabel('Ancho del intervalo de confianza', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
