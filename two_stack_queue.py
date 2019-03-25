"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。
队列中的元素为int类型。

备注：如果输入错误示例——在空的队列中使用pop方法，
其异常交给python本身来处理：
IndexError: pop from empty list
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)
        val = self.stack2.pop()
        return val

if __name__ == '__main__':
    sol = Solution()
    sol.push(2)
    sol.push(3)
    print(sol.pop())
