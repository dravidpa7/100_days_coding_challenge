# Atleast One Number 100

def has_at_least_one_hundred(numbers):
    for number in numbers:
        if number == 100:
            return True
    return False

numbers_list = [45, 78, 99, 92]
result = has_at_least_one_hundred(numbers_list)
print(result)  # Output: False
