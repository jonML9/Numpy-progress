import numpy as np

first_day = np.array([5, 3, 12, 9, 12])
second_day = np.array([7, 6, 11, 5, 10])
third_day = np.array([13, 5, 3, 8, 14])
fourth_day = np.array([12, 4, 9, 11, 15])


overall = np.stack([first_day, second_day, third_day, fourth_day]) # each row is the quantity of orders of a specific product

each_product_sold = np.sum(overall, axis=0) # adds values vertically
medium_number_of_sold_products = np.mean(overall, axis=0) # calculates mean number of orders of a product

print(overall)
print(each_product_sold)
print(medium_number_of_sold_products)


