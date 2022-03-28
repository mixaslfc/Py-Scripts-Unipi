import random
from colorama import Back, Fore, Style

figures=['J','Q','K'] 
fyllo=[i for i in range(1,11)]+ figures 
colors=['♧,', '♦', '♥', '♤'] 

def sum_cards(crds):
    score=0
    for card in crds:
        if card[0] in figures:
            score+=10
        else:
            score+=card[0]
    return score    

def print_cards(crds):
    tmp=""
    for c in crds:
        if c[1] in ['♦', '♥']:
            tmp=tmp+Fore.RED
        tmp+=str(c[0])+c[1]+" "
        if c[1] in ['♦', '♥']:
            tmp=tmp+Style.RESET_ALL 
    return tmp

def winner(crds1,crds2):    
    result=""
    if crds1>21:
        result="Player 1 busted"
    elif crds2>21:
        result="Player 2 busted"
    elif crds1>crds2: 
        result="Player 1 wins"
    elif crds2>crds1:
        result="Player 2 wins"
    else:   
        result="Draw"
    return result   

for i in range(1):
    cards=[]

    for i in fyllo:
        for j in colors:
            cards.append([i,j])

    random.shuffle(cards)

    player1=[]
    while sum_cards(player1)<17:
        player1.append(cards.pop())
    print(print_cards(player1))
    score_p1=sum_cards(player1)

    # print("Player 2 joins the game")
    player2=[]
    while sum_cards(player2)<16:
        player2.append(cards.pop())
    print(print_cards(player2))
    score_p2=sum_cards(player2)

    print(winner(score_p1,score_p2))


    