l = [1]*10000
for i in range(2,10000):
    if l[i]:
        l[2*i::i]=[0]*len(l[2*i::i])
for _ in range(int(input())):
    n = int(input())
    for i in range(n//2,n):
        if l[i] and l[n-i]:print(n-i,i);break