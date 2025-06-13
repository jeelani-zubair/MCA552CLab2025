# kmeans_iris_2d.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
X = iris.data[:, [0, 2]]  # Use only sepal length and petal length
y = iris.target
feature_names = [iris.feature_names[i] for i in [0, 2]]

# Standardize the selected features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)   # (xi' = (xi-mean)/standard deviation) for each feature
                                     # sqrt((xi - mean)/N)
                                     # Standardization ensures each feature contributes equally to the distance calculation by bringing them to the same scale.

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
clusters = kmeans.labels_
centroids = kmeans.cluster_centers_
print(f"Number of iterations until convergence: {kmeans.n_iter_}")

# Plot the clustered data
plt.figure(figsize=(10, 5)) # inches

# KMeans clusters
plt.subplot(1, 2, 1) # 1 row, 1 col, 1st subplot
# sepal length, petal length, colors the points by their KMeans cluster ID, gives a nice color palette, outlines points in black, size of points)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', edgecolor='k', s=60)
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='X', label='Centroids')
plt.title("KMeans Clustering (2D)")
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.legend()

# Actual labels
plt.subplot(1, 2, 2)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap='viridis', edgecolor='k', s=60)
plt.title("Actual Iris Labels (2D)")
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])

plt.tight_layout()
plt.show()