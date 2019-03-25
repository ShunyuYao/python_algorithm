'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None
        root = TreeNode(pre[0])
        tin_root_pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:tin_root_pos+1],
                                               tin[:tin_root_pos])
        root.right = self.reConstructBinaryTree(pre[tin_root_pos+1:],
                                                tin[tin_root_pos+1:])
        return root


pre = [3, 4, 6, 5, 7, 8]
tin = [6, 4, 3, 7, 5, 8]
t1 = []
solve = Solution()
output1 = solve.reConstructBinaryTree(pre, tin)
output2 = solve.reConstructBinaryTree(pre, t1)
output3 = solve.reConstructBinaryTree(t1, t1)
