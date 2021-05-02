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
    1: [2, 3, 4],
    2: [1, 4],
    3: [1, 4],
    4: [1, 2, 3]
}


# DFS
# 완전이진트리가 아닌 정점이나 인접노드가 여러개인 그래프 등
# 모두 적용가능한 코드필요
# stack 이용
# pop, extend

def dfs(graph, root_node):
    #시작노드
    stack = [root_node]
    result = []

    while stack:
        #이후 반복문을 돌리기 위한 요소 : 부모노드

        parent_node = stack.pop()

        #방문한 시점에서 결과리스트에 추가
        #자식노드는 stack에 추가

        if parent_node not in result:
            result.append(parent_node)
            children = graph[parent_node]
            #탐색은 낮은 숫자부터 진행하기위해
            #리스트의 마지막 숫자가 가장 작아야 한다(내림차순)
            #stack에 추가하기전에 자식노드 재배열
            children.reverse()
            #재배열후 stack에 추가
            stack.extend(children)


    return result

# BFS
# 완전이진트리가 아닌 정점이나 인접노드가 여러개인 그래프 등
# 모두 적용가능한 코드필요
# Queue 이용
# dequeue, extend
# dequeue = pop(0)

def bfs(graph, root_node):
    #시작노드
    queue = [root_node]
    result = []

    while queue:
        #이후 반복문을 돌리기 위한 요소 : 부모노드
        #bfs는 queue에서 pop
        parent_node = queue.pop(0)

        #방문한 시점에서 결과리스트에 추가
        #자식노드는 stack에 추가

        if parent_node not in result:
            result.append(parent_node)
            children = graph[parent_node]
            # 탐색은 낮은 숫자부터 진행하기위해
            # 리스트의 첫번째 숫자가 가장 작아야 한다(오름차순)
            # stack에 추가하기전에 자식노드 재배열
            children.sort()
            #재배열후 queue에 추가
            queue.extend(children)


    return result




print(dfs(graph, 1))
print(bfs(graph, 1))
