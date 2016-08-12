"""
You will be provided with an initial array (the first argument), 
followed by one or more arguments. 
Remove all elements from the initial array that are of the same value as these arguments.
"""
def destroyer(*args):
    the_list = args[0]
    to_remove = list(args[1:])
    # Doing some list comprehension 
    return [element for element in the_list if element not in to_remove]
print destroyer(["tree", "hamburger", 53], "tree", 53)