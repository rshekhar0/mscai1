import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Function to generate synthetic data
def generate_data():
    n_samples = int(input("Enter the number of data points to generate: "))
    n_centers = int(input("Enter the number of clusters to generate: "))
    A, B = make_blobs(
        n_samples=n_samples,
        centers=n_centers,
        cluster_std=0.60,
        random_state=0
    )
    return A, B

# Function to plot generated data
def plot_data(A):
    plt.scatter(A[:, 0], A[:, 1])
    plt.title('Generated Data')
    plt.show()

# Function to perform Gaussian Mixture Model (GMM) clustering
def apply_gmm(A, num_clusters):
    gmm = GaussianMixture(n_components=num_clusters, random_state=0)
    pred_B = gmm.fit_predict(A)
    
    # Plot the clustered data
    plt.scatter(A[:, 0], A[:, 1], c=pred_B, cmap='viridis')
    plt.title('Gaussian Mixture Model (GMM) Clustering')
    plt.show()

if __name__ == "__main__":
    # Generate and plot synthetic data
    A, B = generate_data()
    plot_data(A)
    
    # Get user input for the number of clusters for GMM
    num_clusters_gmm = int(input("Enter the number of clusters for GMM: "))
    
    # Apply GMM clustering with the chosen number of clusters
    apply_gmm(A, num_clusters_gmm)
