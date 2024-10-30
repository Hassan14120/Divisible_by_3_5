x = int(input("Enter a number : "))
print(f"Numbers from 1 to {x} that are divisible by both 3 and 5 is :")     
for i in range( 1 , x+1 ):
    if i % 3 == 0 and i % 5 == 0: 
        print( i )
    
        
     