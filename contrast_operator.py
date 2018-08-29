import numpy as np
from sklearn.mixture import GaussianMixture

class ContrastOperator:

    _data_points = None
    clusterer = None
    _number_of_clusters = 1

    def __init__(self):
        self._data_points = None

    def set_cluster_number(self, number):
        self._number_of_clusters = number

    def add_point_to_data(self, point):
        if self._data_points is None:
            self._data_points = np.copy(point).flatten()
            self._data_points = np.expand_dims(self._data_points,axis=1)
        else:
            pt = np.copy(point)
            pt = pt.flatten()
            if len(pt) > self._data_points.shape[1]:
                for p in self._data_points:
                    p = np.append((p,np.zeros(len(pt) - self._data_points.shape[1])))
            self._data_points = np.append(point)

    def cluster_gaussian(self):
        self.clusterer = GaussianMixture(n_components=self._number_of_clusters)
        self.clusterer.fit(self._data_points)
