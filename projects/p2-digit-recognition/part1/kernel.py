import numpy as np

### Functions for you to fill in ###



def polynomial_kernel(X, Y, c, p):
    """
        Compute the polynomial kernel between two matrices X and Y::
            K(x, y) = (<x, y> + c)^p
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            c - a coefficient to trade off high-order and low-order terms (scalar)
            p - the degree of the polynomial kernel

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    # Compute the dot product between each pair of points (x in X and y in Y)
    dot_product = np.dot(X, Y.T)

    # Add the coefficient c, then raise to the power of p
    kernel_matrix = (dot_product + c) ** p

    return kernel_matrix


def rbf_kernel(X, Y, gamma):
    """
        Compute the Gaussian RBF kernel between two matrices X and Y::
            K(x, y) = exp(-gamma ||x-y||^2)
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            gamma - the gamma parameter of gaussian function (scalar)

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    # Compute squared norms for X and Y
    X_norm = np.sum(X ** 2, axis=1).reshape(-1, 1)  # shape: (n, 1)
    Y_norm = np.sum(Y ** 2, axis=1).reshape(1, -1)  # shape: (1, m)

    # Compute pairwise squared Euclidean distances
    sq_dists = X_norm + Y_norm - 2 * np.dot(X, Y.T)

    # Apply the RBF function
    kernel_matrix = np.exp(-gamma * sq_dists)

    return kernel_matrix
