import math

previous_value =0
latest_value = 1

final_value = 0

in_range =4

i=0
fib_value = 0

list_of_fibonacci = []

while i>=0:
    if i==0:
        print(previous_value)
        list_of_fibonacci.append(previous_value)
    elif  i== 1:
        print(latest_value)
        list_of_fibonacci.append(latest_value)
    else:
        final_value = latest_value+previous_value
        if final_value<4000000:
            print(final_value)
            list_of_fibonacci.append(final_value)
            previous_value = latest_value
            latest_value=final_value
        else:
            break

    i = i+1


print(sum([i for i in list_of_fibonacci if i%2==0]))