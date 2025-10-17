import numpy as np

first = np.array([[1, 2, 3], [4, 5, 6]])
second = np.array([[7, 8, 9], [10, 11, 12]])

print(first[1, 2]) #coordinates of 6 ('1' for x axis (the one going right), and '2' is for y axis (the one going deep))
print(np.concatenate([first, second])) #connecting both arrays
a = np.concatenate(np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8])) #one-dimensional merge
print(a)