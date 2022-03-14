


   
def palindrom_product(in_value):
    list_l =in_value
    l = 0
    i=0
    j=0
    string = '1'
    while l<list_l:
        string=string+'0'
        # print(l)
        l=l+1
    
    value = int(string)-1
    j =int(string)-1
    while j<int(string):
        if int(len(str(j)))==list_l:
            product_p = value*j
            reversed_product = str(product_p)[::-1]
            print(product_p)
            print(reversed_product)
            if product_p==int(float(reversed_product)) and len(str(product_p))==len(reversed_product):
                print(product_p)
                break
        j=j-1


print(f'Largest palindrom Product: {palindrom_product(3)}')


