'''
@author: Jason Dao
'''
import random
from random import randint
import requests
from bs4 import BeautifulSoup as bs
from util.Stack import *
class Cards:                                                     #card has symbol, suit, and value compared to others
    def __init__(self,symbol,suit,value,name,url):
        self.symbol=symbol
        self.suit=suit
        self.value=value
        self.name=name
        self.url=url

def start():                                       #assign values to card and put in stack
    r=requests.get("https://en.wikipedia.org/wiki/Standard_52-card_deck")
    soup=bs(r.text,"lxml")
    startpoint=soup.find("body")
    startpoint=startpoint.center.table.tbody.tr     #get image
    startpoint=startpoint.find_next_sibling()
    real=startpoint.td
    List=["Ace","2","3","4","5","6","7","8","9","10","Jack","King","Queen"]
    Suit=["Clubs","Diamonds","Hearts","Spades"]
    deck=Stack()
    for suit in Suit:
        for symbol in List:
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
            tempname=symbol+" of "+ suit
            real=real.a.img
            pic="https:"
            pic=pic+real.attrs["src"]                      #assign url for image of card to scrape later
            temp=Cards(symbol,suit,value,tempname,pic)
            deck.push(temp)
            real=real.parent.parent.find_next_sibling()
        startpoint=startpoint.find_next_sibling()
        real=startpoint
    return deck
    
def randomize(r):                             #randomize stack items
    temp2=[]
    while r.isEmpty()==False:                 #put into second stack
        temp2.append(r.pop())
    while len(temp2) !=0:                     #random number and item number in stack is put into original
        l=randint(0,len(temp2)-1)
        r.push(temp2[l])
        temp2.remove(temp2[l])
    return r

def empty(stack1,stack2):                      #emty stack1 into stack2
    while(stack1.size()!=0):
        stack2.push(stack1.pop())
    return stack2






