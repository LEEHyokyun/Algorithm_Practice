# T = test case
# x y = 각 지점
# 최초 작동시엔 이론상 -1 , 0 , 1 가능하며 실제론 반드시 1
# 최종 지점 도착 직전 마지막 이동거리는 반드시 1
# 작동장치횟수의 최소값

# 최소횟수는 최대한 큰 거리를 가야한다.

# 1씩가도 작동횟수의 최대는 두 지점사이의 거리

import sys

T = int(sys.stdin.readline())

array_test_case = []
for i in range(T):
    array_test_case.append(list(map(int, sys.stdin.readline().split())))

def get_minimum_value(T, array_test_case):

    result = []

    array_steps = []
    array_possible_steps = []

    i = 0
    while i < T:
        length = array_test_case[i][1] - array_test_case[i][0]
        array_possible_steps.clear()
        array_steps.clear()
        for j in range(length):
            if sum(array_steps) < length:
                break
            else:
                if j == 0:
                    array_steps.append(1)
                    array_possible_steps.append(1)
                    continue
                else:
                    before_final_step = array_possible_steps.pop()
                    array_steps.append(before_final_step + 1)
                    array_possible_steps.append(array_steps[j])
        print(result)

    i = i + 1




get_minimum_value(T, array_test_case)