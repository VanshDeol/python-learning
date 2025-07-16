from itertools import product

k , m = map(int, input().split())

max_modulo = 0
all_elements =[]
while k > 0:
    size , *elements = map(int,input().split())
    all_elements.append(elements)
    k -= 1
    
    
all_combinations =list(product(*all_elements))
for combinations in all_combinations:
    op = sum([x**2 for x in combinations]) % m 
    if op > max_modulo:
        max_modulo = op


print(max_modulo)

