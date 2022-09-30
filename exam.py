a=[*map(int,input().split())]
k=len(set(a))
if k == 1:print(a[0]*1000+10000)
elif k == 2:print(sorted(a)[1]*100+1000)
else:print(max(a)*100)