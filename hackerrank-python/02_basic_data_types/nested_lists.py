if __name__ == '__main__':
    n=int(input())
    student=[]
    for _ in range(n):
        name = input()
        score = float(input())
        student.append([name,score])
        
   # student.sort()
    all_scores=[s[1] for s in student]    
    low1=min(all_scores)
    second_lowest = [x for x in all_scores if x > low1]
    low2=min(second_lowest)
    
    rs=[s[0] for s in student if s[1]==low2]
    for i in sorted(rs):
        print(i)
    

