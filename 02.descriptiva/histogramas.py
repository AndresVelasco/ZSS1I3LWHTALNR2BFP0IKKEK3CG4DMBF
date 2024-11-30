import numpy as np
import matplotlib.pyplot as plt

# 1. Aproximadamente normal
np.random.seed(42)
normal_data = np.random.normal(loc=50, scale=15, size=1000)

# 2. Cola larga con media baja (log-normal)
log_normal_data = np.random.lognormal(mean=50, sigma=0.75, size=1000)

# 3. Cola larga con bump a la derecha (mezcla con bump a la derecha)
# Combinamos una distribución normal (más baja) y una log-normal (con cola larga a la derecha)
bump_right_data = np.concatenate([np.random.normal(loc=50, scale=40, size=900),  # Propiedades más baratas
                                  np.random.normal(loc=200, scale=10, size=100)])  # Propiedades caras con cola larga

# Crear los histogramas
plt.figure(figsize=(15, 5))

# Histograma 1 - Aproximadamente normal
plt.subplot(1, 3, 1)
plt.hist(normal_data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histograma Aproximadamente Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# Histograma 2 - Cola larga (log-normal)
plt.subplot(1, 3, 2)
plt.hist(log_normal_data, bins=30, color='salmon', edgecolor='black')
plt.title('Histograma con Cola Larga')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# Histograma 3 - Cola larga con bump a la derecha (mezcla con bump a la derecha)
plt.subplot(1, 3, 3)
plt.hist(bump_right_data, bins=30, color='lightgreen', edgecolor='black')
plt.title('Histograma con Bump a la Derecha')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()
