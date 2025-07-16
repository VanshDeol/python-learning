# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
eng = set(map(int, input().split()))

m = int(input())
fren = set(map(int, input().split()))

print(len(eng - fren))

