import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Observed frequencies
observed = np.array([
    [120, 90, 40],  # Spain
    [200, 180, 70]  # Rest of the World
])

# Totals
row_totals = observed.sum(axis=1)
col_totals = observed.sum(axis=0)
grand_total = observed.sum()

# Expected frequencies
expected = np.outer(row_totals, col_totals) / grand_total

# Chi-squared statistic
chi_squared = ((observed - expected) ** 2 / expected).sum()

# Degrees of freedom
rows, cols = observed.shape
degrees_of_freedom = (rows - 1) * (cols - 1)

# Critical value and p-value
critical_value = stats.chi2.ppf(0.95, degrees_of_freedom)
p_value = 1 - stats.chi2.cdf(chi_squared, degrees_of_freedom)

# Results
print("Observed Frequencies:")
print(observed)
print("\nExpected Frequencies:")
print(expected)
print(f"\nChi-Squared Statistic: {chi_squared:.2f}")
print(f"Degrees of Freedom: {degrees_of_freedom}")
print(f"Critical Value (95%): {critical_value:.2f}")
print(f"P-Value: {p_value:.4f}")

# Visualization
x = np.linspace(0, 10, 500)
y = stats.chi2.pdf(x, degrees_of_freedom)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Chi-Squared Distribution (df=2)")
plt.axvline(critical_value, color='red', linestyle='--', label=f"Critical Value = {critical_value:.2f}")
plt.axvline(chi_squared, color='blue', linestyle='-', label=f"Chi-Squared = {chi_squared:.2f}")
plt.fill_between(x, 0, y, where=(x >= critical_value), color='red', alpha=0.3, label="Rejection Region")
plt.title("Chi-Squared Test of Homogeneity")
plt.xlabel("Chi-Squared Value")
plt.ylabel("Density")
plt.legend()
plt.show()
