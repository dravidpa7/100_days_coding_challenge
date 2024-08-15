def repeat_characters(string):
    result = ""
    # Loop through the string, with index starting from 1
    for index, char in enumerate(string, start=1):
        # Repeat the character index times
        result += char * index
    return result

# Example usage
input_string = input("Enter a string: ")
output_string = repeat_characters(input_string)
print("Output:", output_string)
