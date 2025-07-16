# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m =map(int,input().split())
c= ".|."
for i in range((n//2)):
    print((c*(2*i+1)).center(m,"-"))

print("WELCOME".center(m,"-"))

for i in range((n//2)):
    print((c*(n-(2*i)-2)).center(m,"-"))

