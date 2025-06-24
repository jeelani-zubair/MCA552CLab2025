import numpy as np                                      # numpy: For numerical operations (not used explicitly here).
import matplotlib.pyplot as plt                         # matplotlib.pyplot: For plotting graphs.
import seaborn as sns                                   # seaborn: Enhances matplotlib plots with better style.
from sklearn.datasets import load_iris                  # load_iris: Loads the Iris dataset.
from sklearn.preprocessing import StandardScaler        # StandardScaler: Standardizes data (zero mean, unit variance).
from sklearn.cluster import AgglomerativeClustering     # AgglomerativeClustering: For performing hierarchical clustering.
from scipy.cluster.hierarchy import dendrogram, linkage # dendrogram, linkage: Functions from scipy to build dendrograms for hierarchical clustering.


# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# X contains 150 samples with 4 features (sepal/petal length/width).
# y contains the true species labels (0, 1, 2) — used only for comparison or evaluation.


# Optional: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Standardization ensures that all features have equal importance by rescaling them to have a mean of 0 and standard deviation of 1.
# This is important for clustering as it is based on distance metrics (e.g., Euclidean).


# -----------------------------
# 1. Dendrogram using scipy
# -----------------------------
linked = linkage(X_scaled, method='ward')
# Performs hierarchical clustering using Ward’s method (minimizes variance within clusters).
# linked is a linkage matrix used to create the dendrogram.
# Format of linkage matrix: [cluster1, cluster2, distance, sample_count]


plt.figure(figsize=(10, 6))
dendrogram(linked,
           orientation='top',
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('Dendrogram (Hierarchical Clustering)')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distance')
plt.show()
# Dendrogram shows how data points are merged at each stage of the hierarchy.
# The height of the merges represents the distance between clusters.
# By cutting the dendrogram at a certain height, you decide how many clusters to form.


# -----------------------------
# 2. Agglomerative Clustering
# -----------------------------
# Choose number of clusters (from dendrogram analysis or known labels)
n_clusters = 3
agg_cluster = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
cluster_labels = agg_cluster.fit_predict(X_scaled)
# Creates a clustering model that groups data into n_clusters (here, 3).
# affinity='euclidean': uses Euclidean distance.
# linkage='ward': minimizes within-cluster variance.
# fit_predict() returns a list of cluster labels assigned to each point.


# -----------------------------
# 3. Scatter Plot of Clusters
# -----------------------------
# For visualization, use only first two features
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_scaled[:, 2], y=X_scaled[:, 3],
                hue=cluster_labels, palette='Set1', s=60)
plt.title('Agglomerative Clustering (First 2 Features)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()
# This plots a 2D scatter plot of the first two standardized features.
# Each point is colored based on its assigned cluster.
# You can visually observe how well the clusters are separated in this 2D space.
