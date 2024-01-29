# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
#solution
input = input("Input string: ")
y=""
for i in range(len(input)):
    y = y + input [i]*2
    print(y)

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.
#solution
alphabet = "abcdefghijklmnopqrstuvwxyz"
user_range = input("Enter a range of letters (e.g., a-z): ")
def expand_letter_range(letter_range):
    start, end = letter_range.split('-')
    if start.isupper():
        return ''.join(chr(i) for i in range(ord(start), ord(end) + 1)).upper()
    else:
        return ''.join(chr(i) for i in range(ord(start), ord(end) + 1))

result = expand_letter_range(user_range)
print(result)
