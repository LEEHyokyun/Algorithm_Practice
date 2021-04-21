num = 26
num_2 = num//10
num_1 = num%10
num_sum = 0
num_result = 0
count = 0

while num is not None:
    num_sum = num_1 + num_2
    num_result = num_1*10 + num_sum%10
    if num_result == num:
        print(count)
        break
    else :
        count = count + 1

