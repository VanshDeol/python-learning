

# Complete the solve function below.
def solve(s):
    s = s.split(' ')
    
    cap = [w.capitalize() for w in s]
    
    return ' '.join(cap)  


