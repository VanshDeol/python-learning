from collections import deque

n = int(input())

for _ in range(n):
    block_size = int(input())
    blocks = deque(list(map(int,input().split())))
    top = float('inf')
    while blocks:    #-----OR---use for _ in range(len(blocks)):
                     #Always use while blocks: when modifying the container you're iterating over.
        if blocks[0] >= blocks[-1] and blocks[0] <= top:
            top = blocks.popleft()
        elif blocks [-1] >= blocks[0] and blocks[-1] <= top:
            top = blocks.pop()
        else:
            print("No")
            break
    if not blocks:
        print("Yes")
  
