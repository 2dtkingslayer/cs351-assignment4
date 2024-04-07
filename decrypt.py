# Course: CS 351-008
# Group 11
# Assignment 4
# Member 1: Truong Dang - tdd4 - 31558941
# Member 2: Arnoldo Rivera - ar72 - 31511245
# Member 3: Nifesimi Akintola - na553 - 31550903
# Member 4: Bruno Quinones - bq3 - 31551111

# For Decoration
def barLine():
    print("-" * 30)

'''
==============================================
printInput(input_string: str)
----------------------------------------------
This function prints the input string (Cipher Text)
==============================================
'''
def printInput(input_string):
    print("Input (Cipher Text): " + input_string)

'''
==============================================
printOutput(output_string: str)
----------------------------------------------
This function prints the output string (Plain Text)
==============================================
'''
def printOutput(output_string):
    print("Output (Plain Text): " + output_string)

'''
==============================================
convertToPlainText(cipher: str, keys: dict) -> str
----------------------------------------------
This function converts the cipher text to plain text 
using the keys computed from frequency analysis
==============================================
'''
def convertToPlainText(cipher: str, keys: dict):
    output_string = ''
    for c in cipher:
        if c.isalpha():
            output_string += keys[c]
        else:
            output_string += c
    return output_string

'''
==============================================
printKeys(combinedCP: dict)
----------------------------------------------
This function prints the current mapping of
the cipher text to plain text characters
and indicates if there are any duplicates.
==============================================
'''
def printKeys(combinedCP: dict):
    tempcombinedCP = combinedCP.copy()
    # Check Duplicates
    value_count = {}
    for value in tempcombinedCP.values():
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1
    duplicates = {value: count for value, count in value_count.items() if count > 1}
    for dup in duplicates.keys():
        for t in tempcombinedCP.keys():
            if tempcombinedCP[t] == dup:
                tempcombinedCP[t] += " DUPLICATE!"
    print("CURRENT KEYS:")
    for cipherTextLetter in tempcombinedCP.keys():
        print(cipherTextLetter + " ---> " + tempcombinedCP[cipherTextLetter])

'''
==============================================
inputManually() -> dict
----------------------------------------------
This function takes in manual input from the user
to replace any character of their choice in the cipher 
text with a new plain text character.
Users are to enter the cipher letter followed by a space
and then the plain letter.
==============================================
'''
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

'''
==============================================
updateKeys(combinedCP: dict, new_pairs: dict) -> dict
----------------------------------------------
This function updates the existing cipher to plain text
mapping with the new pairs provided by the user.
==============================================
'''
def updateKeys(combinedCP: dict, new_pairs: dict):
    tempcombinedCP = combinedCP.copy()
    for cipher_letter in new_pairs.keys():
        tempcombinedCP[cipher_letter] = new_pairs[cipher_letter]
    return tempcombinedCP

'''
==============================================
printFrequency(keys_dict: dict, freq_dict: dict)
----------------------------------------------
This function prints the frequency of each letter
==============================================
'''
def printFrequency(keys_dict: dict, freq_dict: dict):
    print("Cipher Letter\tFrequency\tPlain Letter")
    for key in keys_dict.keys():
        print(f"{key}\t\t{freq_dict[key]}\t\t{keys_dict[key]}")
    barLine()

# Initiaizing Frequency Table used for Frequency Analysis
frequency = {
    "A": 8.2,  "B": 1.5, "C": 2.8, "D": 4.3, "E": 12.7,  "F": 2.2, "G": 2.0, "H": 6.1, 
    "I": 7.0, "J": 0.2, "K": 0.8, "L": 4.0, "M": 2.4, "N": 6.7, "O": 7.5, "P": 1.9,
    "Q": 0.1, "R": 6.0, "S": 6.3, "T": 9.1, "U": 2.8, "V": 0.98, "W": 2.4, "X": 0.15, "Y": 1.97, "Z": 0.07
}

# List of characters sorted low to high by frequency
frequency = sorted(frequency, key=lambda x: frequency[x]) 

'''
Initializing punctuation. Assuming that cipher text
will contain only letters of the english alphabet, 
spaces, and punctuations like !()-[]{};:'",<>.\/?@#$%^&*_~
'''
punc = '''!()-[]{};:'",<>.\/?@#$%^&*_~'''

# Input (Cipher Text)
cipher = input("Enter Cipher Text: ")
cipher = cipher.upper() # Make sure all letters are uppercase
barLine()

'''
Computing the frequency of each character 
in the cipher text,for use in mapping stage 
of the frequency analysis
'''
cipherTextFreq = {}
for char in cipher:
    if char in punc or char == ' ' or not char.isalpha():
        continue
    if char in cipherTextFreq:
        cipherTextFreq[char] += 1
    else:
        cipherTextFreq[char] = 1

# Sort Frequency (high to low)
cipherTextFreqSort = sorted(cipherTextFreq, key=lambda x: cipherTextFreq[x], reverse=True)

'''
Mapping cipher characters to plain text characters.
By matching high frequency cipher text characters to
known high frequency characters in the english language
'''
combinedCtoP = {}
for cipherTextLetter in cipherTextFreqSort:
    combinedCtoP[cipherTextLetter] = frequency.pop()
printFrequency(combinedCtoP, cipherTextFreq)

output_string = convertToPlainText(cipher, combinedCtoP)

printKeys(combinedCtoP)
printInput(cipher)
printOutput(output_string)

'''
Asking user if they would like to manually replace 
some characters in the cipher text with a new plain text
character to update the computed mapping.
'''
ans = input("Would you like to manually replace some characters? (Y/N): ").upper()
while ans not in ['Y', 'N']:
    ans = input("Enter a valid option (Y/N) or (E) to exit: ").upper()
    if ans in ['E', 'e']:
        exit(0)
if ans == 'N': # No Editing
    exit(0)

while ans in ['Y', 'y']:
    barLine()
    print("Type cipher and plain letter respectively separated by a space. Type 'DONE' to complete.")
    new_pairs = inputManually()
    combinedCtoP = updateKeys(combinedCtoP, new_pairs)
    printKeys(combinedCtoP)
    print("CT: " + cipher)
    output_string = convertToPlainText(cipher, combinedCtoP)
    print("PT: " + output_string)
    ans = input("Would you like to manually replace some characters? (Y/N): ").upper()
    while ans not in ['Y', 'N']:
        ans = input("Enter a valid option (Y/N): ").upper()

barLine()
print("Final Result of Plain Text: " + output_string)
