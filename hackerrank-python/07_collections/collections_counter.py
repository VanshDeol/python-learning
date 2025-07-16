from collections import Counter


number_of_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
number_of_customers = int(input())
size_counts = Counter(shoe_sizes) 
earning = 0

for _ in range(number_of_customers):
    
    size , price = map(int, input().split())
    
    if size_counts[size] > 0:
        #size_counts.subtract([size])
        # -----OR------
        size_counts[size] -= 1
        earning += price
print(earning)
    
    

