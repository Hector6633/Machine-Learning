import  numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

per = np.percentile(ages, 70)
print(per)

# data distribution and make big data set
x = np.random.uniform(0.0, 5.0, 250)
print(x)