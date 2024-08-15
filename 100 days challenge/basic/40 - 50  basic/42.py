no=[23,45,34,57,89,78,55]
sort= sorted(no,key=lambda x:x % 10)
print(sort)




# List of tuples
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# Sort by the second element in each tuple using a lambda function
sorted_pairs = sorted(pairs, key=lambda x: x[0])      # change the arguments to understand the process

print(sorted_pairs)


# sorting function example -1 

words = ['banana', 'apple', 'cherry', 'date']

sorted_by_length = sorted(words, key=len)

print(sorted_by_length)  # Output: ['date', 'apple', 'banana', 'cherry']

#exampe -2
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

sorted_numbers_desc = sorted(numbers, reverse=True)

print(sorted_numbers_desc)  # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]
