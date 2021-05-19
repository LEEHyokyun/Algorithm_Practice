# N이 주어졌을때
# 연산후 다시 N이 될때까지
# 사이클 출력

import sys

N = int(sys.stdin.readline())

def get_the_number_of_cycle(N):

    new_N = (N % 10) * 10 + ((N // 10) + (N % 10)) % 10

    if new_N == N:
        return 1
    else:
        i = 1
        while new_N is not N:
            i = i + 1
            new_N = (new_N % 10) * 10 + ((new_N // 10) + (new_N % 10)) % 10

    return i

get_the_number_of_cycle(N)
print(get_the_number_of_cycle(N))