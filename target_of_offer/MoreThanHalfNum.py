"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数
组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        num = numbers[0]
        left = [n for n in numbers[1:] if n <= num]
        right = [n for n in numbers[1:] if n > num]
        sorted = left + [num] + right
        num_pos = len(left)
        mid_pos = len(sorted) // 2
        if num == sorted[mid_pos]:
            return num
        elif num < sorted[mid_pos]:

"""
需要一个映射，反映递归的相对位置和实际在整个list中的位置，
便于定位mid_pos
"""
