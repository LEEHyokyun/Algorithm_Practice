import sys
import math

T = int(sys.stdin.readline())
array_for_test = []
for i in range(T):
    array_for_test.append(int(sys.stdin.readline()))

def merge_sort(left_side, right_side):

    left = 0
    right = 0
    result = []

    while left < len(left_side) and right < len(right_side):
        if left_side[left] < right_side[right]:
            result.append(left_side[left])
            left = left + 1
        else:
            result.append(right_side[right])
            right = right + 1

    #left_side와 right_side 중 하나는 반드시 모두 정렬이 완료
    #두 배열중 빈상태가 아니더라도 이미 정렬이 된 상태로, 그대로 이어붙여주면 된다.
    #result = result + left_side[left:]방식도 되지만
    #메소드를 이용하여 붙이도록한다.
    result.extend(left_side[left:])
    result.extend(right_side[right:])

    return result

def dividing(array_for_test):
    #별도 else문 작성없이 if문으로 기본조건을 기재
    if len(array_for_test) == 0 or len(array_for_test) == 1:
        return array_for_test

    mid = len(array_for_test) // 2
    #위 조건으로부터 array_for_test는 요소가 1이될때까지 반복한다.
    #left_side에는 왼쪽요소, right_side에는 오른쪽요소가 저장
    left_side = dividing(array_for_test[:mid])
    right_side = dividing(array_for_test[mid:])

    return merge_sort(left_side, right_side)

for i in dividing(array_for_test):
    print(i)
