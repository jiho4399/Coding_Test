# 백준 5532번 : 방학 숙제

import math
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(L - (max(math.ceil(B/D), math.ceil(A/C))))