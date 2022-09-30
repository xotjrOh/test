m=int(input())
for _ in " "*int(input()):
    a,b=map(int,input().split())
    m-=a*b
if m :print("No")
else :print("Yes")