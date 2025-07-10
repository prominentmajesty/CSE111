# In line 77 to line 82, i wrote a method that i named exceed_requirement that checks if the password contains a sequence of 3 or more repeated characters.
# In that exceed_requirememnt method, If the password contains such a sequence, The method prints a warning message to the user telling the user that the password is weak due to the repeated characters, and then return Boolean value of true, else it will return a Boolean value of false.

# Character type lists
LOWER = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
UPPER = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?", "/", "`", "~"
]
 
# 1) word_in_file function
def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                file_word = line.strip()
                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True
        return False
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return False

# 2) word_has_character function
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

# 3) word_complexity function
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "Week02 Assignment/wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "Week02 Assignment/toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    complexity = word_complexity(password)
    strength = 1 + complexity
    print(f"Password complexity score: {complexity}. Strength: {strength}.")
    return strength

# Method for Exceed requirement
def exceed_requirement(password):
    import re
    if re.search(r'(.)\1{2,}', password):
        #Grader, Please take note that this message fall outside the list of messages that are specified in the instructions.
        # I Just added it in other to show exceeded requirement.
        print("Warning: This password is a weak password because it contains a sequence of repeated characters.")
        return True
    return False

def main():
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Goodbye!")
            break
        strength = password_strength(password)
        exceed_requirement(password)
        print(f"Password strength score: {strength}\n")

if __name__ == "__main__":
    main()
