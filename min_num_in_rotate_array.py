"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如
 数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
  NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# -*- coding:utf-8 -*-
def sequential_search_min(arr):
    min = arr[0]
    for i in arr[1:]:
        if i < min:
            min = i
    return min

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        arr_len = len(rotateArray)
        if arr_len == 0:
            return 0
        left_pos = 0
        right_pos = arr_len - 1
        # 考虑[1,0,1,1,1]和[1,1,1,0,1]是[0,1,1,1,1]的旋转
        if rotateArray[left_pos] < rotateArray[right_pos]:
            return rotateArray[left_pos]

        while (right_pos - left_pos) > 1:
            mid_pos = (left_pos+right_pos)//2
            left = rotateArray[left_pos]
            right = rotateArray[right_pos]
            mid = rotateArray[mid_pos]
            # 下面这两个判断条件很重要
            # 请思考为什么这么写（大于大的，小于小的）
            # 如果把下面一行改为 `mid > left` 则在牛客网上会超时
            # 但是如果条件改为`mid >= left`和`mid <= right`那么不会超时
            # 必须特别注意大于等于和小于等于的区别
            if mid > right:
                left_pos = mid_pos
            elif mid < left:
                right_pos = mid_pos
            elif rotateArray[left_pos] == rotateArray[mid_pos] and \
                 rotateArray[mid_pos] == rotateArray[right_pos]:
                return sequential_search_min(rotateArray)
            print(left_pos, mid_pos, right_pos)
        return rotateArray[right_pos]


if __name__ == '__main__':
    sol = Solution()
    rotateArray = [3, 4, 5, 1, 2]
    rotateArray1 = [3, 2]
    rotateArray2 = [2]
    rotateArray3 = []
    rotateArray4 = [1, 0, 1, 1, 1]
    min_val = sol.minNumberInRotateArray(rotateArray4)
    print(min_val)
