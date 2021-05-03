# 동적계획법

# 큰 문제를 작은 문제로 나눠서 푼다 TOP DOWN
# 메모이제이션(memoization) 이전 결과르 저장하며, 저장한 결과를 활용한다
# 분할정복과 정의 자체는 동일하지만 저장한다는 개념에서 차이

# 작은 문제를 풀어나가면서 큰 문제를 해결한다 DOWN TOP
# 타뷸레이션(Tabulation) for 문을 이용한 반복문으로 값을 모두 구해나간다
# 오버헤드가 나타날 수 있지만 모든 값(연산)을 구하는 측면에서는 유리

# 기존 삼각형에서 누적되는 문제이므로, 메모이제이션으로 풀어야 효율적일것이다.

# T = the number of test case
# N = index

#변수 N을 입력받아 결과를 반환해주는 로직
def P(N):
    array_memoization = [0] * (N + 1)

    result = Dynamic_programming(array_memoization)[N]

    return result

#동적계획법을 구현하는 로직
def Dynamic_programming(array_memoization):
    i = 0
    while i < (len(array_memoization)):
        if i == 0:
            array_memoization[i] = 0
        elif i == 1:
            array_memoization[i] = 1
        elif i == 2:
            array_memoization[i] = 1
        elif i == 3:
            array_memoization[i] = 1
        elif i == 4:
            array_memoization[i] = 2
        else:
            array_memoization[i] = array_memoization[i - 5] + array_memoization[i - 1]
        i = i + 1

    return array_memoization

print(P(6))
print(P(12))