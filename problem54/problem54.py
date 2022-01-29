def spiralOrder(matrix):
    newMatrix = []
    i = 0
    j = 0
    targetNum = len(matrix) * len(matrix[0])

    def up(i, j, matrix, newMatrix, iters):
        iters+=1
        while True:
            if len(newMatrix) == targetNum:
                return newMatrix
            if j >= iters:
                newMatrix.append(matrix[j][i])
                j-=1
            else:
                return right(i+1, j+1, matrix, newMatrix, iters)
    def left(i, j, matrix, newMatrix, iters):
        while True:
            if len(newMatrix) == targetNum:
                return newMatrix
            if i >= iters:
                newMatrix.append(matrix[j][i])
                i-=1
            else:
                return up(i+1, j-1, matrix, newMatrix, iters)
    def down(i, j, matrix, newMatrix, iters):
        while True:
            if len(newMatrix) == targetNum:
                return newMatrix
            if j < len(matrix) - iters:
                newMatrix.append(matrix[j][i])
                j+=1
            else:
                return left(i-1, j-1, matrix, newMatrix, iters)

    def right(i, j, matrix, newMatrix, iters):
        while True:
            if len(newMatrix) == targetNum:
                return newMatrix
            if i < len(matrix[0]) - iters:
                newMatrix.append(matrix[j][i])
                i+=1
            else:
                return down(i-1, j+1, matrix, newMatrix, iters)
    finalMatrix = right(i, j, matrix, newMatrix, 0)
    return finalMatrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))