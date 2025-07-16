# Enter your code here. Read input from STDIN. Print output to STDOUT
n_eng = int(input())
eng_roll = set(map(int, input().split()))

n_french = int(input())
french_roll = set(map(int, input().split()))

print(len(eng_roll.union(french_roll)))










