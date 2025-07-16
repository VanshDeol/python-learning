from collections import Counter

n = int(input())
count = Counter()

for i in range (n):
    words = input()
    count[words] += 1


'''    
unique_count = 0
for v in count:
    unique_count += 1
print(unique_count)

for i in count.values():
    print(i, end = ' ')
'''
#----OR----

print(len(count))
print(*count.values())
