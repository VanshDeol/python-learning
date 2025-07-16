from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for p in product(a,b):
    print(p,end=' ')
    
#-----OR----
    
#print(*list(product(a,b)))
