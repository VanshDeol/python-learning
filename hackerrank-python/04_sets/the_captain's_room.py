
n = int(input())

room_list= list(map(int,input().split()))

uniqueroom_list = set(room_list)

cr = ((n*sum(uniqueroom_list) - sum(room_list))//(n-1))

print(cr)

