import numpy as np  # here we will import the numpy package
x = np.random.randint(0, 20, 15)# here we are initialising the x value
print("Given List:") #here we will be having the most recently used numbers list which are random
print(x) # the initialised value of x will be printed, the value has the random values
print("Most frequent value in the List:") # the line below we will be getting the most frequent values
print(np.bincount(x).argmax())  # here we used the inbuilt functions which gives the lowest frequency first and the highest frequenvcy next