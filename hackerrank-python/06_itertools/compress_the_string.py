from itertools import groupby

string = list(input())

for key, group in groupby(string):
    count = len(list(group))
    #print(count)
    print(f"{(count,int(key))}" ,end =' ')
    

