"""
Return an array consisting of the largest number from each provided sub-array. 
For simplicity, the provided array will contain exactly 4 sub-arrays.
"""
def largest_of_four(super_list):
    # This is so easy thanks to list comprehension :)
    return [max(element) for element in super_list]
print largest_of_four([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]])