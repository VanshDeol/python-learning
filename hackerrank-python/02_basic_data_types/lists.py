if __name__ == '__main__':
    N = int(input())
    ls =[]
    for i in range(N):
        cmds=input().strip().split()
        cmd=cmds[0]
        arg = cmds[1:]
        
        if cmd =="insert":
            ls.insert(int(arg[0]),int(arg[1]))
        
        elif cmd == "print":
            print(ls)
            
        elif cmd == "remove":
            ls.remove(int(arg[0]))
        
        elif cmd == "append":
            ls.append(int(arg[0]))
        
        elif cmd == "sort":
            ls.sort()
            
        elif cmd == "pop":
            ls.pop()
        
        elif cmd == "reverse":
            ls.reverse()            
        

