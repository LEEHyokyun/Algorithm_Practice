

# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
# 10 > 1 3 5 0 0 4 7 0 0 6
# 1+6 = 7
# 10 > 1 0 2 0
# 0의 위치가 어디가 되었든, 반드시 하나 이상의 정수가 선언된 후에 나타난다.


#조건입력
Size_Array = int(input('RepeatNumber? '))
print(Size_Array)

i = 0
j = 0
k = 0

InputArray = []

#반복문 작성
while i < Size_Array:
    number = int(input('number? '))
    if number == 0:
        # 0을 입력했을때 바로바로 숫자제거
        for j in range(len(InputArray)-1):
            if InputArray[i-j-1] != 0:
                InputArray[i-j-1] = 0
                break #숫자제거가 완료되면 반복문 탈출
            else :
                InputArray[i - j - 1] = InputArray[i-j-1]
    i = i + 1
    InputArray.append(number)

#반복문결과 확인
print(InputArray)

#최종결과 도출
sum = 0
for k in range(InputArray):
    sum = sum + int(InputArray[k])
print(sum)
