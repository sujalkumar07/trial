# check if a string is a palindrome 

def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False 
print(is_palindrome("madam"))  #output: true 