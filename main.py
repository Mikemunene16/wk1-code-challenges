# Code challenge 1
def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # If the stack is empty, there's no matching opening bracket
            if not stack:
                return False
            
            # Check if the closing bracket matches the last opening bracket
            last_opening_bracket = stack.pop()
            if (char == ')' and last_opening_bracket != '(') or \
               (char == ']' and last_opening_bracket != '[') or \
               (char == '}' and last_opening_bracket != '{'):
                return False
    
    # After processing the entire expression, the stack should be empty
    return not stack

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


# Code challenge 2

def remove_duplicates(sequence):
    seen = set()  # Create a set to keep track of seen elements
    result = []   # Create an empty list to store unique elements in order
    
    for item in sequence:
        if item not in seen:  # If the item hasn't been seen before
            seen.add(item)    # Add it to the set of seen elements
            result.append(item)  # Add it to the result list
    
    return result

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

# Code challenge 3
import string

def word_frequency(sentence):
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Split the sentence into words and iterate through them
    words = sentence.split()
    for word in words:
        # Remove punctuation and convert to lowercase for case-insensitivity
        cleaned_word = word.strip(string.punctuation).lower()

        # Update the word frequency in the dictionary
        if cleaned_word:
            if cleaned_word in word_freq:
                word_freq[cleaned_word] += 1
            else:
                word_freq[cleaned_word] = 1

    return word_freq

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)





