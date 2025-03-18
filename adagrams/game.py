from random import randint
# Letter frequency in the game
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

# Function to Draw Random Letters
def draw_letters():
    
    letter_list = []  # List to store all available letters
    
# Populate letter_list with available letters (e.g., 'C' appears 2 times → ['C', 'C'])
    for letter, count in LETTER_POOL.items():
        letter_list.extend([letter] * count) # C: 3==>CCC
        
    drawn_letters = []  # Store the selected 10 letters
    letter_counts = {}  # Track how many times each letter is drawn
    
# Keep drawing until we have exactly 10 letters
    while len(drawn_letters) < 10:  # Repeat until we get 10 letters
        index = randint(0, len(letter_list) - 1) # Pick a random index from letter_list
        letter = letter_list[index]  # Get the letter at that index
        
        # Count how many times this letter has been drawn
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

        # Ensure we don't exceed the allowed count of any letter
        if letter_counts[letter] <= LETTER_POOL[letter]:
            drawn_letters.append(letter)  # Add the letter to drawn letters

    return drawn_letters  # Return the selected 10 letters


#  Check if a Word Uses Available Letters
def uses_available_letters(word, letter_bank):
    
    letter_counts = {}  # Store letter counts from letter_bank

    # Count occurrences of each letter in letter_bank
    for letter in letter_bank:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # Check if the word can be formed
    for letter in word.upper():  # Convert word to uppercase for case insensitivity
        if letter not in letter_counts or letter_counts[letter] == 0:
            return False  # Letter is missing or used up
        letter_counts[letter] -= 1  # Reduce available count for that letter
    return True   # All letters were available, so the word is valid


#  Function to Calculate Word Score
def score_word(word):
    letter_scores = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}
    # Convert word to uppercase (case-insensitive)
    word = word.upper()

    # If word is empty, return 0
    if word == "":
        return 0
    
    # Calculate the total score by summing the values of each letter in the word
    total_score = 0
    for letter in word:
        total_score += letter_scores.get(letter, 0) 
        
    # Add extra points for 7 or more letters (only once)
    if len(word) >= 7:
        total_score += 8
        
    return total_score  # Return final score   
        
        
def get_highest_word_score(word_list):
    highest_score = 0  # Stores the highest score found so far
    winning_word = ""  # Stores the best word found so far
    for word in word_list:
        score = score_word(word)  # Calculate the score of the current word

        # If the current word has a higher score, update the highest score and best word
        if score > highest_score:
            highest_score = score
            winning_word = word
        
        # If the current word ties with the highest score, apply tie-breaking rules
        elif score == highest_score:
            # Tie-breaker 1: If one word is exactly 10 letters, it wins
            if len(winning_word) != 10:  # If the current best is NOT 10 letters
                if len(word) == 10:
                    winning_word = word  # Prefer 10-letter word
                
                # Tie-breaker 2: If no 10-letter word, prefer the shorter word
                elif len(word) < len(winning_word):  
                    winning_word = word  # Choose the shortest word

    return (winning_word, highest_score)  # Return the best word and its score as a tuple