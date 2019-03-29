"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
# to do: 该实现引入了辅助空间，其实可以直接获得index索引
# 代码仍有BUG，右子树的索引有问题
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        print(sequence)
        length = len(sequence)
        if length < 1:
            return False
        elif length == 1:
            return True
        else:
            root = sequence[-1]
            left_nodes = []
            right_nodes = []
            sequence.pop()
            for i in range(length):
                index = i
                if sequence[index] <= root:
                    left_nodes.append(sequence[index])
                else:
                    break

            for j in range(i, len(sequence)):
                if sequence[j] > root:
                    right_nodes.append(sequence[j])
                else:
                    return False

            result_l = self.VerifySquenceOfBST(left_nodes)
            result_r = self.VerifySquenceOfBST(right_nodes)

        if result_l and result_r:
            return True
        else:
            return False

if __name__ == '__main__':
    seq = [5, 8, 6, 11, 17, 12, 9]
    seq1 = [4, 6, 7, 5]
    S = Solution()
    result = S.VerifySquenceOfBST(seq1)
    print(result)
