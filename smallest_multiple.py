
# i=21
# j=1
# c=0

# range_value =20
# print(i)
def smallest_multiple(range_value):
    i=range_value+1
    j=1
    c=0
    while i>range_value:
        # print(i)
        while j<=range_value:
            # print(i)
            if i % j==0 and i%range_value==0 and i%(range_value-1)==0:
                # print(i)
                c=c+1
                
            else:
                pass
            # print(j)
            j=j+1
        # print(i)
        if c==range_value:
            # print(c)
            print(i)
            break
        else:
            c=0 
            i=i+1
            j=1


smallest_multiple(19)

# c=1

# while j<=20:
#     c=j*c
#     j=j+1

# print(c)