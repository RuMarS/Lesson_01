#brute force
"""n = int(input())
x = 2 #кандидат в делители
while (x<= n):
    if n%x == 0:
        print(x)
        break
    else:
        x+=1"""

import math
n = int(input())
if n%2 == 0:
    print(2)
else:
    x = 3 #первый кандидат в делители
    # 12 -> 2   3   4    6     -> 2*6   3*4   4*3   6*2
    while x<= math.sqrt(n):
        if n%x==0:
            print(x)
            break
        else:
            x+=2 #берем след нечетное число
    else: #для while, сюда попадаем, если while закончился не по break
        #число простое, делителей от 3 до math.sqrt(n) нет, т.е. само число - мин натур делитель
        print(n)


