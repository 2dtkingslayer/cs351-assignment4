# Course: CS 351-008
# Group 11
# Assignment 4
# Member 1: Truong Dang - tdd4 - 31558941
# Member 2: Arnoldo Rivera - UCID - NJIT ID
# Member 3: Nifesimi Akintola - UCID - NJIT ID
# Member 4: Bruno Quinones - bq3 - 31551111

# For Decoration
def barLine():
    print("-" * 30)

# Print Output String (Plain Text)
def printOutput(output_string):
    print("Output (Plain Text): " + output_string)
    barLine()

# Convert CT to PT using keys
def convertToPlainText(cipher: str, keys: dict):
    output_string = ''
    for c in cipher:
        if c.isalpha():
            output_string += keys[c]
        else:
            output_string += c
    return output_string

# Print keys
def printKeys(keys: dict):
    print("CURRENT KEYS:")
    for cipher_letter in keys.keys():
        print(cipher_letter + " ---> " + keys[cipher_letter])
def printTempKeys(keys: dict):
    print("TEMPORARY KEYS:")
    for cipher_letter in keys.keys():
        print(cipher_letter + " ---> " + keys[cipher_letter])

# Get manual input from user and save to new dictionary
def inputManually() -> dict:
    new_pairs = {}
    pair = input("Enter Cipher Letter and Plain Letter: ").upper()
    while pair != "DONE":
        if len(pair) == 3 and pair[1] == ' ' and pair[0].isalpha() and pair[2].isalpha:
            new_pairs[pair[0]] = pair[2]
        else:
            print("Correct format: \"<letter><space><letter>\". Type again.")
        pair = input("Enter Cipher Letter and Plain Letter: ").upper()
    return new_pairs

# Merge new keys with current keys
def updateKeys(keys: dict, new_pairs: dict):
    temp_keys = keys.copy()
    for cipher_letter in new_pairs.keys():
        temp_keys[cipher_letter] = new_pairs[cipher_letter]
    # Check Duplicates
    if len(set(temp_keys.values())) != len(temp_keys):
        printTempKeys(temp_keys)
        print("There is duplicate in either cipher keys or plain keys. This is invalid! Old key is kept.")
        printKeys(keys)
        return keys
    else:
        return temp_keys

# Initiaizing Frequency Table
frequency = {
    "A": 8.2,  "B": 1.5, "C": 2.8, "D": 4.3, "E": 12.7,  "F": 2.2, "G": 2.0, "H": 6.1, 
    "I": 7.0, "J": 0.2, "K": 0.8, "L": 4.0, "M": 2.4, "N": 6.7, "O": 7.5, "P": 1.9,
    "Q": 0.1, "R": 6.0, "S": 6.3, "T": 9.1, "U": 2.8, "V": 0.98, "W": 2.4, "X": 0.15, "Y": 1.97, "Z": 0.07
}
frequency = sorted(frequency, key=lambda x: frequency[x]) # Sort (low to high)

# Initializing Punctuation
punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''

# Input (Cipher Text)
cipher = input("Enter Cipher Text: ")
cipher = cipher.upper() # Make sure all letters are uppercase
barLine()

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
printKeys(keys)

# Output (Plain Text)
output_string = convertToPlainText(cipher, keys)
printOutput(output_string)

# Manual Replacement
ans = input("Would you like to manually replace some characters? (Y/N): ").upper()
while ans not in ['Y', 'N']:
    ans = input("Enter a valid option (Y/N) or (E) to exit: ").upper()
    if ans in ['E', 'N']:
        exit(0)
if ans == 'N': # No Editing
    exit(0)

while ans in ['Y','y']: # Manually Editing
    print("Type cipher and plain letter respectively separated by a space. Type 'DONE' to complete.")
    new_pairs = inputManually()
    keys = updateKeys(keys, new_pairs)

    output_string = convertToPlainText(cipher, keys)
    printOutput(output_string)

    ans = input("Would you like to manually replace some characters? (Y/N): ")