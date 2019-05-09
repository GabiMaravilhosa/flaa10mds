n = 0
pa = 0
pr = 0
while n < 10:
    num = int(input("digite um numero: "))
    if (num % 2 )== 0:
        pa = pa + num
    elif num % num == 0 and num % 1 == 0 :
        pr = pr + num
    n += 1
print (" a soma dos números pares é", pa)
print(" a soma dos números primos é", pr)
        
