"""
题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和
为输入整数的所有路径。路径定义为从树的根结点开始往下一直到
叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，
数组长度大的数组靠前)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        path = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root.left:
            self.FindPath(root.letf, expectNumber-root.val)
        if root.right:
            self.FindPath(root.right, expectNumber-root.val)
