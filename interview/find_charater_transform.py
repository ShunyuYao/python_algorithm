"""
某CV公司面试题目:
给定一个字符串列表(["dog", "dot", "fog", "hot", "dig", "lot", "lit"])，
定义一种变换，该变换可以让列表中任意一个字符串改变一个字母，变为列表中另一个字符，
比如"dog" -> "fog"(d变f)，"dot" -> "lot" (d变l)
从这两个字符列表当中任取两个字符A和B（比如dog和lag），求A到B的最短变换路径长度。

输入：两个个字符串A和B
输出：A到B变换的最短路径长度
"""
from collections import deque

def find_root(parent_dict, char_A, char_B):
    char = char_B
    path = [char]
    while char != char_A:
        char = parent_dict[char]
        path.insert(0, char)
    return path

def find_character_transform(char_A, char_B, graph):
    find = False
    processed = []
    queue = deque(graph[char_A])
    parent = {ch: char_A for ch in graph[char_A]}
    while queue:
        char = queue.popleft()
        if char not in processed:
            processed.append(char)
            if char == char_B:
                find = True
                continue
            else:
                queue += graph[char]
            for ch in graph[char]:
                if ch not in processed:
                    parent[ch] = char
    return find, parent

if __name__ == '__main__':
    graph = {}
    graph['dog'] = ['dot', 'fog', 'dig']
    graph['dot'] = ['dog', 'hot', 'lot']
    graph['fog'] = ['dog']
    graph['hot'] = ['dot', 'lot']
    graph['dig'] = ['dog']
    graph['lot'] = ['dot', 'hot', 'lit']
    graph['lit'] = ['lot']
    char_A = 'dog'
    char_B = 'lit'
    find, parent = find_character_transform(char_A, char_B, graph)

    if find:
        path = find_root(parent, char_A, char_B)

"""
思路：
先把每个可能的变换用一个图来表示，然后用广度优先遍历即可,
注意要使用列表processed来存放已遍历过的节点，防止死循环，
最后用一个字典来存放父节点，以便于记录找到的路径
"""
