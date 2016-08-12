"""
Return the length of the longest word in the provided sentence.
Your response should be a number.
"""
def longest_word_length(sentence):
    # Length of longest word before looping
    longest_length = 1
    # Split the sentence into a list of words
    word_list = sentence.split(" ")
    
    # Loop through the list of word
    # Check the length of current word and assign it as the longest length
    #   if it is greater than the value of longest_length
    for current_word in word_list:
        if len(current_word) >  longest_length:
            longest_length = len(current_word)
    # Return longest_length value at the end of loop
    return longest_length
print longest_word_length("I am a very great guy and I know it!")