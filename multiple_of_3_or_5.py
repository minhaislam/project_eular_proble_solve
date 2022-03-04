import math

value =1
sum_of_value = 0

while value<1000:
    if value%3 == 0 or value%5 ==0:
        sum_of_value = sum_of_value+value

    value=value+1

print(sum_of_value)
