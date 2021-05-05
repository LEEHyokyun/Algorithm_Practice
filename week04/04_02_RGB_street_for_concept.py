#집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
#각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 차례로 쓰여진다.
#맞닿아있는 집들은 서로 다른 색이어야 한다.

# 모든 집에 대해 최솟값을 가지는 색깔을 선택할수는 없으며
# 색깔중복조건에 부합하면서 최소값을 선택해도 그 값이 최솟값이라는 보장이 없기 때문에
# 모든 경우의 수를 비교하면서 진행해야 한다.
# 모든 노드에 대해 탐색은 하지 않기 때문에 BFS 및 DFS 사용불가
# 동적계획법을 이용하여 이전 선택한 값을 누적하면서 최소값을 나열한후 구해보자.

RGB = 3
each_house_value = [
 [26, 40, 83],
 [49, 60, 57],
 [13, 89, 99]
]

def get_minimum_value(RGB_array, N, first_color):

    # 색깔을 받아서 첫번째 배열상의 value 값과 인덱스 값을 받아오기
    for value in RGB_array[0]:
        if value == first_color:
            first_value = value
            first_index = RGB_array[0].index(value)
        else:
            continue

    values = [[0] * 3] * (2 ** (N - 1))
    index = [0]

    #결과값 구하기
    result = memoization(RGB_array, N, first_value, first_index, values, index)

    return result

def memoization(RGB_array, N, first_value, first_index, values, index):

    # 첫번째 경우가 정해졌을때 가능한 가지의 수는 2^(N-1)가지
    # 모든 경우의 수를 저장하기위해 그만한 크기의 이중배열을 생성
    for i in range(2 ** (N - 1)):
        values[i][0] = first_value

    index.pop()
    index.append(first_index)

    for i in range(1, N): # i = 1, 2 (N-1까지 반복)
        before_index = index.pop()

        for j in range(RGB):
            if j == before_index:
                continue
            elif j != before_index and values[j][i] != 0:
                continue
            elif j != before_index and values[j][i] == 0 :
                while k < (RGB - 1):
                values[j][i] = RGB_array[i][j]
                index.append(j)
                print(index)
        print(values)


get_minimum_value(each_house_value, RGB, 26)


