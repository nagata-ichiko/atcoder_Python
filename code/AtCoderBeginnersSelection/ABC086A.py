# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
b, c = map(int, input().split())

num = b*c

if  num % 2 == 0 :
    print("Even")
    
else :
    print("Odd")

