#집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
#각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 차례로 쓰여진다.
#맞닿아있는 집들은 서로 다른 색이어야 한다.

# 모든 집에 대해 최솟값을 가지는 색깔을 선택할수는 없으며
# 색깔중복조건에 부합하면서 최소값을 선택해도 그 값이 최솟값이라는 보장이 없기 때문에
# 모든 경우의 수를 비교하면서 진행해야 한다.
# 모든 노드에 대해 탐색은 하지 않기 때문에 BFS 및 DFS 사용불가
# 동적계획법을 이용하여 이전 선택한 값을 누적하면서 최소값을 나열한후 구해보자.

#각 집에 칠하는 색깔을 배열로 구현하기 위해 일반화 필요
each_house_value = [
 [26, 40, 83], [49, 60, 57], [13, 89, 99]
]

#색깔의개수와 집의수(N)에 따른 일반화 필요
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

#결과저장
result_array = []



def get_minimum_value(each_house_value, color, N):

    #첫번째집 색깔을 선택한 이후에 나올 수 있는 비용의 경우의 수를 모두 구한 딕셔너리
    #해당 딕셔너리를 만드는 함수
    hash_table = get_hash_table(N, color, each_house_value)

    #위에서 구한 딕셔너리에서 가능한 경우에 대한 비용만 결과배열에 추가하여
    #결과배열중 최솟값을 구하는 함수
    result = get_result_from_hash_table(N, hash_table)

    return result

def get_hash_table(N, color, each_house_value):
    if color == 1:
        for k in range(N):
            if k + 1 < N:
                for i in range(N):
                    for j in range(N):
                        value = 26 + each_house_value[k][i] + each_house_value[k+1][j]
                        hash_table[color][i+1][j+1] = value
            else:
                break
    print(hash_table)
    return hash_table


def get_result_from_hash_table(N, hash_table):
    for i in range(N):
        for j in range(N):
            if i == 0 or i == j:
                hash_table[1][i + 1][j + 1] = 0
                continue
            else:
                result_array.append(hash_table[1][i + 1][j + 1])
                continue
    result = min(result_array)
    return result

get_minimum_value(each_house_value, 1, 3)
print(get_minimum_value(each_house_value, 1, 3))