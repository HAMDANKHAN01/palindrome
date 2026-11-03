text = input("Enter a text: ")

rev = text[::-1]

if text == rev:
    print("Palindrome")
else:
    print("Not a palindrome")