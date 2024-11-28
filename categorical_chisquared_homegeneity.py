import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Data: Visitors and Conversions by Traffic Source
traffic_sources = ["Organic", "Paid Ads", "Social Media"]
visitors = np.array([1000, 1200, 800])
conversions = np.array([120, 150, 90])
visitors = np.array([1000, 1200, 800])
conversions = np.array([120, 140, 60])

# Total visitors and conversions
total_visitors = np.sum(visitors)
total_conversions = np.sum(conversions)

# Overall conversion rate
overall_conversion_rate = total_conversions / total_visitors

# Expected conversions for each traffic source
expected_conversions = overall_conversion_rate * visitors

# Chi-squared statistic
chi_squared = np.sum((conversions - expected_conversions) ** 2 / expected_conversions)

# Degrees of freedom
df = len(traffic_sources) - 1

# Critical value at 0.05 significance level
critical_value = chi2.ppf(0.95, df)

# p-value
p_value = 1 - chi2.cdf(chi_squared, df)

# Visualization: Chi-squared PDF
x = np.linspace(0, 20, 500)
pdf_y = chi2.pdf(x, df)

plt.figure(figsize=(8, 5))
plt.plot(x, pdf_y, label=f'Chi-squared PDF (df={df})', color='blue')
plt.axvline(chi_squared, color='red', linestyle='--', label=f'Chi-squared = {chi_squared:.2f}')
plt.axvline(critical_value, color='green', linestyle='--', label=f'Critical value (0.05): {critical_value:.2f}')
plt.title('Chi-squared Test for Homogeneity')
plt.xlabel('Chi-squared value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Print results
print(f"Chi-squared value: {chi_squared:.2f}")
print(f"Critical value (0.05 level): {critical_value:.2f}")
print(f"p-value: {p_value:.4f}")
print(f"Conclusion: {'Reject H0' if chi_squared > critical_value else 'Fail to Reject H0'}")
