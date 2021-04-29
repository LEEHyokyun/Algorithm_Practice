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
    1: [2, 4, 3],
    2: [1, 4],
    3: [1, 4],
    4: [1, 3, 2]
}


# DFS
# 완전이진트리가 아닌 정점이나 인접노드가 여러개인 그래프 등
# 모두 적용가능한 코드필요
# stack 이용

def dfs(graph, root_node):
    stack = [root_node]
    result = []

    while stack:

        parent_node = stack.pop()
        children = graph[parent_node]
        children_node = children.map()

        if children_node not in result:
            result.append(parent_node)
            stack.extend(graph[parent_node])

    return result


print(dfs(graph, 1))
