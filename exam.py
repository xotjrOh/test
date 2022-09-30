def recursion(s, l, r):
    global cnt

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        cnt+=1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    global cnt

    cnt = 1
    return recursion(s, 0, len(s)-1)
for _ in " "*int(input()):
    print(isPalindrome(input()),cnt)