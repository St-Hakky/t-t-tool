# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt


class NearestNeighbor:

    def __init__(self):
        self.data = None
        self.distance = None

    def fit(self, data, distance="euclidean"):
        self.data = data
        self.distance = distance

    def get_nearest_neighbor(self, q):
        if self.distance == "euclidean":
            distances = np.array(
                [self._get_euclidean_distance(p, q) for p in self.data])

        index = distances.argmin()
        return (index, self.data[index])

    def _get_euclidean_distance(self, p, q):
        return np.linalg.norm(p - q)


def __main():

    # Setting
    N = 100
    dim = 2
    data = np.random.rand(N, dim)

    # Query
    q = np.random.rand(1, dim)[0]

    # nearest neighbour
    nn = NearestNeighbor()
    nn.fit(data)
    nn_index, nn_sample = nn.get_nearest_neighbor(q)

    # visualize
    plt.gca().set_aspect('equal', adjustable='box')
    plt.ylim([0, 1])
    plt.xlim([0, 1])
    plt.scatter(x=data.T[0], y=data.T[1],
                color="blue", label="Data")
    plt.scatter(x=q[0], y=q[1],
                color="green", label="Query")
    plt.scatter(x=nn_sample[0], y=nn_sample[1],
                color="red", label="Nearest Neighbor")
    plt.legend(loc="best")
    plt.show()


if __name__ == "__main__":
    __main()
