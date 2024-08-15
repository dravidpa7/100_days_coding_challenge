row = 5
for i in range (row):
    for j in range (i):
        if j % 2 != 0:
            print("2" ,end=" ")
        else :
            print("1",end=" ")
    print("")