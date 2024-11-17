import numpy as np
# from  scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

median = np.median(speed)
print(median)

mean = np.mean(speed)
print(mean)

# mode = stats.mode(speed)
# print(mode)

# standard deviations

std = np.std(speed)
print(std)

# varience
var = np.var(speed)
print(var)