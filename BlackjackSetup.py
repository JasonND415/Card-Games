import Cards
from Cards import Cards,Stack,randomize,randint

def start():
    List=["2","3","4","5","6","7","8","9","10","Jack","King","Queen","Ace"]
    Suit=["Hearts","Clubs","Diamonds","Spades"]
    deck=Stack()
    for i in range (8):
        for symbol in List:
            for suit in Suit:
                if symbol=="Queen":
                    value=10
                elif symbol=="Jack":
                    value=10
                elif symbol =="King":
                    value=10
                elif symbol == "Ace":
                    value=11
                else:
                    value=int(symbol)
                temp=Cards(symbol,suit,value)
                deck.push(temp)    
    temp2=Cards("Shuffle","Cut",10000) 
    deck.push(temp2)    
    return deck

def options(one,two,sum):
    if (sum==21):
        print("You got blackjack")
        return 1
    elif ((one.symbol=="Ace" and (two.value==8 or two.value==9)) or two.symbol=="Ace" and (one.value==8 or one.value==9) ):
        print("Choose an option")
        print("Press d to double down")
        print ("Press h to hit")
        print ("Press st to stand")
        return 4
    elif one.symbol==two.symbol and (sum==9 or sum==10 or sum==11):
        print("Choose an option")
        print("Press sp to split")
        print("Press d to double down")
        print ("Press h to hit")
        print ("Press st to stand")
        return 2;
    elif one.symbol==two.symbol:
        if (one.symbol!="Ace"):    
            print("Choose an option")
            print("Press sp to split")
            print ("Press h to hit")
            print ("Press st to stand")
        return 3;
    elif sum==9 or sum==10 or sum==11:
        print("Choose an option")
        print("Press d to double down")
        print ("Press h to hit")
        print ("Press st to stand")
        return 4;
    else:
        print("Choose an option")
        print ("Press h to hit")
        print ("Press st to stand")
        return 5;

def check(deck):
    card1=deck.pop()
    card2=deck.pop()
    if (card1.symbol=="Ace"and (card2.value==8 or card2.value ==9)):
        deck.push(card1)
        deck.push(card2)
        return True
    elif (card2.symbol=="Ace"and (card1.value==8 or card1.value ==9)):
        deck.push(card1)
        deck.push(card2)
        return True
    else:
        deck.push(card1)
        deck.push(card2)
        return False

def insurance(ace):
    if ace.symbol=="Ace":
        print("Do you want insurance?")
        return True;
    else:
        return False;

def empty_no_ace(deck,empty2):
    while deck.isEmpty()==False:
        empty2.push(deck.pop())
    return empty2

def empty(deck,empty2):
    while deck.isEmpty()==False:
        r=deck.pop()
        if r.value !=1:
            empty2.push(r)
        else:
            r.value=11
            empty2.push(r)
    return empty2

def shuffle(deck,disposal):
    while True:
        if deck.peek().value==10000:
            deck=empty(disposal,deck)
            deck=randomize(deck)
        if deck.peek().value!=10000:
            break
    return deck

class money:
    def __init__(self,cash):
        self.cash=cash
        self.wager=float(0)
        self.insurance=float(0)
        self.wager2=float(0)
    def set_wager(self,r):
        self.wager=float(r)
    def lose(self):
        self.cash-=self.wager
        self.wager=float(0)
    def win(self):
        self.cash+=self.wager
        self.wager=float(0)
    def blackjack(self):
        self.cash+=(self.wager*1.5)
        self.wager=float(0)
    def see_cash(self):
        return self.cash
    def push(self):
        self.wager=float(0)
    def double_down(self):
        self.wager*=2
    def double_downsplit(self):
        self.wager2*=2
    def insurance_bet(self):
        self.insurance=self.wager/2
    def insurance_win(self):
        self.cash+=(2*self.insurance)
        self.insurance=float(0)
    def insurance_loss(self):
        self.cash-=self.insurance
        self.insurance=float(0)
    def split(self):
        self.wager2=self.wager
    def split_lose(self):
        self.cash-=self.wager2
        self.wager2=float(0)
    def split_win(self):
        self.cash+=self.wager2
        self.wager2=float(0)
    def split_push(self):
        self.wager2=float(0)

class colors:
    RED= "\033[31m"
    BLACK= "\033[30m"
    END="\033[0m"

class Spinner:
    def __init__(self):
        self.money=0
        self.List=[10,100,500,500,1000,1000, 1000,1000, 5000, 5000,5000,5000, 5000,10000,10000,50000,1000000]
    def choose(self):
        s=randint(0,len(self.List)-1)
        return self.List[s]

    