# Question - 2.2

# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise


# creating an function to check the charcter is vowel is not
def check_vowel(char):
    if char.lower() in ['i','e','a','u','o']:
        return True
    else:
        return False
    
    
char = input('Enter the only one length character : ')[0]
if check_vowel(char):
    print('vowel')
else: 
    print('consonant')
