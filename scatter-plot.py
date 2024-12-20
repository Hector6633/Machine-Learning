import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

# Histogram
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)
y = numpy.random.normal(6.4, 74.36, 1000)

plt.hist(x, 100)
plt.show()
plt.scatter(x,y)
plt.show()
