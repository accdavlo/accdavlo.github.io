import numpy as np
import matplotlib.pyplot as plt

# X-axis values (N)
N = np.arange(1, 16)

def add_noise(x):
   noise = 0.02*(np.random.rand(15)-0.5)
   noise[0]=0
   return x+noise

# Synthetic Y-values (log10 error) reconstructed from the image
std_uniform = np.array([-0.55, -0.8, -0.95, -1.35, -1.55, -1.65, -1.7, -1.8, -1.9, -2.0, -2.05, -2.15, -2.25, -2.3, -2.35])
w_uniform   = np.array([-0.55, -0.75, -1.05, -1.9, -2.0, -2.05, -2.1, -2.15, -2.2, -2.3, -2.35, -2.4, -2.5, -2.65, -2.8])
std_dist    = np.array([-0.55, -0.81, -1.04, -1.9, -2.0, -2.15, -2.3, -2.4, -2.5, -2.6, -2.7, -2.8, -2.9, -3.05, -3.2])
w_dist      = np.array([-0.55, -0.81, -1.02, -1.9, -2.05, -2.2, -2.35, -2.45, -2.55, -2.65, -2.75, -2.9, -3.0, -3.2, -3.4])

# Create figure
plt.figure(figsize=(5, 4))

# Plot lines
plt.plot(N, add_noise(std_uniform), 'k--', label='Standard Uniform Greedy')
plt.plot(N, add_noise(w_uniform), color='olive', marker='*', markersize=8, label='Weighted Uniform Greedy')
plt.plot(N, add_noise(std_dist), 'b-o', label='Standard Distributed Greedy')
plt.plot(N, add_noise(w_dist), 'r-', linewidth=2, label='Weighted Distributed Greedy')

# Labels, legend, title
plt.xlabel(r'$N$')
plt.ylabel(r'$\log_{10}(\mathbb{E}\|u_{N_\delta}(Y) - u_N(Y)\|^2_{1,\Omega})^{1/2}$')
# plt.title('Error Comparison')
plt.legend()

# Save to PDF
plt.tight_layout()
plt.savefig("error_comparison_greedy.pdf")
plt.show()

