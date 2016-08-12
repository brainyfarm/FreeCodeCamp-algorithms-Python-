"""
Repeat a given string (first argument) num times (second argument). 
Return an empty string if num is not a positive number.
"""
def repeat_string(string, num):
    result = ""
    if(num < 0):
        return ""
    else:
       while(num >= 1):
           result += string
           num -= 1
    return result 
print repeat_string("abc", 4)