
size_m = int(input())
m = set(map(int, input().split()))

size_n = int(input())
n = set(map(int, input().split()))

for item in sorted(m^n):
    print(item)















