"""
某CV公司面试题目:
给定一个字符串，求包含这个字符串所有字符的的最小子串位置。
（比如"AAAAAA"的最小子串就是"A"，"ABBAACBADDDCAD"的最小子串就是
"CBAD"，其位置是左5，右8

输入：一个字符串
输出：最小子串的左端点和右端点位置
"""
def min_char_list(char_list):
    char_set = set(char_list)
    char_num = {ch: 0 for ch in char_set}
    aux_set = set()

    for i, char in enumerate(char_list):
        char_num[char] += 1
        aux_set = aux_set | set([char])
        if aux_set == char_set:
            break

    left_pos = min_left_pos = 0
    right_pos = min_right_pos = i
    min_len = right_pos - left_pos + 1

    while right_pos < len(char_list)-1:
        pop_char = char_list[left_pos]
        left_pos += 1
        char_num[pop_char] -= 1
        while char_num[pop_char] == 0 and right_pos < len(char_list)-1:
            right_pos += 1
            char_num[char_list[right_pos]] += 1
        if (right_pos - left_pos + 1) < min_len:
            min_len = right_pos - left_pos + 1
            min_left_pos = left_pos
            min_right_pos = right_pos

    return min_len, min_left_pos, min_right_pos

if __name__ == '__main__':
    string = "ABBAACBADDDCAD"
    print('len string:', len(string))
    min_len, min_left_pos, min_right_pos = min_char_list(string)
    print(min_len, min_left_pos, min_right_pos)

"""
思路：
一种暴力搜索的优化版，先搜索到第一个不重复子串，然后删除最左边的字符，
这时子串有两种情况：
1. 仍然是一个包含所有字符的完整子串
2. 少了被删去的那个字符，子串并不完整
情况2时，我们只要向右搜索直到找到被删去的字符，即可得到一个新的完整子串。
不断删除最左边字符直到字符串尾部，找到最小的完整子串。
"""
