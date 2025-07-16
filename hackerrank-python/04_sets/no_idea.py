# Enter your code here. Read input from STDIN. Print output to STDOUT
n , m = input().split()
n = int(n)
m = int(m)
#print(type(n))
#print(m)

array = list(map(int,input().split()))

a = set(map(int,input().split()))

b = set(map(int,input().split()))

#print(a)

happiness = 0

for i in array:
    if i in a:
        happiness += 1
    elif i in b:
        happiness += -1

print(happiness)



