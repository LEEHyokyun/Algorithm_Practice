#DFS
#Depth first search
#깊이우선탐색, 루트노드를 시작으로 깊이우선탐색하여 노드들을 조회하는 방법

#Input : 정점의 개수 - 간선의 개수 - 시작노드
# 1
# 2 3 4
# 4 4

# 깊이탐색은 깊이우선, 1 2 4 3

graph = {
    1: [2, 3, 4],
    2: [4],
    3: [4]
}

def DFS_By_Stack(Input_graph, root_node):

    stack = [root_node]
    visited = []

    #last in first out
    while stack:
        current_node = stack.pop()
        visited.append(current_node)

        for near_node in Input_graph[current_node]:
            if near_node not in visited :
                stack.append(near_node)

    return visited

print(DFS_By_Stack(graph, 1))