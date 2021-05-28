# x1 y1
# x2 y2
# x1 y1에 대한 거리 r1
# x2 y2에 대한 거리 r2
# 가능한 x y 좌표의 수

#각 테스트케이스마다 x,y의 경우의 수 출력
#무한대일 경우에는 -1
import sys

Test_case = int(sys.stdin.readline())

for i in range(Test_case):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    length_between_center_of_circle = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    inner_contact_distance = abs(r1 - r2)
    outer_contact_distance = abs(r1 + r2)

    # 중심이 같을때 (서로 같은 원일때/ 다른원일때)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    # 중심이 다를때 (내접/외접/두 지점이 만날때/만나지않을때)
    else:
        if length_between_center_of_circle == inner_contact_distance:
            print(1)
        elif length_between_center_of_circle == outer_contact_distance:
            print(1)
        elif length_between_center_of_circle > inner_contact_distance:
            print(2)
        elif length_between_center_of_circle > outer_contact_distance:
            print(0)
