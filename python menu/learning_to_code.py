# variables and memory allocation (in python)
# when creating a variable python with automatically allocate it in memory but the way it does this
# will vary depending on the type of variable you have. 
# For normal variables such as integers, floating point numbers, strings(at least for python) and so on, python will allocate the 
# variable as the value. see the following example. 

# create integer a
a = 1
# create integer b to be equal to a
b = a
# add 1 to b
b += 1
print(f"a={a}, b={b}")

# how ever for more complicated variables like lists and generally any data structure python will not allocate memory in the same way
# instead python allocates the list in what is called the heap, and the variable is given the location of the memory in the heap
# to see this see the following example

# create array a
a_array = [1,2,3]
# create array b to be equal to b
b_array = a_array
# add 1 to entry in the array index by 1 (the second entry)
b_array[1] += 1
print(f"a_array = {a_array}, b_array = {b_array}")

# Notice that at the end both array a and b are the same even though we only modified array b. This is became at the b = a step
# we didn't copy the array into b but we copied the location of the array. so both a and b are variables that store the location
# of the same array. these types of variables are called points as the point to the data and are not the actual data.
# memory allocation is different in all programming languages but generally follows these ideas.

print([[] for i in range(10)])


my_dick = {"one":1, 1:2 }

print(my_dick[1])

arr = [1, 2, 3, 4, 5]

for i in arr:
    i += 1

print(arr)


