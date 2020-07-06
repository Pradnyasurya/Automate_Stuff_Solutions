import random
numberOfStreaks = 0
streak=0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    htlist=[]
    for i in range(100):
        toss = random.choice(['heads','tails'])
        htlist.append(toss)
    

    # Code that checks if there is a streak of 6 heads or tails in a row. 
    for p in range(len(htlist)):       

        if htlist[p] == htlist[p-1]:
                streak+=1
        else:
                streak=0

        if streak==6:
                numberOfStreaks+=1        

        
print('number of streaks :',numberOfStreaks)
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))