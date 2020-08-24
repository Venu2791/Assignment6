
import random
from itertools import groupby
from collections import defaultdict,Counter

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
cardvalue={'2':2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"jack":11,"queen":12,'king':13,"ace":14}

def deck_with_single_expression():
    """This is a special function (using lambda,zip,map).
    It is used for creating a deck of 52 cards.
    Return - list of 52 tuples (values,suits)"""
    deck=sum(map(lambda x:list(map(lambda y: (x,y),suits)),vals),[])
    return deck

def deck_without_using_keyword():
    """ This is a normal function (without using keywords).
    It is used for creating a deck of 52 cards.
    Return - list of 52 tuples (values,suits) """
    cards = [(x,y) for x in vals for y in suits]
    return cards

def flush(hand):
    """ {h[1] for h in player1}
    check for flush, so if all the cards are from the same suite it's flush. 
    Royal or straight could be validated with other with the sum of values. """
    suits = {h[1] for h in hand}
    if len(suits) == 1:
        return True
    return False

def acevalue(set):
    if straight:
        if "ace" in {h[0] for h in set}:
            if '2' in {h[0] for h in set}:
                cardvalue.update({"ace": 1})

def straight(hand):
    cards=[h[0] for h in hand]
    values=[cardvalue[i] for i in cards]  
    value_sum=max(values)-min(values)       
    if len(set(Counter(hand).values()))==1 and value_sum==len(hand)-1:
        return True
    return False
def four_ofa_kind(hand):
    if len(hand)>3:
        cards=[h[0] for h in hand]
        #values = [i[0] for i in hand]
        countlist=sorted(list(Counter(cards).values()))
        #print(countlist)
        if countlist==[1,4]:
            return True
        if countlist==[4]:
            return True
    return False      

def three_ofa_kind(hand):
    cards=[h[0] for h in hand]
    #values = [i[0] for i in hand]
    countlist=sorted(list(Counter(cards).values()))
    if countlist==[1,1,3]:
        return True
    if countlist==[1,3]:
        return True
    if countlist==[3]:
        return True
    return False     

def two_pair(hand):
    if len(hand)>3:
        cards=[h[0] for h in hand]
        #values = [i[0] for i in hand]
        countlist=sorted(list(Counter(cards).values()))
        count2=Counter(countlist)
        if count2[2]==2:
            return True
    return False
def one_pair(hand):
    cards=[h[0] for h in hand]
    #values = [i[0] for i in hand]
    countlist=sorted(list(Counter(cards).values()))
    count2=Counter(countlist)
    if count2[2]==1:
        return True
    return False
def fullhouse(hand):
    cards=[h[0] for h in hand]
    #values = [i[0] for i in hand]
    countlist=sorted(list(Counter(cards).values()))
    if countlist==[2,3]:
        return True
    return False  
def rank(hand):
    if flush(hand) and straight(hand):
        return 1
    if four_ofa_kind(hand):
        return 2
    if fullhouse(hand):
        return 3
    if flush(hand):
        return 4
    if straight(hand):
        return 5
    if three_ofa_kind(hand):
        return 6
    if two_pair(hand):
        return 7
    if one_pair(hand):
        return 8
    return 9

def match(player1: 'string player 1 deck', player2: 'string player 2 deck') -> 'winner of the game':
    """ This function is used to distribute the cards among two players.
    It gives who the winner of the game is. 
    Input - set of cards of player 1 and player 2
    Return - winner of the game 
    Returns 1 if player 1 wins, 2 if player 2 wins and 0 if pot is split """
    if((len(player1) not in [3,4,5]) or (len(player2) not in [3,4,5])):
        raise Exception("3 or 4 or 5 cards per player")
    if(len(player1) != len(player2)):
        raise Exception("Players must have same number of cards")
    count = 0
    for i in range(len(player1)):
        if player1[i] in (player2):
            count = 1
    if count == 1:
        raise Exception("Only one deck of cards used. Same card occurance for both players")
    player1_rank=  rank(player1)
    player2_rank=rank(player2)
    if player1_rank < player2_rank:
        winner= 1
    elif player1_rank == player2_rank:
        acevalue(player1)
        player1_value = sum([cardvalue[i] for i in [h[0] for h in player1]])
        cardvalue.update({"ace":14})
        acevalue(player2)
        player2_value =sum([cardvalue[i] for i in [h[0] for h in player2]])
        if player1_value>player2_value:
            winner= 1
        elif player1_value==player2_value:
            winner= 0
        else:
            winner= 2    
    else:
        winner= 2    
    return winner