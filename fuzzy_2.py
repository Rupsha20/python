import numpy as np
import matplotlib.pyplot as plt

# Triangular Membership Function
def triangular(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

# Trapezoidal Membership Function
def trapezoidal(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)

# Gaussian Membership Function
def gaussian(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

# Define the x range
x = np.linspace(0, 10, 500)

# Triangular membership function parameters
tri_a, tri_b, tri_c = 2, 5, 8
tri_y = triangular(x, tri_a, tri_b, tri_c)

# Trapezoidal membership function parameters
trap_a, trap_b, trap_c, trap_d = 2, 4, 6, 8
trap_y = trapezoidal(x, trap_a, trap_b, trap_c, trap_d)

# Gaussian membership function parameters
gauss_mean, gauss_sigma = 5, 1.5
gauss_y = gaussian(x, gauss_mean, gauss_sigma)

# Plotting the membership functions
plt.figure(figsize=(12, 6))

# Plot each function
plt.plot(x, tri_y, label="Triangular", color='b')
plt.plot(x, trap_y, label="Trapezoidal", color='g')
plt.plot(x, gauss_y, label="Gaussian", color='r')

# Adding labels, title, and legend
plt.title("Typical Membership Functions")
plt.xlabel("x")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid()

# Display the plot
plt.show()
