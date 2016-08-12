"""
Return the remaining elements of an array after chopping off n elements from the head.
The head means the beginning of the array, or the zeroth index.
"""
def slasher(the_list, n):
    if(n >= len(the_list)):
        return []
    while(n > 0):
        the_list.remove(the_list[0])
        n -= 1
    return the_list
    
print slasher(["burgers", "fries", "shake"], 1)