#첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 6
# 2 5 3 7 8 1
# 평균은 4
# 2 3 1
# 평균은 2
# 2 1
# 평균은 1.5
# 1
# 1 적고 > 2 적고 > 3 적으면 배열의 반은 완성.

# 1. 숫자입력후 배열생성
# 2. 입력받은 숫자의 평균값 산출
# 3. 평균값을 기준으로

#조건입력
RepeatNumber = int(input('RepeatNumber? '))
print(RepeatNumber)

i = 0
sum = 0
InputArray = []

#조건입력
while i < RepeatNumber:
    number = int(input('number? '))
    i = i + 1
    InputArray.append(number)

j = 0
sum = 0
for j in range(InputArray):
    sum = sum + j
print(sum)



