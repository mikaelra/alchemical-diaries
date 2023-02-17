# Data gathered from 20 - 27.07.2021

ml = [810, 450, 351, 320, 300, 275]
p = [0.36, 0.625, 0.82, 0.849, 0.876, 0.876]
ea = []
print('ml')
print(ml)

print('p')
print(p)

print("ml * p = ea")
for i in range(len(ml)):
    ea.append(ml[i]*p[i])
print(ea)

from matplotlib.pyplot import *

plot(ea)
show()

