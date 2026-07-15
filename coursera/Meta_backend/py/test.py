def summation(n):
   if n == 1:
       return 0
   return n + summation(n-1)

a = summation(5)
print(a)