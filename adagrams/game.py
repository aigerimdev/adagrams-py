from random import randint
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}
def draw_letters():
    letter_list = []#where i am gonnna store letters
    # put letetrs from LETTER_POOL to letter_list
    for letter, count in LETTER_POOL.items():
        letter_list.extend([letter] * count)
    drawn_letters = []  # Store the selected 10 letters
    letter_counts = {}  # Track how many times each letter is drawn

    while len(drawn_letters) < 10:  # Repeat until we get 10 letters
        index = randint(0, len(letter_list) - 1)  # Get a random index
        letter = letter_list[index]  # Get the letter at that index
        
        # Count how many times this letter has been drawn
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

        # Ensure we don't exceed the allowed count of any letter
        if letter_counts[letter] <= LETTER_POOL[letter]:
            drawn_letters.append(letter)  # Add the letter to drawn letters

    return drawn_letters  # Return the selected 10 letters

def uses_available_letters(word, letter_bank):
    letter_counts = {}  # Dictionary to track available letter counts

    # Populate letter_counts with frequencies from letter_bank
    for letter in letter_bank:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # Check if the word can be formed
    for letter in word.upper():  # Convert word to uppercase for case insensitivity
        if letter not in letter_counts or letter_counts[letter] == 0:
            return False  # Letter is missing or used up
        letter_counts[letter] -= 1  # Use up one occurrence of the letter

    return True  # Word is valid

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass