"""
Check if a string (first argument, string) ends 
with the given target string (second argument, target).
"""
def confirmEnding(string,target):
    # Some intelligent stuff going on here
    # We fing out what part of string we need to compare with target
    start_reading_from = len(string) - len(target)
    # String slicing and comparing
    return string[start_reading_from:] == target

print confirmEnding("Open sesame", "same")