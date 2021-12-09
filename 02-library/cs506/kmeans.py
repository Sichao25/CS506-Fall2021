from collections import defaultdict
from math import inf
import random
import sys
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    #raise NotImplementedError()
    means=[]
    n = len(points)
    d = len(points[0])
    for j in range(d):
        mean = 0
        for p in points:
            mean += p[j]
        means.append(mean/n)
    return means
    
def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    #raise NotImplementedError()
    clusters = list(set(assignments))
    clusters.sort()
    centroids = []

    for c in clusters:
        points_in_cluster = []
        for i in range(len(dataset)):
            if assignments[i] == c:
                points_in_cluster.append(dataset[i])
        centroids.append(point_avg(points_in_cluster))

    return centroids

        

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    #raise NotImplementedError()
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i])**2
    return res**(1/2)

def distance_squared(a, b):
    #raise NotImplementedError()
    return distance(a,b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    #raise NotImplementedError()
    res = []
    idx = [i for i in range(len(dataset))]
    idx_choice = random.choices(idx, k=k)
    for i in range(len(dataset)):
        if i in idx_choice:
            res.append(dataset[i])
    return res

def cost_function(clustering):
    #raise NotImplementedError()
    cost = 0
    for cluster_id in clustering.keys():
        cluster = clustering.get(cluster_id)
        centroid = point_avg(cluster)
        for entry in cluster:
            cost += distance_squared(entry, centroid)
    return cost

def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    # raise NotImplementedError()
    centroids = []
    centroids.append(random.choice(dataset))
    for i in range(1,k):
        dists = []
        pp = []
        cumsum = []
        for point in dataset:   
            d = sys.maxsize
            for j in range(len(centroids)):
                dist = distance(point, centroids[j])
                dists.append(min(d, dist))
            d2 = sum(dists)
            p = d/d2
            pp.append(p)
            cumsum.append(sum(pp))
        rdm = random.randrange(0,1)
        for p in cumsum:
            if rdm < p:
                i = j
                break
        centroids.append(dataset[i])
    return centroids  



def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
