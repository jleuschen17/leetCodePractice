import numpy as np
alpha = 'abcdefghijklmnopqrstuvwxyz'
alphaDict = {}
i=0
for char in alpha:
    alphaDict[char] = i
    i+=1

print(alphaDict[1])