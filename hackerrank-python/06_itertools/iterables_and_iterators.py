from itertools import combinations

n = int(input())

letters = list(input().split())

k = int(input())

comb  = list(combinations(letters,k))

'''
count = 0
for i in range (len(comb)):
    if 'a' in comb[i]:
        count += 1

----OR----
'''

count = sum(1 for c in comb if 'a' in c)

print(count/len(comb))

