# euler problem 54

###card rankiings
num_rank = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['H','S','C','D']
card_rank = []
for n in num_rank:
    for s in suits:
        card_rank.append(n+s)

### list must be sorted
def hand_win(s_hand1,s_hand2):
    ### a royal flush?
    f1 = flush(s_hand1)
    s1 = straight(s_hand1)
    f2 = flush(s_hand2)
    s2 = straight(s_hand2)
    if f1> -1 and s1 > -1:
        sf1 = f1*s1
    else:
        sf1 = -1
    if f2> -1 and s2 > -1:
        sf2 = f2*s2
    else:
        sf2 = -1
    h1 = [sf1,four_of_a_kind(s_hand1),full_house(s_hand1),f1,s1,three_of_a_kind(s_hand1),two_pair(s_hand1),pair(s_hand1),high_card(s_hand1)]
    h2 = [sf2,four_of_a_kind(s_hand2),full_house(s_hand2),f2,s2,three_of_a_kind(s_hand2),two_pair(s_hand2),pair(s_hand2),high_card(s_hand2)]
    for i in range(0,len(h1)):
        if h1[i] > -1 or h2[i] > -1:
            if h1[i] > h2[i]:
                return 1
            else:
                return 0
    
def flush(hand):
    if hand[0]%4 == hand[1]%4 and hand[0]%4 == hand[2]%4 and hand[0]%4 == hand[3]%4 and hand[0]%4 == hand[4]%4:
        return hand[4]*13000 + hand[3]*1300 + hand[2]*130 + hand[1]*13 + hand[0]
    return -1
    
def straight(hand):
    if hand[0]/4 == hand[1]/4-1 and hand[0]/4 == hand[2]/4 - 2 and hand[0]/4 == hand[3]/4 - 3 and hand[0]/4 == hand[4]/4 -4:
        return hand[0]
    return -1

def four_of_a_kind(hand):
    if hand[0]/4 == hand[1]/4 and hand[0]/4 == hand[2]/4 and hand[0]/4 == hand[3]/4:
        return hand[0]
    elif hand[1]/4 == hand[2]/4 and hand[1]/4 == hand[3]/4 and hand[1]/4 == hand[4]/4:
        return hand[1]
    return -1

def three_of_a_kind(hand):
    if hand[0]/4 == hand[1]/4 and hand[0]/4 == hand[2]/4:
        return hand[0]
    elif hand[1]/4 == hand[2]/4 and hand[1]/4 == hand[3]/4:
        return hand[1]
    elif hand[2]/4 == hand[3]/4 and hand[2]/4 == hand[4]/4:
        return hand[2]
    return -1
def full_house(hand):
    if hand[0]/4 == hand[1]/4 and hand[0]/4 == hand[2]/4 and hand[3]/4 == hand[4]/4:
        return hand[0]
    elif hand[2]/4 == hand[3]/4 and hand[2]/4 == hand[4]/4 and hand[0]/4 == hand[4]/4:
        return hand[2]
    return -1
def two_pair(hand):
    if hand[0]/4 == hand[1]/4 and hand[2]/4 == hand[3]/4:
        return hand[2]*130+hand[0]*13+hand[4]
    elif hand[0]/4 == hand[1]/4 and hand[3]/4 == hand[4]/4:
        return hand[3]*130+hand[0]*13+hand[2]
    elif hand[1]/4 == hand[2]/4 and hand[3]/4 == hand[4]/4:
        return hand[3]*130+hand[1]*13+hand[0]
    return -1

def pair(hand):
    if hand[0]/4 == hand[1]/4:
        return hand[0]*1300+hand[4]*130+hand[3]*13+hand[2]
    elif hand[1]/4 == hand[2]/4:
        return hand[1]*1300+hand[4]*130+hand[3]*13+hand[0]
    elif hand[2]/4 == hand[3]/4:
        return hand[2]*1300+hand[4]*130+hand[1]*13+hand[0]
    elif hand[3]/4 == hand[4]/4:
        return hand[3]*1300+hand[2]*130+hand[1]*13+hand[0]
    return -1

def high_card(hand):
    return hand[4]*13000+hand[3]*1300+hand[2]*130+hand[1]*13+hand[0]


### read text file
text_file = open('p054_poker.txt', 'r')
lines = text_file.read().split('\n')
lines = [l.split(" ") for l in lines]   
lines = lines[0:1000]
lines_int = []

for hand in lines:
    l = []
    for card in hand:
        l.append(card_rank.index(card))
    lines_int.append(l)
lines_int = [ [l[0:5],l[5:10]] for l in lines_int]

p1_wins = 0
for hand in lines_int:
    p1 = hand[0]
    p2 = hand[1]
    p1.sort()
    p2.sort()
    p1_wins += hand_win(p1,p2)
