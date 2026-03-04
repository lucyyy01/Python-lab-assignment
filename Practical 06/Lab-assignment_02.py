# Design a function that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program:
# Practice makes perfect
# Then, the output should be: PRACTICE MAKES PERFECT

# Function to convert lines to uppercase
def capitalize_lines():
    line = input("Enter a sentence: ")
    result = line.upper()
    print(result)

# Call the function
capitalize_lines()