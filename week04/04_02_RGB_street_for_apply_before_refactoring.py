#집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
#각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 차례로 쓰여진다.
#맞닿아있는 집들은 서로 다른 색이어야 한다.

# 모든 집에 대해 최솟값을 가지는 색깔을 선택할수는 없으며
# 색깔중복조건에 부합하면서 최소값을 선택해도 그 값이 최솟값이라는 보장이 없기 때문에
# 모든 경우의 수를 비교하면서 진행해야 한다.
# 모든 노드에 대해 탐색은 하지 않기 때문에 BFS 및 DFS 사용불가
# 동적계획법을 이용하여 이전 선택한 값을 누적하면서 최소값을 나열한후 구해보자.


each_house_value = [
 [26, 40, 83], [49, 60, 57], [13, 89, 99]
]

hash_table = {
    1:{1:{},
       2:{},
       3:{}},

    2:{1:{},
       2:{},
       3:{}},

    3:{1:{},
       2:{},
       3:{}}
}



def get_minimum_value(each_house_value, color, N):

    #첫번째집 색깔을 선택한 이후에 나올 수 있는 비용의 경우의 수를 모두 구한 딕셔너리
    #해당 딕셔너리를 만드는 함수
    #
    if color == 1:
        for i in range(N):
            for j in range(N):
                value = 26 + each_house_value[1][i] + each_house_value[2][j]
                hash_table[1][i+1][j+1] = value

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j or j == k :
                    hash_table[i+1][j+1][k+1] = 0
                    continue
                else :
                    continue
    print(hash_table)
   

    return result




get_minimum_value(each_house_value, 1, 3)
