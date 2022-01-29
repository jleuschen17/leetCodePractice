import numpy as np
arr = np.linspace(0, 198, 100)
def BinarySearch(target, arr):
    newarr = arr
    print(len(newarr))
    while True:
        if len(newarr) == 0:
            return False
        index = len(newarr) // 2
        if newarr[index] == target:
            return True
        elif newarr[index] < target:
            newarr = newarr[index + 1:]
            print(newarr)
        else:
            newarr = newarr[:index]
            print(newarr)


print(BinarySearch(109, arr))