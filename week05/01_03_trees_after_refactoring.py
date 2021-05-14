#첫째줄에
#나무의 수 N
#나무의 길이 M

#둘째줄에
#나무의 높이 배열

#적어도 M의 길이이상의 나무를
#가져가기위한 절단기를 설정할 수 있는 높이의 최댓값

# 1. 절단기로 자른 후의 나무의 남은 길이를 배열로 만들고
# 2. 해당 배열의 수로 M이상의 수를 만들 수 있을때까지
# 3. 절단기의 높이로 자르고, 남은 나무 기둥의 길이가 M이상이면 가능
# 4. 절단기 높이에 대한 반복으로 최대값 구하기

# 경우의 수는 1부터 N까지

import sys

N, M = map(int, sys.stdin.readline().split())
tree_height = list(map(int, sys.stdin.readline().split()))

def get_max_H (N, M, tree_height):

    tree_height_after_cut = []
    H = 0

    while H < max(tree_height):
        H = H + 1

        # 나무절단후 남아있는 나무의 길이를 배열에 저장하는 함수
        get_tree_height_after_cut(H, N, tree_height, tree_height_after_cut)

        # 남아있는 나무의 길이로 최소길이 M을 만들수있는 절단기의 최대길이를 반환해주는 함수
        print(H)

        if sum(tree_height_after_cut) < M:
            return H - 1
            break
        else:
            tree_height_after_cut.clear()
            continue


def get_tree_height_after_cut(H, N, tree_height, tree_height_after_cut):
    for i in range(N):
        if tree_height[i] > H:
            tree_height_after_cut.append(tree_height[i] - H)
        else:
            tree_height_after_cut.append(0)

get_max_H(N, M, tree_height)
print(get_max_H(N, M, tree_height))