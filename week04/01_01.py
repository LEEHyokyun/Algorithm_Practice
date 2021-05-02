#https://coding-all.tistory.com/2
#https://kamang-it.tistory.com/entry/AlgorithmDynamic-Programming%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EA%B3%BC-%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98memoization-%ED%83%80%EB%B7%B8%EB%A0%88%EC%9D%B4%EC%85%98tabulation

# 동적계획법

# 큰 문제를 작은 문제로 나눠서 푼다 TOP DOWN
# 메모이제이션(memoization) 이전 결과르 저장하며, 저장한 결과를 활용한다
# 분할정복과 정의 자체는 동일하지만 저장한다는 개념에서 차이

# 작은 문제를 풀어나가면서 큰 문제를 해결한다 DOWN TOP
# 타뷸레이션(Tabulation) for 문을 이용한 반복문으로 값을 모두 구해나간다
# 오버헤드가 나타날 수 있지만 모든 값(연산)을 구하는 측면에서는 유리

# 기존 삼각형에서 누적되는 문제이므로, 메모이제이션으로 풀어야 효율적일것이다.

# T = the number of test case
# N = element number


# 규칙성을 찾은 후에 코드로 구현해보자