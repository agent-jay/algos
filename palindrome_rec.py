
def palindrome(s):
    print(s)
    if len(s)==0 or len(s)==1:
        return True
    elif s[0]==s[-1]:
        return palindrome(s[1:-1])
    else:
        return False

#print(palindrome("Hello"))
#print(palindrome("rotor"))
#print(palindrome("roter"))
print(palindrome("rostisor"))
