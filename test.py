#!/data/data/com.termux/files/usr/bin/python
import sys
import numpy as np

print("hello word!")
def pythonsum(n):
    a=list(range(n))
    b=list(range(n))
    c=[]
    for i in range(len(a)):
        a[i]=i**2
        b[i]=i**3
        c.append(a[i]+b[i])

    return c

def numpysum(n):
    a=np.arange(n)**2
    b=np.arange(n)**3
    c=a+b

    return c
    

size=int(sys.argv[1])
print(pythonsum(size))

