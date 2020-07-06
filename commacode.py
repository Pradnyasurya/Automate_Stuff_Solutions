def commacode(userlist):

    if len(userlist)==1:
        return userlist[0]

    else:
        try:
            # string=', '.join(userlist)
           string = '{} and {}'.format(', '.join(userlist[:-1]), userlist[-1])
        except TypeError:
            # string=', '.join(str(x) for x in userlist)
            string = '{} and {}'.format(', '.join(str(x) for x in userlist[:-1]), userlist[-1])

        
        # string= str(userlist)
        # print("ok")
        return string



myList=[]
n = int(input("Enter the number of elements to be added:"))
for i in range(0,n):
    item=input("Enter the item: ")

    # ..............LOL....................#

#doomed quest.... item is always going to be string.
# right now, don't know how to know the type of 
# user input


    # if isinstance(item,str):
    #     myList.append(item)
    # elif isinstance(item,int):
    #     myList.append(int(item))
    
#............hahahahaha.................#

    try:
        item3=int(item)
        myList.append(item3)
    except ValueError:
        myList.append(item)

string = commacode(myList)
print(string)
