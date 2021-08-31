def isPalindrome(s):
    return s == s [:: -1]

s = input("Enter The Word")
answer = isPalindrome(s)

if answer:
    print("Yes")
else:
    print("No")
