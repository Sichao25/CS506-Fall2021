from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    #raise NotImplementedError()
    means=[]
    n=len(points)
    for j in range(len(points[0])):
        mean=0
        for i in range(n):
            means+=points[i][j]
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
    centroids=[]
    sum_samples={}
    for i in range(len(assignments)):
        if assignments[i][0] not in sum_samples:
            sum_samples[assignments[i][0]]=[0]
            for j in range(len(dataset[0])):
                sum_samples[assignments[i][0]].append(0)
        sum_samples[assignments[i][0]][0]+=1
        for j in range(len(dataset[0])):
            sample=sum_samples[assignments[i][0]]
            sample[j+1]+=dataset[i][j]
    
    i=0
    while i in sum_samples:
        value=sum_samples[i]
        slice_value=[]
        for num in value[1:]:
            slice_value.append(num/value[0])
        centroids.append(slice_value)
    #centroids.append([value[0]/value[2],value[1]/value[2]])
        i+=1
    centroids=np.array(centroids)
    #print(centroids)
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
    pass

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
