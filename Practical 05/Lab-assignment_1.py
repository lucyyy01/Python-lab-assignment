# Develop a program that asks the user to enter a series of integers and store them ina Tuple.
# Develop a program that asks the user to enter a series of integers and store them in a Tuple. Perform the following:
# a) Print the total number of items in the Tuple.
# b) Print the last item in the Tuple.
# c) Print the Tuple elements in reverse order.
# d) Print Yes if the Tuple contains an integer 5 and No otherwise.
# e) Remove the first and last items from the Tuple, sort the remaining items, and print the result.

# Input integers from user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(numbers))

# b) Last item
print("Last item in tuple:", numbers[-1])

# c) Tuple in reverse order
print("Tuple in reverse order:", numbers[::-1])

# d) Check if 5 is present
if 5 in numbers:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining items
new_tuple = numbers[1:-1]
sorted_tuple = tuple(sorted(new_tuple))

print("Sorted tuple after removing first and last items:", sorted_tuple)