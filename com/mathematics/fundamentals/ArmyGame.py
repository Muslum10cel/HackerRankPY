import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

suplly_for_row = (n // 2) + (n % 2)
suplly_for_col = (m // 2) + (m % 2)

print(suplly_for_row * suplly_for_col)
