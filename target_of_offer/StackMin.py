"""
题目描述
定义的栈数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minStack == [] or node < self.minStack[-1]:
            self.minStack.append(node)
        else:
            self.minStack.append(self.min())

    def pop(self):
        # write code here
        if len(self.stack) > 0 and len(self.minStack) > 0:
            element_pop = self.stack.pop()
            self.minStack.pop()
        else:
            return None
        return element_pop

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]

if __name__ == '__main__':
    S = Solution()
    S.push(3)
    S.push(4)
    S.push(2)
    S.push(1)
    print(S.min())
    S.pop()
    print(S.min())
    S.pop()
    print(S.min())
