def isPalindrome(s):
    return str(s) == str(s)[::-1] 
#reversing the string given

s = input("Enter a value : ")

if isPalindrome(s):
    print("Yes")
else:
    print("No")

