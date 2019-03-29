"""
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵：
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
则依次打印出数字
1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printAPath(self, matrix, cols, rows, start):
        end_rows = rows - start - 1
        end_cols = cols - start - 1
        for i in range(start, end_cols+1):
            print(matrix[start][i])
        if start < end_rows:
            for i in range(start+1, end_rows+1):
                print(matrix[i][end_cols])
        if start < end_cols and start < end_rows:
            for i in range(end_cols-1, start-1, -1):
                print(matrix[end_rows][i])
        if start < end_cols and start < end_rows - 1:
            for i in range(end_rows-1, start, -1):
                print(matrix[i][start])

    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        while cols > 2*start and rows > 2*start:
            self.printAPath(matrix, cols, rows, start)
            start += 1

if __name__ == '__main__':
    matrix = [[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix2 = [[1],[2],[3],[4],[5]]
    matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
    S = Solution()
    # S.printMatrix(matrix)
    # S.printMatrix(matrix2)
    S.printMatrix(matrix3)

"""
思路：
设每次回到坐标(start, start)为一次循环打印，那么可以发现规律：
当左上角坐标满足条件 cols > 2*start and rows > 2*start 时，
可以完成一次循环打印，否则无法完成，但是循环打印可能不完整，需
要考虑边界条件。
边界条件主要是看最后一圈什么时候该停，最后一圈只要能打印就是完整
的一次，否则就是停止
"""
