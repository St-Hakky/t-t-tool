# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt


class KNearestNeighbors:

    def __init__(self):
        self.data = None
        self.distance = None
        self.k = None

    def fit(self, data, k, distance="euclidean"):
        self.data = data
        self.distance = distance
        self.k = k

    def get_k_nearest_neighbors(self, q):
        if self.distance == "euclidean":
            distances = np.array(
                [self._get_euclidean_distance(p, q) for p in self.data])

        indexes = distances.argsort()[:self.k]
        return (indexes, self.data[indexes])

    def _get_euclidean_distance(self, p, q):
        return np.linalg.norm(p - q)


def __main():

    # Setting
    N = 100
    dim = 2
    data = np.random.rand(N, dim)

    # Query
    q = np.random.rand(1, dim)[0]

    # k-nearest neighbors
    knn = KNearestNeighbors()
    knn.fit(data, 10)
    knn_indexes, knn_sample = knn.get_k_nearest_neighbors(q)

    # visualize
    plt.gca().set_aspect('equal', adjustable='box')
    plt.ylim([0, 1])
    plt.xlim([0, 1])
    plt.scatter(x=data.T[0], y=data.T[1],
                color="blue", label="Data")
    plt.scatter(x=q[0], y=q[1],
                color="green", label="Query")
    plt.scatter(x=knn_sample.T[0], y=knn_sample.T[1],
                color="red", label="K Nearest Neighbors")
    plt.legend(loc="best")
    plt.show()


if __name__ == "__main__":
    __main()
