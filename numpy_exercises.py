#!/usr/bin/env python
# coding: utf-8

# In[3]:


# importing numpy and renaming as np
import numpy as np


# In[4]:


# creating a np array
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[11]:


#1 How many negative numbers are there?
print(a[a < 0].shape[0])   # a where a is less than 0. then getting the sum with shape
print(len(a[a < 0]))     # use len to get the length


# In[12]:


#2 How many positive numbers are there?
print(a[a > 0].shape[0])    # a where a is greater than 0. then getting the sum w/ shape
print(len(a[a >0]))      # use len to get the length


# In[20]:


#3 How many even positive numbers are there?
a[(a > 0) & (a % 2 ==0)].shape[0]   # a where a is greater than 0 and a is divisible by 2 w/ no remainder.
                                    # Use shape to get the sum


# In[22]:


len(a[(a > 0) & (a % 2 ==0)])     # use len to get the length


# In[9]:


#4 If you were to add 3 to each data point, how many positive numbers would there be?
a[(a + 3) > 0].shape     # adding 3 to a. then putting condition of a > 0. This gives me a list of all nums > 0
                        # then getting the sum with shape
len(a[(a + 3) > 0])


# In[7]:


a[(a + 3) > 0]


# In[10]:


#5 If you squared each number, what would the new mean and standard deviation be?
print(a.mean())     # getting the avg of a 
print((a ** 2).mean())     # getting the a squared avg
print(a.std())     # getting the stddev of a
print((a **2).std())     # getting the stdev of a squared


# In[24]:


#6. A common statistical operation on a dataset is centering. This means to adjust the data such that the
# center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.
# print(a.mean())
# print(a)
b = a - a.mean()  # Creating a variable that takes a and subtracts the avg
b


# In[33]:


import matplotlib.pyplot as plt
plt.hist(a)
plt.show()


# In[32]:


b.mean()     # getting the avg of the new variable to confirm 0
plt.hist(b)
plt.show()


# In[ ]:


#7. Calculate the z-score for each data point. Recall that the z-score is given by:
# Z = Standard score.    x = value     μ = mean     σ = std
# Z = (x − μ) / σ
z = (a - a.mean())/a.std()     # a - avg of a divided by stdev of a
z


# In[34]:


# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add 
# your solutions.
import numpy as np
# Life w/o numpy to life with numpy

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


# In[35]:


## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
def sum_of_a(num):
    return sum(num)     #defining function and returning the sum of the list of a
sum_of_a(a)


# In[40]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
def min_of_a(num):
    return min(num)     #defining function and returning the min of the list of a
min_of_a(a)


# In[41]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
def max_of_a(num):
    return max(num)     #defining function and returning the max of the list of a
max_of_a(a)


# In[38]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
import statistics
def mean_of_a(num):
    return statistics.mean(num)     #defining function, importing statistics module and returning the avg of the list of a
mean_of_a(a)


# In[39]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the 
# above list together
def product_of_a(num):     #defining function 
    result = 1             #creating a starting point
    for x in num:          # for loop to itterate thru list
        result = result * x      # 1 will be multiplied to the first num in list and will cont. thru all the list
    return result
product_of_a(a)


# In[42]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a 
# squared like [1, 4, 9, 16, 25...]
def squares_of_a(num):      #defining function and returning the num squared
    return [a **2 for a in num]
squares_of_a(a)


# In[43]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
def odds_in_a(num):
    list = []     #Creating an empty list
    for x in num:     # for every num in list
        if x % 2 == 1:     # if divisible by 2 and having a remainder of 1
            list.append(x)     # append that num to list
    return list     # Return list
odds_in_a(a)
    


# In[44]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
def evens_in_a(num):
    list = []      #Creating an empty list
    for x in num:      # for every num in list
        if x %2 == 0:     # if divisible by 2 and having a remainder of 0
            list.append(x)     # append that num to list
    return list     # Return list
evens_in_a(a)


# In[45]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares 
# for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array([[3, 4, 5],     # Creating a numpy array b
    [6, 7, 8]])
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need 
# to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
sum_of_b
b.sum()      # array b .sum() will to give you the sum of the array


# In[46]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print(min_of_b)
print(b.min())     # array b .min() will to give you the min of the array


# In[47]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(max_of_b)
print(b.max())     # array b .max() will to give you the max of the array


# In[48]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(mean_of_b)
print(b.mean())     # array b .mean() will to give you the average of the array


# In[ ]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied 
# together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print(product_of_b)
print((b.prod()))     # array b .prod() will to give you the product of all the numbers multiplied


# In[50]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
print(squares_of_b)
print(b ** 2)     # array b ** 2 will to give you the list of squares


# In[51]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
print(odds_in_b)
print(b[b % 2 == 1])     # array b where b is divisible by two w/ a remainder 1 for odds


# In[52]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
print(evens_in_b)
print(b[b % 2 == 0])       # array b where b is divisible by two w/ a remainder 0 for evens


# In[53]:


# Exercise 9 - print out the shape of the array b.
b.shape     # shape


# In[54]:


# Exercise 10 - transpose the array b.
b.transpose()     # array b.transpose() will transform the matrix to a 3 x 2


# In[55]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.flatten()     # array b.flatten() will make a 1x 6 matrix


# In[56]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(6,1)


# In[57]:


b.reshape(-1,1)     # -1 will show all rows if not known


# In[79]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(c.min())
print(c.max())
print(c.sum())
print(c.prod())


# In[80]:


# Ex 1 - print out standard deviation of c. STD is the sqrt of the variance
c.std()


# In[81]:


# Exercise 3 - Determine the variance of c.
c.var()


# In[82]:


c.std() ** 2      #Another way to get the variance


# In[83]:


# Exercise 4 - Print out the shape of the array c
c.shape


# In[84]:


# Exercise 5 - Transpose c and print out transposed result.
c.transpose()


# In[87]:


# Exercise 6 - Get the dot product of the array c with c. 
print(c.prod())
print(c.dot(c))


# In[76]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
t = c.transpose()
(c * t).sum()


# In[19]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(c * t).prod()


# In[32]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])
import math
# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)


# In[33]:


# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)     # add np when dealing with trig the fuction with the corresponding array d


# In[34]:


# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)     # add np when dealing with trig the fuction with the corresponding array d


# In[35]:


# Exercise 4 - Find all the negative numbers in d
d[d < 0]     # d where d is less than 0


# In[36]:


# Exercise 5 - Find all the positive numbers in d
d[d > 0]


# In[37]:


# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)


# In[42]:


# Exercise 7 - Determine how many unique numbers there are in d.
np.unique(d).shape


# In[45]:


# Exercise 8 - Print out the shape of d.
d.shape     #shows we have a 3 x 6 matrix


# In[47]:


# Exercise 9 - Transpose and then print out the shape of d.
d.transpose().shape      # transposes the 3x6 matrix to 6x3


# In[48]:


# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)      # to reshape the array use the array.reshape(how you want to reshape it seperated by comma)


# In[ ]:




