"""
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断
第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有
数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序
列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2
就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) == 0 or len(popV) == 0:
            return False
        stack = []
        i = 0
        pop_num = popV[i]
        for num in pushV:
            stack.append(num)
            print(stack)
            while pop_num == stack[-1]:
                stack.pop()
                i += 1
                if i < len(popV):
                    pop_num = popV[i]
                else:
                    break
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [2, 4, 3, 5, 1]
    stack = Solution().IsPopOrder(pushV, popV)
    print(stack)

"""
思路：
先一直push到可以pop为止
然后一直pop到不可以pop，再接着pop，如此循环。
如果最后stack为空，那么说明弹出序列可行。
"""
