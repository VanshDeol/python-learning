from itertools import combinations

string , size = input().split()
size = int(size)
string = sorted(string)
for i in range(1,size+1):
    comb = combinations(string, i)
    for p in comb:
        print(''.join(p))



