class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def front_through(node):
    print(node.val)
    if node.left:
        front_through(node.left)
    if node.right:
        front_through(node.right)
    return None

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

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10
    front_through(pRoot1)
