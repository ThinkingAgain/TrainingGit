"""
矩阵旋转
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""

def rotate(matrix) :
    lo = 0
    hi = len(matrix) - 1

    while (lo < hi):
        for i in range(lo,hi):
            t = matrix[lo][i]
            matrix[lo][i] = matrix[hi+lo-i][lo]
            matrix[hi+lo-i][lo] = matrix[hi][hi+lo-i]
            matrix[hi][hi+lo-i] = matrix[i][hi]
            matrix[i][hi] = t
        lo +=1
        hi -=1


m=[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

rotate(m)
for x in m:
    print(x)


"""
行列式计算
Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

A 1x1 matrix |a| has determinant a.

A 2x2 matrix [ [a, b], [c, d] ] or

|a  b|
|c  d|

def determinant(matrix):
    if len(matrix) == 2:
        return maxtrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    

matrix = [ [1, 3], [2,5]]
print(determinant(matrix))
"""

"""
有效的数独：

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
judge = [[]for i in range(27)]
for i in range(9):
    for j in range(9):
        if board[i][j]!=".":
            x = board[i][j]
            if (x in judge[i])or(x in judge[9+j])or(x in judge[i//3*3+j//3+18]):
                print(i,j,":False")
            judge[i].append(x)
            judge[9+j].append(x)
            judge[i//3*3+j//3+18].append(x)
print("True")

print(board)
print(judge)
"""