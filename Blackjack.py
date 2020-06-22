'''
@ author: Jason Dao
Blackjack Rules: Naturals pay 1.5 to 1, split blackjacks pay 1:1, insurance pays 2:1, no resplitting, can only double down on 9,10,or 11 ONLY, only one card given for each ace split
Info: 8 decks are used with a cut card mixed in
'''
import BlackjackSetup
from util.Cards import *
from BlackjackSetup import start, colors, money, insurance, options, empty, empty_no_ace,shuffle,check, Spinner

sum = 0
splitsum = 0
dealersum = 0
deck = start()
deck=randomize(deck)
luck=Spinner()
print("Your starting amount of money will be chosen randomly. Money ranges from $10 to $1,000,000. Good luck! Press any button to start the spinner and game.")
l=input()
number=luck.choose()
cash = money((float(number)))
disposal = Stack()
person1 = Stack()
sp = Stack()
dealer = Stack()
temp2 = 0
temp3 = 0
temp5=0
checkace=Stack()
checkace2=Stack()
r=False
while True:
    print("================================")
    print("You have", cash.see_cash(), "dollars")
    print("How much in dollars do you want to bet?")
    wagers = input()
    if wagers == str(0) or cash.see_cash() < float(wagers):
        if cash.see_cash() < float(wagers):
            print("You don't have enough")
        break
    else:
        print()
        cash.set_wager(wagers)
        if deck.peek().value==10000:
            deck=shuffle(deck,disposal)
            disposal=Stack()
        dealercard = deck.pop()
        if deck.peek().value==10000:
            deck=shuffle(deck,disposal)
            disposal=Stack()
        dealercard2 = deck.pop()
        print("The dealer's first card is the",
              dealercard.symbol, "of", dealercard.suit)
        dealersum += dealercard.value
        dealer.push(dealercard)
        print("The dealer has", dealersum)
        print()
        if deck.peek().value==10000:
            deck=shuffle(deck,disposal)
            disposal=Stack()
        card1 = deck.pop()
        if deck.peek().value==10000:
            deck=shuffle(deck,disposal)
            disposal=Stack()
        card2 = deck.pop()
        print("Your first card is the", card1.symbol, "of", card1.suit,
              "and your second card is the", card2.symbol, "of", card2.suit)
        sum += card1.value
        sum += card2.value
        person1.push(card1)
        person1.push(card2)
        if insurance(dealercard):
            ins = input()
            if ins.lower() == "yes" or ins.lower() == "y":
                print("You made the insurance bet")
                cash.insurance_bet()
            print()
        temp = options(card1, card2, sum)
        if(temp == 1):
            a=5
        else:
            while True:
                if (sum > 21):
                    checkace = Stack()
                    while(person1.isEmpty() == False):
                        hope = person1.pop()
                        if hope.value == 11:
                            print("Ace is now 1")
                            sum -= 10
                            hope.value = 1
                            person1.push(hope)
                            person1 = empty_no_ace(checkace, person1)
                            checkace = Stack()
                            print()
                            if person1.size() != 2:
                                print("Choose an option")
                                print("Press h to hit")
                                print("Press st to stand")
                            else:
                                print("Choose an option")
                                print("Press sp to split")
                                print("Press h to hit")
                                print("Press st to stand")
                            break
                        else:
                            checkace.push(hope)
                    if(checkace.size() != 0):
                        print("Your sum is", sum)
                        if (splitsum == 0):
                            break
                        else:
                            print("Playing second deck")
                            temp3 = sum
                            sum = splitsum
                            r=check(sp)
                            if sum==21:
                                print('Your second deck has 21')
                            elif sum == 9 or sum == 10 or sum == 11 or r==True:
                                print("Choose an option for second deck")
                                print("Press d to double down")
                                print("Press h to hit")
                                print("Press st to stand")
                            else:
                                print("Choose an option")
                                print("Press h to hit")
                                print("Press st to stand")
                            splitsum = 0
                            disposal = empty(person1, disposal)
                            person1 = sp
                            if sum==21:
                                temp5=1
                                break
                if(sum == 21):
                    print("Your sum is 21")
                    if (splitsum == 0):
                        break
                    else:
                        print("Playing second deck")
                        temp3 = sum
                        sum = splitsum
                        r=check(sp)
                        if sum==21:
                            print('Your second deck has 21')
                        elif sum == 9 or sum == 10 or sum == 11 or r==True:
                            print("Choose an option for second deck")
                            print("Press d to double down")
                            print("Press h to hit")
                            print("Press st to stand")
                        else:
                            print("Choose an option")
                            print("Press h to hit")
                            print("Press st to stand")
                        splitsum = 0
                        disposal = empty(person1, disposal)
                        person1 = sp
                        if sum==21:
                            temp5=1
                            break
                print("Your sum is", sum)
                l = input()
                if (l.lower() == "h" or l.lower()=="hit"):
                    r=False
                    if deck.peek().value==10000:
                        deck=shuffle(deck,disposal)
                        disposal=Stack()
                    tempcard = deck.pop()
                    print("Your card is the", tempcard.symbol, "of", tempcard.suit)
                    sum += tempcard.value
                    person1.push(tempcard)
                    print()
                    if (sum < 21):
                        print("Choose an option")
                        print("Press h to hit")
                        print("Press st to stand")
                elif (l.lower() == "st" or l.lower() == "stand" or l.lower() == "stop" or l.lower() == "stick"):
                    if (splitsum == 0):
                        break
                    else:
                        print("Playing second deck")
                        temp3 = sum
                        sum = splitsum
                        r=check(sp)
                        if sum==21:
                           print('Your second deck has 21')
                        elif sum == 9 or sum == 10 or sum == 11 or r==True:
                            print("Choose an option for second deck")
                            print("Press d to double down")
                            print("Press h to hit")
                            print("Press st to stand")
                        else:
                            print("Choose an option")
                            print("Press h to hit")
                            print("Press st to stand")
                        splitsum = 0
                        disposal = empty(person1, disposal)
                        person1 = sp
                        if sum==21:
                            temp5=1
                            break
                elif((l.lower() == "d"  or l.lower() == "double down" or l.lower()=="double") and (temp==4 or sum==9 or sum==10 or sum==11 or r==True)):
                    temp=0
                    if deck.peek().value==10000:
                        deck=shuffle(deck,disposal)
                        disposal=Stack()
                    tempcard = deck.pop()
                    if (temp3 == 0):
                        cash.double_down()
                    else:
                        cash.double_downsplit()
                    print("Your card is the", tempcard.symbol, "of", tempcard.suit)
                    sum += tempcard.value
                    if sum>21:
                        sum-=10
                    print("Your sum is", sum)
                    person1.push(tempcard)
                    if (splitsum == 0):
                        break
                    else:
                        print("Playing second deck")
                        temp3 = sum
                        sum = splitsum
                        r=check(sp)
                        if sum==21:
                            print('Your second deck has 21')
                        elif sum == 9 or sum == 10 or sum == 11 or r==True:
                            print("Choose an option for second deck")
                            print("Press d to double down")
                            print("Press h to hit")
                            print("Press st to stand")
                        else:
                            print("Choose an option")
                            print("Press h to hit")
                            print("Press st to stand")
                        splitsum = 0
                        disposal = empty(person1, disposal)
                        person1 = sp
                        if sum==21:
                            temp5=1
                            break
                elif ((l.lower() == "sp" or l.lower()=="split") and (temp == 2 or temp == 3)):
                    cash.split()
                    sp.push(person1.pop())
                    if card1.symbol != "Ace":
                        splitsum = int(sum/2)
                    else:
                        splitsum = 11
                        sum=11
                        if deck.peek().value==10000:
                            deck=shuffle(deck,disposal)
                            disposal=Stack()
                        card1=deck.pop()
                        if deck.peek().value==10000:
                            deck=shuffle(deck,disposal)
                            disposal=Stack()
                        card2=deck.pop()
                        print("The", card1.symbol, "of", card1.suit, "has been assigned to first deck and the",
                        card2.symbol, "of", card2.suit, "has been assigned to the second")
                        person1.push(card1)
                        sp.push(card2)
                        sum+=card1.value
                        splitsum+=card2.value
                        if (sum == 22):
                            card1.value = 1
                            sum -= 10
                        if (splitsum == 22):
                            card2.value = 1
                            splitsum -= 10
                        print("Deck one has",splitsum)
                        print("Deck two has",sum)
                        disposal=empty(person1,disposal)
                        disposal=empty(sp,disposal)
                        temp3=splitsum
                        break                        
                    sum = splitsum
                    if deck.peek().value==10000:
                        deck=shuffle(deck,disposal)
                        disposal=Stack()
                    card1 = deck.pop()
                    if deck.peek().value==10000:
                        deck=shuffle(deck,disposal)
                        disposal=Stack()
                    card2 = deck.pop()
                    print("The", card1.symbol, "of", card1.suit, "has been assigned to first deck and the",
                        card2.symbol, "of", card2.suit, "has been assigned to the second")
                    sum += card1.value
                    splitsum += card2.value
                    print("The first deck has", sum)
                    print("The second deck has", splitsum)
                    person1.push(card1)
                    sp.push(card2)
                    if sum==21:
                        a=5
                    elif sum == 9 or sum == 10 or sum == 11:
                        print("Choose an option for first deck")
                        print("Press d to double down")
                        print("Press h to hit")
                        print("Press st to stand")
                    else:
                        print("Choose an option for first deck")
                        print("Press h to hit")
                        print("Press st to stand")
                    if (sum==21):
                        temp=1
                else:
                    print("Invalid input")
    print()
    temp4 = 0
    if temp3 != 0:
        temp4 = sum
        sum = temp3
        temp3 = temp4
    if sum > 21:
        print("You lose deck one. You busted.")
        cash.lose()
        print("The dealer's second card is the",
              dealercard2.symbol, "of", dealercard2.suit)
        dealersum += dealercard2.value
        dealer.push(dealercard2)
        if dealersum == 21:
            temp2 = 1
            cash.insurance_win()
        else:
            cash.insurance_loss()
    else:
        print("The dealer's second card is the",
              dealercard2.symbol, "of", dealercard2.suit)
        dealersum += dealercard2.value
        dealer.push(dealercard2)
        print("The dealer has", dealersum)
        if dealersum == 21:
            temp2 = 1
            cash.insurance_win()
        else:
            cash.insurance_loss()
        while True:
            if dealersum > 21:
                checkace2 = Stack()
                while(dealer.isEmpty() == False):
                    hope2 = dealer.pop()
                    if hope2.value == 11:
                        dealersum -= 10
                        print("Dealer's ace is now 1")
                        hope2.value = 1
                        dealer.push(hope2)
                        dealer = empty_no_ace(checkace2, dealer)
                        checkace2 = Stack()
                        print("The dealer has", dealersum)
                        break
                    else:
                        checkace2.push(hope2)
                if(checkace2.size() != 0):
                    break
            if dealersum > 16 and dealersum < 22:
                break
            if deck.peek().value==10000:
                deck=shuffle(deck,disposal)
                disposal=Stack()
            cardmore = deck.pop()
            print("The dealer's card is the",
                  cardmore.symbol, "of", cardmore.suit)
            dealersum += cardmore.value
            dealer.push(cardmore)
            print("The dealer has", dealersum)
        if (dealersum > 21 or dealersum < sum):
            if (dealersum>21):
                print("Computer busted on deck one")
            else:
                print("You got a higher score on deck one. Dealer got",dealersum, "and you got",sum)
            if temp3==0 and sum==21 and temp==1:
                cash.blackjack()
            else:
                cash.win()
        elif(dealersum > sum):
            print("You lose deck one. Dealer score was",
                  dealersum, "and your score is", sum)
            cash.lose()
        else:
            if (temp == 1 and temp2 == 1):
                print("Push. Both got blackjack on deck one")
                cash.push()
            elif temp == 1:
                print("You win, you have blackack on deck one")
                if (temp3==0):
                    cash.blackjack()
                else:
                    cash.win()
            elif temp2 == 1:
                print("You lose deck one, computer has blackjack")
                cash.lose()
            else:
                print("Push on deck one, dealer score is",
                      dealersum, "and your score is", sum)
                cash.push()
    if temp3 != 0:
        if temp3 > 21 or dealersum > temp3 and dealersum < 22:
            if (temp3>21):
                print("You busted deck two")
            else:
                print("You got a lower score on deck two. Dealer got",dealersum, "and you got",temp3)
            cash.split_lose()
        elif (dealersum > 21 or dealersum < temp3):
            if (dealersum>21):
                print("Computer busted on deck two")
            else:
                print("You got a higher score on deck two. Dealer got",dealersum, "and you got",temp3)
            cash.split_win()
        else:
            if (temp5 == 1 and temp2 == 1):
                print("Push on deck two. Both of you got blackjack")
                cash.split_push()
            elif temp5 == 1:
                print("Your second deck won, it had blackjack")
                cash.split_win()
            elif temp2 == 1:
                print("Your second deck lost, computer had blackjack")
                cash.split_lose()
            else:
                print("Push, tie score between second deck and computer")
                cash.split_push()
    sum = 0
    splitsum = 0
    dealersum = 0
    temp5 = 0
    temp4 = 0
    temp3 = 0
    temp2 = 0
    temp = 0
    disposal = empty(person1, disposal)
    disposal = empty(dealer, disposal)
    disposal=empty(checkace,disposal)
    disposal=empty(checkace2,disposal)
    person1 = Stack()
    dealer = Stack()
    r=False

print("Your final amount is",cash.see_cash(), "dollars")
print("Press enter to quit")
r=input()
