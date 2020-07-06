import random
htlist=[]
numberOfStreaks=0
streak = 0 
for i in range(100):
        toss = random.choice(['heads','tails'])
        htlist.append(toss)

# for listitems in htlist:
for p in range(len(htlist)):
        

        if htlist[p] == htlist[p-1]:
                streak+=1
        else:
                streak=0

        if streak==6:
                numberOfStreaks+=1
        




        
       
        # temp.append(listitems) 
        # # temp = listitems
        # if temp == ['heads','heads','heads','heads','heads','heads'] or temp == ['tails','tails','tails','tails','tails','tails']:
        #         numberOfStreaks+=1
        #         temp.clear()
        #         continue
        # else:
        #         continue
                 
      

print('number of streaks :',numberOfStreaks)
