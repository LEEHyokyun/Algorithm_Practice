# d(n) = n + n//10 + n%10
# 이때 n을 d(n)의 생성자라 하며, 생성자가 없는 숫자를 self Number라 한다.
# 규칙성도 있는데, 10K보다 작은 숫자들을 배열에 저장하고
# 생성자에 해당하는 숫자를 출력하지않는 방식으로 로직구현

n = 10000
array_test_case = []

for i in range(n):
    array_test_case.append(i + i // 10 + i % 10)

for j in range(n):
    if j not in array_test_case:
        print(j)
    else:
        continue




