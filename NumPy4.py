import numpy as np

np.random.seed(40) #for not letting 'random' module change the numbers every time when the program runs (you can insert any num into ())

one = np.random.random((3, 2)) #module random generates any number from 0.0 to 1.0

two = np.random.random((3, 2)) #generates 3 numbers (axis 'y') and 2 numbers 'axis 'x'

three = np.random.randint(10, 20, size = (2, 4)) #for generating numbers from 10 (included) to 20(excluded)

four = np.random.uniform(10.5, 20.9, size = (2, 4)) #for generating 'float numbers'

five = np.random.choice(np.array(['John', 'Dave', 'Emilia']), size = (5)) #just shuffles values in array, and here it gives 5 shuffled values

six = np.arange(1, 10, 2) #1 - start, 10 - end(excluded), 2 - gap

seven = np.arange(1, 9).reshape((2, 4)) #makes the array two-dimensional


print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)