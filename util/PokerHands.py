def royalflush(list,list2):
    i=straightflush(list,list2)
    if i==True and list[0]==14 and list[1]==13:           #if satsifies straightflush and first two cards are Ace and king, it is royalflush
        return True
    else:
        return False

def straightflush(list,list2):
    j=straight(list)  
    i=flush(list2)
    if j==True and i==True:         #if satsifies both straight and flush,is straightflush
        return True
    else:
        return False

def four(list):            
    for i in list:              #prints how many occurrences of each item in list
        if list.count(i)>=4:    #if at least four, four of a kind
            return True
    return False

def fullhouse(list):
    count=0
    c=0
    both=True
    for i in list:              
        if c!=0 and i==list[c-1]: #takes into account duplicates
            c+=1
            continue
        if list.count(i)==2:    #if at least two count,record it happened once
            count+=1
        if list.count(i)==3:    #if at least three count,record it happened once
            both=False
        if count==1 and both==False:            #if both scenarios occur,there is a fullhouse
            return True
        c+=1
    return False

def flush(list):                     #input:list of suits
    temp=list[0]                     #if other cards are like first suit,return True, else return False
    for i in list:
        if temp != i:
            return False
    return True

def straight(list):         #return sorted list of values
    if list[0]==14 and list[1]== 5 and list[2]==4 and list[3]==3 and list[4]==2:      #ace low 
        return True
    temp=list[0]            #if values subtract by 1 each time, it is a straight
    for i in list:
        if temp !=i:
            return False
        temp-=1
    return True

def three(list):      
    for i in list:              #prints how many occurrences of each item in list
        if list.count(i)>=3:    #if at least three three of a kind
            return True
    return False

def twopair(list):
    count=0
    c=0
    for i in list:              
        if c!=0 and i==list[c-1]: #takes into account duplicates
            c+=1
            continue
        if list.count(i)>=2:    #if at least two count
            count+=1
        if count==2:            #if it occurs twice,there is a two pair
            return True
        c+=1
    return False

def pair(list):
    for i in list:              #prints how many occurrences of each item in list
        if list.count(i)>=2:    #if at least two there is a pair
            return True
    return False

def highcard(list):
    return list[0]                 #return greatest card

def findout(list,listsuit):
    all=[]                                        #get true or false of each possible hand
    all.append(royalflush(list,listsuit))
    all.append(straightflush(list,listsuit))
    all.append(four(list))
    all.append(fullhouse(list))
    all.append(flush(listsuit))
    all.append(straight(list))
    all.append(three(list))
    all.append(twopair(list))
    all.append(pair(list))
    for number,result in enumerate(all):
        if result==True:                           #return first instance of True, highest possible hand
            return number
    return 9


