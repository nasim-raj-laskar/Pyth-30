import numpy
from matplotlib import pyplot as plt

def  gaussian_kernel(size,size_y=None):
    size=int(size)
    if not size_y:
        size_y=size
    else:
        size_y=int(size_y)
    x,y=numpy.mgrid[-size:size+1,-size_y:size_y+1]
    g=numpy.exp(-(x**2/float(size)+y**2/float(size_y)))
    return g/g.sum()

gaussian_kernel_array=gaussian_kernel(3)
print(gaussian_kernel_array)
plt.imshow(gaussian_kernel_array,cmap=plt.get_cmap('jet'),interpolation='nearest')
plt.colorbar()
plt.show()