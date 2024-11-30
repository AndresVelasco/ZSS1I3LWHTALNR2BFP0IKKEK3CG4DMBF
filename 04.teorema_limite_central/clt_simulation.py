import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up for reproducibility
np.random.seed(42)

# Generate a skewed population: Exponential distribution simulating individual spending in an ecommerce
population_size = 100000
population_data = np.random.exponential(scale=50, size=population_size)  # mean spending ~50

# Sample sizes for demonstration (CLT effect on sample means)
sample_size = 100
n_samples = 1000

# Calculate sample means
sample_means = [np.mean(np.random.choice(population_data, sample_size)) for _ in range(n_samples)]

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot population distribution
sns.histplot(population_data, kde=True, color='skyblue', bins=50, ax=ax[0])
ax[0].set_title('Population Distribution (Skewed)')
ax[0].set_xlabel('Customer Spending')
ax[0].set_ylabel('Frequency')

# Plot distribution of sample means
sns.histplot(sample_means, kde=True, color='salmon', bins=30, ax=ax[1])
ax[1].set_title(f'Distribution of Sample Means (n={sample_size}, CLT)')
ax[1].set_xlabel('Sample Mean of Spending')
ax[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
