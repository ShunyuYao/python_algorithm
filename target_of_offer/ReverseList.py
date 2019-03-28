"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        node1 = pHead
        node2 = pHead.next
        node1.next = None
        while node2.next is not None:
            temp_node = node2.next
            node2.next = node1
            node1 = node2
            node2 = temp_node

        node2.next = node1
        return node2

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    output = Solution().ReverseList(n1)
    print(output.next.next.next.val)

"""
思路：
很简单，用两个相邻指针，将后一个指针的下一个节点指向前一个指针，
不断右移指针即可，因为反转后头节点会变成尾节点，所以要注意删除头节点的下一个节点
"""
