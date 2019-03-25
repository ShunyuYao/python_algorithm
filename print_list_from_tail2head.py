# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode == None:
            return []
        val_list = []
        head = listNode
        # 如果链表是一个环怎么办？
        while head:
            val_list.insert(0, head.val)
            head = head.next
        return val_list
