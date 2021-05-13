#첫째줄에
#나무의 수 N
#나무의 길이 M

#둘째줄에
#나무의 높이 배열

#적어도 M의 길이이상의 나무를
#가져가기위한 절단기를 설정할 수 있는 높이의 최댓값

# 1. 절단기로 자른 후의 나무의 남은 길이를 배열로 만들고
# 2. 해당 배열의 수로 M이상의 수를 만들 수 있을때까지
# 3. 절단기의 높이에 대해 경우의 수가 존재하면 +1
# 4. 절단기의 높이에 대해 경우의 수가 없으면 반복문 끝
import sys

N, M = map(int, sys.stdin.readline().split())

tree_height = list(map(int, sys.stdin.readline().split()))

def get_max_H (N, M, tree_height):
    tree_height_after_cut = []
    H = 0

    for i in range(N):
        tree_height_after_cut.append(tree_height[i] - 2)

    print(tree_height_after_cut)


get_max_H(N, M, tree_height)