# Pass or Fail

def mark (x):  
    if x >=50:
        return 1 
    else:
        return 0
    
score= 90
result = mark(score)

if result == True :
    print("Pass")
    
else :
    print("Fail")