
def sum_square_difference(range_value):
    list_of_sum = [i for i in range(1,range_value+1)]
    list_of_sum_square=[i**2 for i in range(1,range_value+1)]
    difference_of_value = (sum(list_of_sum)**2)-sum(list_of_sum_square)
    print(difference_of_value)

sum_square_difference(100)

# c=1

# while j<=20:
#     c=j*c
#     j=j+1

# print(c)