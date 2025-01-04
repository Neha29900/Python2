def isPalinndrome(s):
    n = input("s")
    return s == s[::-1]

s = 121
ans = isPalinndrome(s)

if ans:
    print("Yes")
else:
    print("NO")