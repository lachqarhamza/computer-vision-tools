def euclidean(img1, img2):
    if(have_same_size(img1, img2)):
        distance = 0
        distance = numpy.sum((img1 - img2) ** 2)
        return numpy.sqrt(distance)
    else:
        return -1

def manhattan():
    pass

def max():
    pass

def min():
    pass
