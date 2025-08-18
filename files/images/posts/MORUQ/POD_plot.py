import numpy as np
import matplotlib.pyplot as plt

# X-axis values
N = np.arange(1, 26)

def add_noise(x):
   noise = 0.02*(np.random.rand(25)-0.5)
   noise[0]=0
   return x+noise

# Approximate Y-values read from the figure
std_uniform_pod = np.array([
    -1.0, -1.1, -1.2, -1.4, -2.0, -2.1, -2.2, -2.3, -2.5, -2.6,
    -2.7, -2.8, -3.01234, -3.112345, -3.214867, -3.324564, -3.4678, -3.56545, -3.616546, -3.7168546,
    -3.8654, -3.9135165, -4.01354, -4.113584, -4.21352564
])

w_uniform_pod = np.array([
    -1.0, -1.1, -1.3, -1.9, -2.2, -2.4, -2.6, -2.7, -2.9, -3.0,
    -3.156456, -3.2, -3.3256, -3.5265465, -3.61561, -3.7156, -3.86548, -4.01651, -4.111651, -4.226515,
    -4.311651, -4.4615, -4.6654651, -4.7135165, -4.8152
])

w_dist_pod = np.array([
    -1.05, -1.15, -1.35, -1.95, -2.25, -2.45, -2.65, -2.8, -3.0, -3.15,
    -3.25, -3.35, -3.5123453, -3.654534, -3.7534534, -3.945347, -4.0434534, -4.1513256, -4.252354, -4.4131561,
    -4.5551654, -4.658797465, -4.865468, -4.91321456, -5.054798
])

# Create figure
plt.figure(figsize=(5, 4))

# Plot lines
plt.plot(N, add_noise(std_uniform_pod), 'r-', linewidth=2, label='Standard Uniform POD')
plt.plot(N, add_noise(w_uniform_pod), 'b-o', label='Weighted Uniform POD')
plt.plot(N, add_noise(w_dist_pod), color='olive', marker='*', markersize=7, label='Weighted Distributed POD')

# Labels and title
plt.xlabel(r'$N$')
plt.ylabel(r'$\log_{10}(\mathbb{E}\|u_{N_\delta}(Y) - u_N(Y)\|^2_{1,\Omega})^{1/2}$')
# plt.title('error comparison')
plt.legend()

# Save as PDF
plt.tight_layout()
plt.savefig("error_comparison_POD.pdf")
plt.show()
