from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic 3D data (for illustration purposes)
np.random.seed(0)
X = np.dot(np.random.random((3, 3)), np.random.normal(size=(3, 200))).T

# Apply PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)  # Reduce the dimensionality to 2D

# Plot the original 3D data
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(121, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], color='blue')
ax.set_title('Original 3D Data')

# Plot the PCA-reduced 2D data
plt.subplot(122)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], color='red')
plt.title('PCA-Reduced 2D Data')

plt.show()
