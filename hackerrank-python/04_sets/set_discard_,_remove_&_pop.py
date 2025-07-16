n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

for i in range(n_commands):
    e_command = list(input().split())
    command = e_command[0]

    if command == 'pop':
        s.pop()
    elif command == 'remove':
        arg = int(e_command[1])
        s.remove(arg)
    elif command == 'discard':
        arg = int(e_command[1])
        s.discard(arg)
         
print(sum(s))

