# Question 7: Count cvc (consonant-vowel-consonant) pairs in a string
# Example: "bat" has 1 cvc pair (b-a-t), "hello" has 1 cvc pair (h-e-l)

string = input("Enter a string: ")  # Get string from user

# Step 1: Define which letters are vowels
vowels = "aeiouAEIOU"

# Step 2: Start counting from 0
count = 0

# Step 3: Check every 3 letters in the string
# We use range(len(string) - 2) because we need 3 letters at a time
for i in range(len(string) - 2):
    # Get 3 consecutive letters
    char1 = string[i]        # First letter
    char2 = string[i + 1]    # Second letter (next one)
    char3 = string[i + 2]    # Third letter (next next one)
    
    # Check if all 3 are actual letters (not space or numbers)
    if char1.isalpha() and char2.isalpha() and char3.isalpha():
        # Check the pattern: consonant-vowel-consonant
        # char1 should NOT be in vowels (so it's consonant)
        # char2 should be in vowels
        # char3 should NOT be in vowels (so it's consonant)
        if char1 not in vowels and char2 in vowels and char3 not in vowels:
            count = count + 1  # Found one! Add 1 to count

print("Number of cvc pairs:", count)

print("\n" + "="*50 + "\n")

# Question 9: Remove more than 2 successive occurrences of same alphabet
# Example: "Indiaaa is theeeee bessssst" → "India is theee besst"

sentence = input("Enter a sentence: ")  # Get sentence from user

# Step 1: Create empty result string
result = ""

# Step 2: Keep track of how many times we see same letter in a row
count = 1

# Step 3: Go through each letter in the sentence
for i in range(len(sentence)):
    # If it's the first letter, just add it to result
    if i == 0:
        result = result + sentence[i]
    else:
        # Check if current letter is same as previous letter
        if sentence[i] == sentence[i-1]:
            count = count + 1  # Same letter! Increase count
            # Only add if we haven't reached 2 yet
            if count <= 2:
                result = result + sentence[i]
            # If count is 3, 4, 5... we don't add (skip it)
        else:
            # Different letter! Reset count to 1
            count = 1
            result = result + sentence[i]  # Add this new letter

print("Result:", result)

print("\n" + "="*50 + "\n")

# Question 10: Find minimum number of rotations to get actual string
# Example: given = "lohel", actual = "hello", answer = 2 rotations

given_string = input("Enter the given string: ")    # Example: "lohel"
actual_string = input("Enter the actual string: ")  # Example: "hello"

# Step 1: Start with -1 (meaning not found)
rotations = -1

# Step 2: Try rotating the string different times
# We try 0 rotations, 1 rotation, 2 rotations... up to length of string
for i in range(len(given_string)):
    # Rotate the string by i positions
    # string[i:] means: take from position i to end
    # string[:i] means: take from start to position i
    # Example: "lohel", when i=2: "hel" + "lo" = "hello"
    rotated = given_string[i:] + given_string[:i]
    
    # Check if this rotated string matches actual string
    if rotated == actual_string:
        rotations = i  # Found it! Save the number
        break  # Stop searching

# Step 3: Print result
if rotations != -1:
    print("Minimum rotations needed:", rotations)
else:
    print("Cannot get actual string from given string")

print("\n" + "="*50 + "\n")

# Question 16: Display frequency of each character in string

string = input("Enter a string: ")

for char in string:
    if char != " ":
        count = 0
        for c in string:
            if c == char:
                count = count + 1
        
        already_printed = False
        for i in range(string.index(char)):
            if string[i] == char:
                already_printed = True
                break
        
        if not already_printed:
            print(char, ":", count)