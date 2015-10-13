__author__ = 'laura'
from math import sqrt
import matplotlib.pyplot as plt
import numpy
import random
from operator import itemgetter


class Point(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return "x={0:.3f},y={1:.3f})".format(self.x, self.y)


def distance(point_1, point_2):
    return sqrt(pow((point_1.x - point_2.x), 2) + pow((point_1.y -point_2.y), 2))


def average_points(points):
    sum_x = 0.0
    sum_y = 0.0
    num_points = len(points)
    for p in points:
        sum_x += p.x
        sum_y += p.y
    return Point(sum_x/num_points, sum_y/num_points)


def plot_k_mean(points, all_centroids):
    x = [p.x for p in points]
    y = [p.y for p in points]
    for centroids in all_centroids:
        xc = [c.x for c in centroids]
        yc = [c.y for c in centroids]
        print("centroids", xc, yc)
        plt.scatter(x, y, c="blue")
        plt.scatter(xc, yc, c="red")
        plt.plot()
        plt.show()
        #plt.pause(0.00005)
        #plt.clf()


def k_mean(points, num_k, limit_x, limit_y):
    num_points = len(points)
    centroids = [Point(random.randint(1, limit_x), random.randint(1, limit_y)) for k in range(num_k)]
    grades = numpy.zeros((num_points, num_k), dtype=numpy.int)
    all_centroids = []
    b = None
    old_b = None
    while old_b is None or grades != old_grades:
        all_centroids.append(centroids[:])
        distances = [[distance(p, c) for c in centroids] for p in points]
        old_grades = [[grades[i][k] for k in range(num_k)] for i in range(num_points)]
        grades = [[0 if k != min(enumerate(distances[i][:]), key=itemgetter(1))[0] else 1 for k in range(num_k)] for i in range(num_points)]
        print("grades", grades)
        for k in range(num_k):
            points_centroid = []
            for i in range(num_points):
                if grades[i][k] == 1:
                    points_centroid.append(points[i])
            if len(points_centroid) == 0:
                points_centroid.append(Point(random.randint(1, limit_x), random.randint(1, limit_y)))
            centroids[k] = average_points(points_centroid)
        b = numpy.packbits([grades[i][:] for i in range(num_points)], axis=-1)
        old_b = numpy.packbits([old_grades[i][:] for i in range(num_points)])
        print("grades", grades)
        print("old", old_grades)
    return all_centroids


def main():
    num_points = 10
    limit_x = 20
    limit_y = 20
    num_k = 2
    points = [Point(random.randint(1, limit_x), random.randint(1, limit_y)) for i in range(num_points)]
    all_centroids = k_mean(points, num_k, limit_x, limit_y)
    plot_k_mean(points, all_centroids)

if __name__ == "__main__":
    main()