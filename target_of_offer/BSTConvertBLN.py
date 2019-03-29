"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # left tree nodes
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree

        # right tree nodes
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree

        # back to the top of the list
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree

if __name__ == '__main__':
    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7

    S = Solution()
    newList = S.Convert(pNode1)
    print(newList.val)
"""
思路：
递归把树分为左子树、右子树和根节点，连接根节点和左子树
最右边的值（左子树最大值）。连接根节点和右子树最左边的值
（右子树最小值）即可。主要是要理递归的结束条件和返回值。
"""
