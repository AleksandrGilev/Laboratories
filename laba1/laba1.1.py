oklad = input('oklad:')

while True:
    if oklad.isdigit():
        oklad = int(oklad)
        pr = oklad * 13 / 100
        break
    else:
        print('mistake')
        oklad = input('oklad:')

print('kvart_prem:', oklad * 2 / 3)
print('na_ryki:', oklad - pr)
