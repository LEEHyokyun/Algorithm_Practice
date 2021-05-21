# T = test case
# x y = 각 지점
# 최초 작동시엔 이론상 -1 , 0 , 1 가능하며 실제론 반드시 1
# 최종 지점 도착 직전 마지막 이동거리는 반드시 1
# 작동장치횟수의 최소값



import sys

T = int(sys.stdin.readline())

array_test_case = []
for i in range(T):
    array_test_case.append(list(map(int, sys.stdin.readline().split())))

def get_minimum_value(T, array_test_case):

    result = []

    for i in range(T):
        length = array_test_case[i][1] - array_test_case[i][0]

        max_length_for_each_operation = []

        for j in range(length):

            if j == 0:
                max_length_for_each_operation.append(0)
            elif j == 1:
                max_length_for_each_operation.append(1)
            else :
                max_length_for_each_operation.append(max(max_length_for_each_operation) + j//2)
                if max(max_length_for_each_operation) < length:
                    continue
                else:
                    print(j)
                    break

get_minimum_value(T, array_test_case)