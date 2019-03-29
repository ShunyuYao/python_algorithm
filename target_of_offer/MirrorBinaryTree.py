"""
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def __init__(self):
        self.root_list = []

    def Mirror(self, root):
        if not root:
            return None
        self.root_list.append(root.val)
        root.left, root.right = root.right, root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)

        return self.root_list

if __name__ == '__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    root = Solution().Mirror(pRoot1)
    print(root)
