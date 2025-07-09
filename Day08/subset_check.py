test_cases = int(input())

while (test_cases >= 1):
    set_a_elements = int(input())
    set_a = set(map(int, input().split()))
    
    set_b_elements = int(input())
    set_b = set(map(int, input().split()))
    
    print(set_a.issubset(set_b))
        
    test_cases -= 1
    
    
