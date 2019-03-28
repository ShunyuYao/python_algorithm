# -*- coding:utf-8 -*-
# 关键在于写出`f(n+2) = f(n) + f(n+1)`的前向公式
# 此题目如果用`f(n) = f(n-1) + f(n-2)`的递归会导致不必要的内存消耗
# 因为每次都有数字重叠
class Solution:
    def Fibonacci(self, n):
        # write code here
        assert n >= 0
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fn0 = 0
            fn1 = 1
            for i in range(n-1):
                fn2 = fn0 + fn1
                fn0 = fn1
                fn1 = fn2
        return fn2
