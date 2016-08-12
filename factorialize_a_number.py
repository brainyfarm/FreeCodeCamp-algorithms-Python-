"""
Return the factorial of the provided integer.

If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.

Factorials are often represented with the shorthand notation n!

For example: 5! = 1 * 2 * 3 * 4 * 5 = 120
"""

def factorial(n):
    result = 1
    if(n == 0):
        return 1
    else:
        while(n >= 1):
            result *= n
            n -= 1
        return result
        
print factorial(5)