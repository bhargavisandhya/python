bookdict = dict([("python",50),("web development",60),("Design and analysis of algorithms",55),("Data base management systems",65),("android development",68),("Deep Learning",70)])# here we use dictionary
print("Now let us have glance at all the list of books in the UMKC book store:") # printing the list of books
for k,v in bookdict.items(): # creating class
    print(k,v)
print("Now enter the range of values to find the books in that range") # entering the range of values
start = int(input("enter the starting value:")) # here we will enter the starting values
last = int(input("enter the ending value")) # here we will enter the ending values
for name,val in bookdict.items():
    if val >= start and val <= last:
        print("Books available in the given cost are",name) # here the available books and cost of that specific book  will be displayed.