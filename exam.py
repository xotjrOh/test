h,m=map(int,input().split())
k=int(input())
print((h+(m+k)//60)%24,(m+k)%60)