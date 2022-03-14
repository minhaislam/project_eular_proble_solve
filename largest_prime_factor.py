
# import numpy as np

def check_prime(in_value):
    prime =in_value
    if prime> 1:
        for j in range(2,prime):
            # print(j)
            if prime%j ==0:
                return False
        return True
    else:
        return False


def ret_list(in_value):
    list_l =[]
    value =in_value
    i=3
    while i<value:
        if check_prime(i) ==True and value%i ==0 and i%2 !=0:
            # print(i)
            value=value/i
            # print(value)
            list_l.append(i)
        i=i+1
        # value=value/i
    list_l.append(value)
    return list_l

print(f'Largest Prime Factor: {max(ret_list(600851475143))}')

print(np.prod(ret_list(600851475143)))

