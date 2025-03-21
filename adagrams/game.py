from random import randint

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}
# Helper function 
def build_sack_of_letters():
    letters=[]
    for letter, count in LETTER_POOL.items():
        letters.extend([letter] * count)
    
    return letters

def draw_letters():
    sack_of_letters =  build_sack_of_letters()
    drawn_letters = []
    letter_counts = {}
    
    while len(drawn_letters) < 10:
        index = randint(0, len(sack_of_letters) - 1)
        letter = sack_of_letters[index]
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

        # Ensure we don't exceed the allowed count of any letter
        if letter_counts[letter] <= LETTER_POOL[letter]:
            drawn_letters.append(letter)

    return drawn_letters

# Helper function
def build_count_letters(letter_list):
    letter_counter = {}
    for letter in letter_list:
        letter_counter[letter] = letter_counter.get(letter, 0) + 1
    return letter_counter

def uses_available_letters(word, letter_bank):
    letter_counts = build_count_letters(letter_bank)

    for letter in word.upper():
        if letter not in letter_counts or letter_counts[letter] == 0:
            return False
        letter_counts[letter] -= 1
    return True


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
    word = word.upper()

    if word == "":
        return 0
    
    # Calculate the total score by summing the values of each letter in the word
    total_score = 0
    for letter in word:
        total_score += letter_scores.get(letter, 0)
        
    # Add extra points for 7 or more letters
    if len(word) >= 7:
        total_score += 8
        
    return total_score 

def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = ""
    for word in word_list:
        score = score_word(word)

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

    return (winning_word, highest_score)