
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

group_A_size , group_B_size = map(int, input().split())
group_A = defaultdict(list)

for i in range (group_A_size):
    #inputs = input()
    #print(inputs)
    group_A[input()].append(i+1)
    #print(group_A)

for i in range (group_B_size):
    inputs = input()
    if inputs in group_A:
        print(' '.join(map(str,group_A[inputs])))
    else:
        print(-1)

