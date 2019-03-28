"""
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下
移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
 例如:
 a b c e
 s f c s
 a d e e
 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
 但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个
 格子之后，路径不能再次进入该格子。
 """
# -*- coding:utf-8 -*-
# todo: 找到路径然后返回的代码有些冗余
# def restruct_matrix(matrix):
#     for i, mat in enumerate(matrix):
#         if i % 4 == 0:
#             i
class Solution:

    def __init__(self):
        self.passed = []
        self.find = False

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(path) < 1:
            return True
        height = len(matrix)
        width = len(matrix[0])
        if [rows, cols] not in self.passed:
            self.passed.append([rows, cols])
        else:
            return False
        if matrix[rows][cols] != path[0]:
            return False
        else:
            print(path)
            if rows + 1 < height:
                self.find = self.hasPath(matrix, rows+1, cols, path[1:])
                if self.find:
                    return True
            if rows - 1 >= 0:
                self.find = self.hasPath(matrix, rows-1, cols, path[1:])
                if self.find:
                    return True
            if cols + 1 < width:
                self.find = self.hasPath(matrix, rows, cols+1, path[1:])
                if self.find:
                    return True
            if cols - 1 >= 0:
                self.find = self.hasPath(matrix, rows, cols-1, path[1:])
                if self.find:
                    return True
        return False

if __name__ == '__main__':
    matrix = [
     ['a', 'b', 'c', 'e'],
     ['s', 'f', 'c', 's'],
     ['a', 'd', 'e', 'e']
      ]
    rows = 0
    cols = 1
    path = 'bcced'
    find = Solution().hasPath(matrix, rows, cols, path)
    print(find)
