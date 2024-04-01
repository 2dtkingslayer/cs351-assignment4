# Course: CS 351-008
# Group 11
# Assignment 4
# Member 1: Truong Dang - tdd4 - 31558941
# Member 2: Arnoldo Rivera - UCID - NJIT ID
# Member 3: Nifesimi Akintola - UCID - NJIT ID
# Member 4: Bruno Quinones - UCID - NJIT ID

def printOutput(str):
    print("Output (Plain Text): " + str + "\n")

# Initiaizing Frequency Table
frequency = {
    "A": 8.2,  "B": 1.5, "C": 2.8, "D": 4.3, 
    "E": 12.7,  "F": 2.2, "G": 2.0, "H": 6.1, 
    "I": 7.0, "J": 0.2, "K": 0.8, "L": 4.0, 
    "M": 2.4, "N": 6.7, "O": 7.5, "P": 1.9,
    "Q": 0.1, "R": 6.0, "S": 6.3, "T": 9.1, 
    "U": 2.8, "V": 0.98, "W": 2.4, "X": 0.15, 
    "Y": 1.97, "Z": 0.07
}
frequency = sorted(frequency, key=lambda x: frequency[x]) # Sort (low to high)

# Initializing Punctuation
punc = '''!()-[]\{\};:'",<>./?@#$%^&*_~'''

# Input (Cipher Text)
cipher = input("Enter Cipher Text: ")
cipher = cipher.upper() # Make sure all letters are uppercase

# Analyze Frequency
letters_freq = {}
for char in cipher:
    if char in punc or char == ' ':
        continue
    if char in letters_freq:
        letters_freq[char] += 1
    else:
        letters_freq[char] = 1
# Sort Frequency (high to low)
letters_freq = sorted(letters_freq, key=lambda x: letters_freq[x], reverse=True)

# Connect Cipher Text's Letters Frequency to Frequency Table
keys = {}
for letter in letters_freq:
    keys[letter] = frequency.pop()

# Output (Plain Text)
output_string = ''
for c in cipher:
    if c.isalpha():
        output_string += keys[c]
    else:
        output_string += c
printOutput(output_string)

# Manual Replacement
ans = input("Would you like to manually replace some characters? (Y/N): ").upper()
while ans not in ['Y', 'N']:
    ans = input("Enter a valid option (Y/N) or (E) to exit: ").upper()
    if ans in ['E', 'e']:
        exit(0)
if ans == 'N': # No Editing
    exit(0)

while ans in ['Y','y']: # Manually Editing
    char = input("What character would you like to replace? ").upper()
    while len(char) != 1 or not char.isalpha():
        char = input("Only 1 character! What character would you like to replace? ").upper()

    rep_char = input("What character would you like to replace it with? ").upper()
    while len(rep_char) != 1 or not rep_char.isalpha():
        rep_char = input("Only 1 character! What character would you like to replace it with? ").upper()

    # Replaces a character with the other one
    output_string = output_string.replace(char, '-^-')
    output_string = output_string.replace(rep_char, char)
    output_string = output_string.replace('-^-', rep_char)

    printOutput(output_string)

    ans = input("Would you like to manually replace some characters? (Y/N): ")