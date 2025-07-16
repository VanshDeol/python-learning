from collections import deque

n = int(input())
my_deque = deque()
for _ in range(n):
    inputs = input().split()
    op = inputs[0]
    
    if op == 'append':
        my_deque.append(int(inputs[1]))
    elif op == 'appendleft':
        my_deque.appendleft(int(inputs[1]))
    elif op == 'pop':
        my_deque.pop()
    elif op == 'popleft':
        my_deque.popleft()
        
for items in my_deque:
    print(items,end=' ')
