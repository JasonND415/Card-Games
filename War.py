'''
@author: Jason Dao
'''
from util.Cards import *
Start=Stack()
Start=start()
Start=randomize(Start)
Person1=Stack()
Dispose1=Stack()
Person2=Stack()
Dispose2=Stack()
r=int(Start.size()/2)
print("This starts the game of war")
for i in range (r):
    Person1.push(Start.pop())
Person2=Start
c=0
sure=False
while (Person1.size()!=0 or Dispose1.size()!=0) and (Person2.size()!=0 or Dispose2.size()!=0):
    comcard=Person2.pop()
    print("The computer's card is the",comcard.symbol, "of", comcard.suit)
    personcard=Person1.pop()
    print("Your card is the",personcard.symbol, "of", personcard.suit)
    if comcard.value>personcard.value:
        print("You lose this round")
        Dispose2.push(comcard)
        Dispose2.push(personcard)
    elif comcard.value<personcard.value:
        print ("You win this round")
        Dispose1.push(comcard)
        Dispose1.push(personcard)
    else:
        print ("War!!!!")
        warstack1=Stack()
        warstack2=Stack()
        c=0
        while True:
            if Person1.size()+Dispose1.size()<3 and Person2.size()+Dispose2.size()<3:
                print ("HOLY MOLY,this war ends in a tie")
                sure=True
                break
            if Person1.size()+Dispose1.size()<3:
                sure=True
                print("You lose the game. You ran out of cards.")
                break
            if Person2.size()+Dispose2.size()<3:
                sure=True
                print("You win the game !!!! Your opponent ran out of cards.")
                break
            if (Person1.size()==0):
                Person1=randomize(Dispose1)
                Dispose1=Stack()
            if (Person2.size()==0):
                Person2=randomize(Dispose2)
                Dispose2=Stack()
            if (c != 3):
                warstack1.push(Person1.pop())
                warstack2.push(Person2.pop())
                c+=1
            else:
                warcomcard=Person2.pop()
                print("The computer's card is the",warcomcard.symbol, "of", warcomcard.suit)
                warpersoncard=Person1.pop()
                print("Your card is the",warpersoncard.symbol, "of", warpersoncard.suit)
                if warpersoncard.value==warcomcard.value:
                    c=0
                    print("The war continues!!!")
                elif warpersoncard.value>warcomcard.value:
                    print("You win the war")
                    while warstack1.size()!=0:
                        j=warstack1.pop()
                        print("You saved the",j.symbol, "of", j.suit)
                        Dispose1.push(j) 
                    while warstack2.size()!=0:
                        j=warstack2.pop()
                        print("You stole the",j.symbol, "of", j.suit)
                        Dispose1.push(j) 
                    break
                else:
                    print("You lost the war")
                    while warstack2.size()!=0:
                        j=warstack2.pop()
                        print("You couldn't take the",j.symbol, "of", j.suit)
                        Dispose2.push(j) 
                    while warstack1.size()!=0:
                        j=warstack1.pop()
                        print("You lost the",j.symbol, "of", j.suit)
                        Dispose2.push(j)
                    break
    if sure==True:
        break
    if (Person1.size()==0):
        Person1=randomize(Dispose1)
        Dispose1=Stack()
    if (Person2.size()==0):
        Person2=randomize(Dispose2)
        Dispose2=Stack()
    print()
    input()
if sure==False:
    if Person1.size()+Dispose1.size()==0:
        print("You lose the game")
    else:
        print("You win the game!!!!!")
print("Press enter to quit")
j=input()

        





    