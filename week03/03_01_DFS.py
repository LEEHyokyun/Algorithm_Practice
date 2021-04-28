# DFS
# Depth first search
# 깊이우선탐색, 루트노드를 시작으로 깊이우선탐색하여 노드들을 조회하는 방법

# Input : 정점의 개수 - 간선의 개수 - 시작노드
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 깊이탐색은 깊이우선, 1 2 4 3

# 숫자를 입력받았을때 이를 그래프로 구현하는 로직

# 먼저 그래프부터 만들기
graph = {
    1: [4, 2, 3],
    2: [4, 1],
    3: [4, 1],
    4: [1, 2, 3]
}

#DFS
def dfs_by_stack(Input_graph, root_node):

    stack = [root_node]
    visited_node = []

    # last in first out
    while stack:
        current_node = stack.pop()
        visited_node.append(current_node)

        for near_node in Input_graph[current_node]:
            if near_node not in visited_node:
                stack.append(near_node)


    return visited_node


print(dfs_by_stack(graph, 1))
