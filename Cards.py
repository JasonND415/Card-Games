'''
@author: Jason Dao
'''
import random
from random import randint, randrange
class Cards:
    def __init__(self,symbol,suit,value):
        self.symbol=symbol
        self.suit=suit
        self.value=value


class Stack:
    def __init__(self):
        self.items=[]
        self.count=0
    def push(self,l):
        self.items.append(l)
        self.count+=1
    def pop(self):
        self.count-=1
        return self.items.pop()
    def size(self):
        return self.count
    def isEmpty(self):
        if self.count==0:
            return True
        else:
            return False

def start():
    List=["2","3","4","5","6","7","8","9","10","Jack","King","Queen","Ace"]
    Suit=["Hearts","Clubs","Diamonds","Spades"]
    deck=Stack()
    for symbol in List:
        for suit in Suit:
            if symbol=="Queen":
                value=12
            elif symbol=="Jack":
                value=11
            elif symbol =="King":
                value=13
            elif symbol == "Ace":
                value=14
            else:
                value=int(symbol)
            temp=Cards(symbol,suit,value)
            deck.push(temp)
    return deck
    
def randomize(r):
    temp2=[]
    while r.isEmpty()==False:
        temp2.append(r.pop())
    while len(temp2) !=0:
        l=randint(0,len(temp2)-1)
        r.push(temp2[l])
        temp2.remove(temp2[l])
    return r






