"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链
表满足单调不减规则。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 and not pHead2:
            return pHead1
        if pHead2 and not pHead1:
            return pHead2
        if not pHead1 and not pHead2:
            return None
        if pHead1.val < pHead2.val:
            node = pHead1
            pHead1 = pHead1.next
        else:
            node = pHead2
            pHead2 = pHead2.next
        head = node
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val < pHead2.val:
                node.next = pHead1
                pHead1 = pHead1.next
            else:
                node.next = pHead2
                pHead2 = pHead2.next
            node = node.next

        while pHead1 is not None:
            node.next = pHead1
            pHead1 = pHead1.next
            node = node.next

        while pHead2 is not None:
            node.next = pHead2
            pHead2 = pHead2.next
            node = node.next
        return head

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(6)
    n4 = ListNode(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(7)
    p1.next = p2
    p2.next = p3

    node = Solution().Merge(n1, p1)
    while node is not None:
        print(node.val)
        node = node.next
    # print(node.next.next.next.next.val)

"""
这个和归并排序的"并"阶段很像，只不过变成了链表，同时要注意边界条件。
相同思路的题目似乎在面试时很热门，我自己面试时碰到一次，
在网上看别人的面经时也看到过
"""
