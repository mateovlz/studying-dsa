


test_1 = "Welcome"
    #   w e l c o m e
    #   0 1 2 3 4 5 6 

"""
    String Slicing
    Remember that slicing an array or string in 
    python [start_index, end_index, step]
"""

print(test_1[0:3]) # Wel

print(test_1[2:4]) # lc

print(test_1[::2]) # w l o e its stepping 2 steps

print(test_1[::-1]) # iterate backwards 

""" 
    If the value is alphanumeric
"""
print(test_1[0].isalnum())

""" 
    If the value is alphabethic
"""
print(test_1[0].isalpha())

""" 
    Concatenation of String base of a iteration
"""
print("_wi_".join(['asd','asd']))
print("abcd".join("   "))
print(" ".join("abcd"))

"""
    Getting ASCII Code from concatenation ORD
"""

print([ord(char) for char in test_1])