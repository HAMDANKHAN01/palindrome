
import sys

# Check if text was passed as a command-line argument
if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    # Fallback for manual local testing
    text = input("Enter a text: ")

# Check palindrome
text = text.lower().replace(" ", "")

if text == text[::-1]:
    print("The text is a palindrome")
else:
    print("The text is not a palindrome")
