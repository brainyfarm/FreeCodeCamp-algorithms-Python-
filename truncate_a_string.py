"""
Truncate a string (first argument) if it is longer than the given maximum string length (second argument). 
Return the truncated string with a ... ending.

Note that inserting the three dots to the end will add to the string length.

However, if the given maximum string length num is less than or equal to 3, 
then the addition of the three dots does not add to the string length in determining the truncated string.
"""
def truncate(string, num):
    if(len(string) <= num):
        return string
    elif(len(string) > num):
        if(num <= 3):
            return string[:num] + '...'
        return string[:num-3] + '...'
print truncate("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket") - 2)