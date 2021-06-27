'''Write a Python program for all the cases which can check a string contains only a certain set of characters
(in this case a-z, A-Z and 0-9).'''
import re

def is_allowed_specific_character(s):
    characterRe = re.compile(r'[^a-zA-Z0-9.]')
    s = characterRe.search(s)
    return not bool(s)

print(is_allowed_specific_character("Puneetpsk1609")) 
print(is_allowed_specific_character("85686@psk123_"))


print()
#Write a Python program that matches a word containing 'ab'.

def text_match(t):
        p = '\w*ab.\w*'
        if re.search(p,  t):
                return "Match Found!  Hurray!!"
        else:
                return("Oops!! Match not found")

print(text_match("Puneet Python Lover"))
print(text_match("abbbaaababababbbbaaa"))

print()
#Write a Python program to check for a number at the end of a word/sentence.

def end_num(s):
    text = re.compile(r".*[0-9]$")
    if text.match(s):
        return True
    else:
        return False

print(end_num('ab34de'))
print(end_num('abc123'))
print(end_num('abc'))
print(end_num('12345abcde'))



print()
#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given s

results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 9, 11, and 222 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))


print()
#Write a Python program to match a string that contains only uppercase letters

def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return ('Match Found! Hurray!')
        else:
                return('Oops! Match not found!!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))
