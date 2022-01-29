def rotate(matrix):
    jOrig = len(matrix) - 1
    for i in range(len(matrix)):
        matrix.append([])
        j=jOrig
        while True:
            if j < 0:
                break
            matrix[-1].append(matrix[j][i])
            j-=1
    for i in range(jOrig + 1):
        matrix.pop(0)
    print(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)