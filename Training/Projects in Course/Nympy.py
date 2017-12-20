import numpy

Nums = numpy.arange(27)     # Generate a 'multi dimensional' array
print(Nums)                 # Print the array (single dimension)
print(type(Nums),"\n")

Nums.reshape(3,9)           # Change to two dimensional array
print(Nums.reshape(3,9),"\n")

Nums.reshape(3,3,3)         # Change to three dimensional array
print(Nums.reshape(3,3,3),"\n")

NewArray = [[123,234,345,456,567],[],[]]

Nums2 = numpy.asarray(NewArray)
print(Nums2)