import numpy as np

frustration_level = np.array([51, 30, 33, 43, 47, 53, 0])
happiness_level = np.array([44, 57, 57, 57, 47, 40, 70])

correlation = np.corrcoef(frustration_level, happiness_level)[0, 1]
print(correlation)
