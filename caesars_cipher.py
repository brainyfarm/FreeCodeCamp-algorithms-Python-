# -*- coding: utf-8 -*-
"""
One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher. 
In a shift cipher the meanings of the letters are shifted by some set amount.

A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places. 
Thus 'A' ↔ 'N', 'B' ↔ 'O' and so on.

Write a function which takes a ROT13 encoded string as input and returns a decoded string.

All letters will be uppercase. Do not transform any non-alphabetic character
(i.e. spaces, punctuation), but do pass them on.
"""
def rot13(encoded_string):
    
    string_list = list(encoded_string)
    string_code = map(ord, string_list)
    
    string_translate = [unichr(element) if element < 65 or element > 90 else unichr(element + 13) if element <=77 else unichr(element - 13)  for element in string_code ]
    return "".join(string_translate)
    
print rot13("SERR PBQR PNZC!");
# "FREE CODE CAMP!" :)