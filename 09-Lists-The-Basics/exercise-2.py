# Define a first_and_last function that accepts a list of strings. 
# The function should return a concatenation of the first element and the last element. 
# Assume the list will always have 1 or more elements.
#
# first_and_last(["a", "b", "c"])        => "ac"
# first_and_last(["bob", "tom", "rob"])  => "bobrob"
# first_and_last(["a"])                  => "aa"
def first_and_last(listq):
    return str(listq[0] + listq[-1])
print(first_and_last(["a", "b", "c"]))



# Define a product_of_even_indices function that accepts a list of numbers. 
# The list will always have 6 total elements. 
# The function should return the product (multiplied total) of all numbers at an even index (0, 2, 4).
#
# product_of_even_indices([1, 2, 3, 4, 5, 6])    =>  15
# product_of_even_indices([3, 4, 3, 5, 3, 6])    =>  27
def product_of_even_indices(list):
    return list[0] * list[2] * list[4]
print(product_of_even_indices([1, 2, 3, 4, 5, 6]))


# Define a first_letter_of_last_string function that accepts a list of strings. 
# It should return one character — the first letter of the last string in the list. 
# Assume the list will always have at least one string.
#
# first_letter_of_last_string(["cat", "dog", "zebra"]) => "z"
# first_letter_of_last_string(["nonsense"]) => "n"
def first_letter_of_last_string(list):
    return list[-1][0]