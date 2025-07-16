from itertools import permutations

string , size = input().split()

size = int(size)
for p in sorted(permutations(string,size)):
    #print(p) ---- print as singular tuple eg ('A', 'C')
    print(''.join(p))   # ---- print as AC
    
#print(*list(permutations(string,size)))

