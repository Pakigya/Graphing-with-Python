import numpy as np
import matplotlib.pyplot as plt


import math

def getroot(n):
    n= int(n)
    if (n<1):
        #print("no roots as number of root = 0")
        return 0
    elif (n==1):
        return  math.sqrt(2)
    else:
        return  math.sqrt(2+getroot(n-1))

x = []
y = []
print("Enter the number of roots: \n")
n = input("Please enter something: \n")
print("you entered ", str(n), " number of roots.\n")
print("Answer for n roots is ", str(getroot(n)), "\n \n")

print ("for all roots till n, the values of (x,y) to be plotted are as follows")
n= int(n)
for i in range(0,n+1):
    output = "(" + str(i) + "," + str(getroot(i)) + ")\n"
    x.append(i)
    y.append(getroot(i))
    print(output)

plt.plot(x,y, '-r', label =  'n vs root graph' )

plt.show()
