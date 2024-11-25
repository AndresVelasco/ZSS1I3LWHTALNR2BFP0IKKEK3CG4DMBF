import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parameters for the normal distribution
mean = 50      # Mean of the distribution
std_dev = 10   # Standard deviation of the distribution
n_samples = 10000  # Number of data points to simulate

# Simulate normally distributed data
data = np.random.normal(loc=mean, scale=std_dev, size=n_samples)

# Plot the histogram of the simulated data
plt.figure(figsize=(8,6))
plt.hist(data, bins=30, density=True, edgecolor='black', alpha=0.7, label='True Data')

# Plot the normal distribution curve
xmin, xmax = plt.xlim()  # Get the limits of the x-axis from the histogram
x = np.linspace(xmin, xmax, 100)  # Generate 100 points between xmin and xmax
p = stats.norm.pdf(x, mean, std_dev)  # Get the probability density function of the normal distribution
plt.plot(x, p, 'r', linewidth=2, label='Normal Distribution')

# Add title and labels
plt.title('Histogram with Normal Distribution Curve')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
