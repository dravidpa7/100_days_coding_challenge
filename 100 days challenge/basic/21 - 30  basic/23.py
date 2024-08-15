# Smallest of Two Numbers

s=int(input("Enter 1st no "))
e=int(input("Enter 2nd no "))

if s>=e:
    print(f"{e} is the smallest")
elif s <= e :
    print(f"{s} is the smallest")
else :
    print(f"Both are equal")