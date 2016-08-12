"""
null in js, None in python
false is False

Remove all falsy values from an array.
Falsy values in JavaScript are false, null, 0, "", undefined, and NaN

I had to modify a lot of stuff from this very challenge due to some differences
in JS and Python
"""
def bouncer(the_list):
    # List comprehension rocks!
    return [element for element in the_list if element is not False and element is not "" and element is not None and element is not 0]
print bouncer([7, "ate", "", False, None, 9, 0])