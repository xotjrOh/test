import bisect
input()
a1=input().split()
a1.sort()

m=int(input())
a2=input().split()
for k in a2:
    print(1 if bisect.bisect_right(a1,k)-bisect.bisect_left(a1,k) else 0 , end=" ")