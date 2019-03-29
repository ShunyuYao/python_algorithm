"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""
# 注意各种非常规输入
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k < 1:
            return None
        node1 = head
        for i in range(k-1):
            if node1.next is None:
                return None
            node1 = node1.next
        node2 = head
        while node1.next is not None:
            node1 = node1.next
            node2 = node2.next
        return node2

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    output = Solution().FindKthToTail(n1, 4)
    print(output.val)

'''
https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%80%92%E6%95%B0%E7%AC%ACk%E4%B8%AA%E7%BB%93%E7%82%B9.py#L6
需要特别注意代码的鲁棒性
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''
