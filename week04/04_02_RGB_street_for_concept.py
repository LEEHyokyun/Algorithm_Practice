#집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
#각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 차례로 쓰여진다.
#맞닿아있는 집들은 서로 다른 색이어야 한다.

# 모든 집에 대해 최솟값을 가지는 색깔을 선택할수는 없으며
# 색깔중복조건에 부합하면서 최소값을 선택해도 그 값이 최솟값이라는 보장이 없기 때문에
# 모든 경우의 수를 비교하면서 진행해야 한다.
# 모든 노드에 대해 탐색은 하지 않기 때문에 BFS 및 DFS 사용불가
# 동적계획법을 이용하여 이전 선택한 값을 누적하면서 최소값을 나열한후 구해보자.


each_house_value = [
 [26, 40, 83],
 [49, 60, 57],
 [13, 89, 99]
]

def get_minimum_value(RGB_array, N):

    result = memoization(RGB_array, N)

    return result

def memoization(RGB_array, N):

    for j in range(3):

        before_index = j

        for i in range(N):

            value = RGB_array[i][j]
            if j == before_index:
                value = value + min(RGB_array[i][j-1], RGB_array[i][j+1])
            else:
                value = value + RGB_array[i][j]
                print(value)





get_minimum_value(each_house_value, 3)



