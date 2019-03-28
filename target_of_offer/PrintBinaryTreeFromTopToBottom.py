from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.print_queue = deque()
        self.print_list = []
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        self.print_queue += [root]

        while len(self.print_queue) > 0:
            cur_node = self.print_queue.popleft()
            if cur_node.left:
                self.print_queue += [cur_node.left]
            if cur_node.right:
                self.print_queue += [cur_node.right]
            self.print_list.append(cur_node.val)
        return self.print_list

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
    print(S.PrintFromTopToBottom(pNode1))

"""
并不是所有的二叉树都适合用递归，这个题目不用递归比较好
"""
