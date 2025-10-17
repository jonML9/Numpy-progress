import numpy as np

ratings = np.array([4.2, 3.4, 4.98, 4.56, 4.81, 5, 4.01, 2.99])
positive_ratings = ratings[ratings >= 4] #I am writing 'ratings' two times in order to sort 'True' values, because if I write it one time, it will show Trues and Falses
negative_ratings = ratings[ratings <= 4]
print(positive_ratings)
print(negative_ratings)