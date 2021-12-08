def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    #raise NotImplementedError()
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    #raise NotImplementedError()
    intersection = len(list(set(x).intersection(y)))
    union = (len(set(x)) + len(set(y))) - intersection
    if union == 0:
        return 1
    else:
        return 1 - float(intersection) / union

def dot(A,B): 
    return (sum(a*b for a,b in zip(A,B)))

def cosine_sim(x, y):
    #raise NotImplementedError()
    if dot(x,x) == 0 or dot(y,y) == 0:
        return 0
    else:
        return dot(x,y) / ( (dot(x,x) **.5) * (dot(y,y) ** .5) )
# Feel free to add more
