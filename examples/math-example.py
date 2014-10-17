import math

p = [4, 7]
q = [2, 9]
x = 0

def dist(p,q):
    global x
    x = math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
    return x

dist(p,q)
print x