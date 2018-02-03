#defining function for getting tripltes
def func(a, n):
    found =False
    for i in range(0, n - 2):
        #creating range

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (a[i] + a[j] + a[k] == 0):
                    print( a[i], a[j], a[k])
                    found = True

    if (found == False):
        print(" No Triplets ")

#defining array
a = [-4, -3, -2, -1, 0, 1, 2, 3]
#defining length
n = len(a)
func(a, n)