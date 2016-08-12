"""
Write a function that splits an array (first argument) into 
groups the length of size (second argument) and returns them as a two-dimensional array.
"""
def chunk_list(the_list, size):
    m = size
    index = 0
    big_list = []
    while(size <= len(the_list) +m):
        to_append = the_list[index:size]
        if(len(to_append) > 0):
            big_list.append(to_append)
        size += m
        index += m
    return big_list
print chunk_list([0, 1, 2, 3, 4, 5,6], 2)