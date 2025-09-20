import random



array = []




for x in range(1_000_000): 
    minimum = 100 # set minimum
    for i in range(3): # 3 rolls
        dice = random.randint(1, 100) # 100 side dice
        if dice < minimum: # set min
            minimum = dice
    
    array.append(minimum)        
            
    
# Calculate average
average_roll = sum(array) / len(array)


print ("average roll = ", average_roll)





