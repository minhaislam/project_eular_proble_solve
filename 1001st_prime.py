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


def nth_no_of_prime(range_prime):

    i=1
    c=0
    k=1
    list_of_prime=[]
    while k>0:
        if check_prime(k)==True:
            list_of_prime.append(k)
            c=c+1
            
            if c==range_prime:
                return k
                break
        k=k+1          

print(nth_no_of_prime(10001))


