
n_set_a = int(input())
set_a = set(map(int, input().split()))

n_other = int(input())

for i in range (n_other):
    operation , size = input().split()
    size = int(size)
    other_set = set(map(int, input().split()))
    if operation == 'update':
        set_a |= other_set
    
    elif operation == "intersection_update":
        set_a &= other_set
    
    elif operation == 'difference_update':
        set_a -= other_set
    
    elif operation == 'symmetric_difference_update':
        set_a ^= other_set

print(sum(set_a))

