def check_multiple(num, multiple_of):
    # Check if num is a multiple of multiple_of
    if num % multiple_of == 0:
        # Determine if the multiple is positive or negative
        if num > 0 and multiple_of > 0:
            result = "Positive"
        elif num < 0 and multiple_of < 0:
            result = "Positive"
        else:
            result = "Negative"
    else:
        result = "Not a multiple"
    
    return result

# Example usage
num = int(input("Enter the number: "))
multiple_of = int(input("Enter the multiple to check: "))

result = check_multiple(num, multiple_of)
print(f"{num} is a {result} multiple of {multiple_of}")
