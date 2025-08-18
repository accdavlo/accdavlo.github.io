import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Number of samples
N = 10000

titles=False

# Draw samples from Beta(1.5, 2)
mu_samples = beta.rvs(1.5, 2, size=N)

# Compute function values
f_samples = 10 + np.sin(2 * np.pi * mu_samples)

# Create the figure
fig, axes = plt.subplots(1, 2, figsize=(9, 3))

# Left plot: histogram of mu
axes[0].hist(mu_samples, bins=30, density=False, alpha=0.7, edgecolor='black')
if titles:
   axes[0].set_title(r'Parameters $\mu$ drawn with a Beta(1.5,2) distribution')
   axes[0].set_xlabel('Value')
   axes[0].set_ylabel('Samples')

# Right plot: histogram of f(mu)
axes[1].hist(f_samples, bins=30, density=False, alpha=0.7, edgecolor='black')
if titles:
   axes[1].set_title(r'Function $f=10+\sin(2\pi \mu)$')
   axes[1].set_xlabel('Value')
   axes[1].set_ylabel('Samples')

# Adjust layout
plt.tight_layout()

# Save as PDF
if titles:
   plt.savefig("beta_distribution_plots.pdf")
else:
   plt.savefig("beta_distribution_plots_no_titles.pdf")
plt.show()

