"""
Return true if the given string is a palindrome. Otherwise, return false.

A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.

You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) 
and turn everything lower case in order to check for palindromes.
"""
# Import regular expression
import re

def palindrome(string):
    
    # Clean string of non-alphabets and non-numeric characters
    # Convert all to lowercase
    regex = re.compile('[\W_]', re.IGNORECASE)
    cleaned_string = re.sub(regex, "", string).lower()
    
    # Clever reversing with the striding
    reversed_string = cleaned_string[::-1]
    
    # Compare reversed string to cleaned one
    return cleaned_string == reversed_string

print palindrome("Race-_=+cAr")