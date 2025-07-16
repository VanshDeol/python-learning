from itertools import combinations_with_replacement

string , size = input().split()
size = int(size)
string = sorted(string)
for c in combinations_with_replacement(string, size):
    print(''.join(c))

