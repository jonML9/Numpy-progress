import numpy as np

prices = np.array([14.90, 15.66, 20.11, 30.99, 41.22, 15.75])
quantity = np.array([40, 50, 35, 30, 45, 50])

min_price = np.min(prices) # .min() is a function of numpy
max_price = np.max(prices) # and so is .max()


revenue_per_product = prices * quantity
average_revenue_per_product = np.round(np.mean(revenue_per_product), 2) #.round() is for rounding the value, and .mean() for calculating the average value. '2' is for showing the last two numbers of the float number
total_revenue = np.sum(revenue_per_product)



print(min_price, max_price)
print(revenue_per_product)
print(average_revenue_per_product)
print(total_revenue)











