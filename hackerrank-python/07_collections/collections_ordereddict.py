
from collections import OrderedDict

n = int(input())

order_dict = OrderedDict()

for i in range(n):
    
    *item_name , item_price = input().split()  #Unpacking all inputs in item__name except last
    item_price = int(item_price)
    item_name = ' '.join(item_name)    # Converting list to string
    order_dict[item_name] = order_dict.get(item_name,0) + item_price 
    
#If item_name already exists in the dict, we add to its current value.
#If it doesnt exist yet, we start from 0.



for key,value in order_dict.items():
    print (f"{key} {value}")

