import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')
print(calorie_stats)

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

nth_percentile = np.percentile(calorie_stats, 3.3)
print(nth_percentile)

more_calories = 100 - 3.3
print(more_calories)

calorie_std = np.std(calorie_stats)
print(calorie_std)