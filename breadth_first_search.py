from collections import deque

def judge_func(input):
    assert isinstance(input, str)
    if input[-1] == 'm':
        return True
    else:
        return False

def breadth_first_search(graph, search_queue):
    searched = []
    while search_queue:
        element = search_queue.popleft()
        if element in searched:
            continue
        else:
            searched.append(element)
        result = judge_func(element)
        if result:
            print('find {}!'.format(element))
            return element
        else:
            search_queue += graph[element]
    return False

if __name__ == '__main__':
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["claire"] = ['jonny', 'thom']
    graph['alice'] = ['peggy']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    search_queue = deque()
    search_queue += graph['you']
    result = breadth_first_search(graph, search_queue)
    print(result)
