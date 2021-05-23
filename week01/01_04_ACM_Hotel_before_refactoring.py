# T Test case W 각 층별 방의 개수, H 건물높이(층수), N 몇번째 손님
# 걷는 거리가 작은 것이 우선순위, 걷는거리가 같을때엔 아래층의 방을 더 먼저
# 101 > 201 > 301 > 401 > ..... 순서대로 배정

import sys
T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    steps = 1
    height = 1
    width = 1

    while steps < N:
        if height < H and width < W:
            height = height + 1
            steps = steps + 1
            continue

        elif height == H and width < W:
            height = 1
            width = width + 1
            steps = steps + 1
            continue

        elif height < H and width == W:
            height = height + 1
            width = 1
            steps = steps + 1
            continue

        # 코드의 논리적 오류를 최소화 하기위한 형식적 코드
        else:
            pass

    print(height * 100 + width)





