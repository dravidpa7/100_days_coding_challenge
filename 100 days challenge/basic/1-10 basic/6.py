# Sum - Format Print

total_sum = sum(range(1, 10))
print(f"The sum of numbers from 1 to 100 is: {total_sum}")


# ----- without using inbuild sum function ------
total_sum = 0
for number in range(1, 10):
    total_sum += number

print(f"The sum of numbers from 1 to 100 is: {total_sum}")
