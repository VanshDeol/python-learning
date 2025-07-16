

n = int(input())
eng = set(map(int, input().split()))

m = int(input())
fren = set(map(int, input().split()))

print(len(eng.symmetric_difference( fren)))

