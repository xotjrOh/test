from collections import Counter
import sys
a=[]
for _ in " "*int(input()):
    a+=[int(sys.stdin.readline())]
a=sorted(a)
print(round(sum(a)/len(a)))
print(a[len(a)//2])
b=Counter(a).most_common(2)
if len(b)>1 and b[0][1]==b[1][1]:print(b[1][0])
else : print(b[0][0])
print(a[-1]-a[0])