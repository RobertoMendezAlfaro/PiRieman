#!/usr/bin/env python
def riemann(a,b,n,func):
    return func
#resultado
sum = 0.0

a = 0
b = 1
n = 6
x = ((a+b/n)/2)

#ecuación a calcular
func = 1/(1+x**2)

for rec in range(n-1):
   # riemann
   # x += b/n
    sum = func + sum
    x += b/n

print(sum)
