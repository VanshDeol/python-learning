set_a = set(map(int, input().split()))

num = int(input())

result = True

while num >= 1:
    other_set = set(map(int, input().split()))
    
    result = result and set_a.issuperset(other_set)
    
    num -= 1

print(result)
