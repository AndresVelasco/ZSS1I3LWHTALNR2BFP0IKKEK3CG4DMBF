import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Simulate a population (e.g., normally distributed data)
np.random.seed(0)
population = np.random.normal(loc=50, scale=10, size=1000)  # Mean=50, SD=10

# Parameters
sample_size = 15  # Reduced sample size to increase variability
num_samples = 100
confidence_level = 0.95  # Keep a typical 95% confidence level

# Function to calculate the confidence interval
def calculate_ci(sample, confidence_level):
    mean = np.mean(sample)
    std_err = np.std(sample, ddof=1) / np.sqrt(len(sample))
    margin_of_error = stats.t.ppf((1 + confidence_level) / 2., len(sample) - 1) * std_err
    return mean - margin_of_error, mean + margin_of_error

# Collect the confidence intervals from multiple samples
c_is = []
sample_means = []
for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=False)
    lower, upper = calculate_ci(sample, confidence_level)
    c_is.append((lower, upper))
    sample_means.append(np.mean(sample))

# Convert to numpy arrays for easier handling
c_is = np.array(c_is)
sample_means = np.array(sample_means)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sample_means, label="Sample Mean", color='blue', alpha=0.6)
plt.errorbar(range(num_samples), sample_means, yerr=[sample_means - c_is[:, 0], c_is[:, 1] - sample_means],
             fmt='o', color='red', label="Confidence Interval", alpha=0.7)

# Plot the true population mean as a horizontal line
plt.axhline(y=np.mean(population), color='green', linestyle='--', label='True Mean (Population)')

plt.title(f'Confidence Intervals from Multiple Samples (Confidence Level: {confidence_level*100}%)')
plt.xlabel('Sample Index')
plt.ylabel('Sample Mean')
plt.legend()
plt.show()
