#------ Square - Format Print  --------
for number in range(1, 10):
    square = number * number
    print(f"The square of {number} is {square}")
    
    
#----- using inbuild function -----

for number in range(1, 10):
    square = pow(number, 2)
    print(f"The square of {number} is {square}")
