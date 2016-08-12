"""
Reverse the provided string.
Your result must be a string.
"""
def reverse_string(string):
    # Turn the string into a list
    string_list = list(string)
    # Reverse the list
    string_list.reverse()
    # Convert list to string and return
    return "".join(string_list)
    
print reverse_string("hello")
    