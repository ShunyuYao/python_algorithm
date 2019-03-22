import time
inf = float('inf')

# ATT: this implentation will not go through all nodes
# sometimes and cause local minium
def find_mini_path(graph, dist_map):
    road = ['start_point']
    next_node = ''
    cur_node = 'start_point'
    while cur_node != 'final_point':
        mini_dist = inf
        for dst_node in graph[cur_node].keys():
            dist = dist_map[cur_node] + graph[cur_node][dst_node]
            if dist < dist_map[dst_node]:
                dist_map[dst_node] = dist
            if dist < mini_dist:
                mini_dist = dist
                next_node = dst_node
        cur_node = next_node
        road.append(cur_node)
    return road


def find_path(parents):
    node = 'final_point'
    path = [node]
    while node != 'start_point':
        p_node = parents[node]
        node = p_node
        path.append(node)
    return path


def find_lowest_cost_node(costs, processed):
    mini_cost = inf
    lowest_cost_node = None
    for node in costs.keys():
        # print(node)
        cost = costs[node]
        # print(processed)
        # time.sleep(1)
        if cost < mini_cost and node not in processed:
            mini_cost = cost
            costs[node] = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijk_search(graph, parents, costs):
    processed = []
    cur_node = find_lowest_cost_node(costs, processed)
    print(cur_node)
    while cur_node != None:
        for neighbor_node in graph[cur_node].keys():
            dist = costs[cur_node] + graph[cur_node][neighbor_node]
            if dist < costs[neighbor_node]:
                costs[neighbor_node] = dist
                parents[neighbor_node] = cur_node
        if cur_node not in processed:
            processed.append(cur_node)
            print(processed)
            time.sleep(1)
        cur_node = find_lowest_cost_node(costs, processed)
        path = find_path(parents)
    return path

if __name__ == '__main__':
    graph = {}
    graph['start_point'] = {'a': 6, 'b': 2}
    graph['a'] = {'final_point': 1}
    graph['b'] = {'a': 3, 'final_point': 5}
    graph['final_point'] = {}

    parents = {}
    parents['a'] = 'start_point'
    parents['b'] = 'start_point'

    costs = {'a': 6, 'b': 2, 'final_point': inf}
    path = dijk_search(graph, parents, costs)
    print(path)
    # print(output_parents)
