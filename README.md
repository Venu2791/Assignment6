# Session 6 – Test Cases and code understanding : Poker rules to determine if player 1 or player 2 wins
### Question 1 : To create deck of cards using lambda, zip and map
Here we have used lambda and map functions to create a deck of 52 cards
### Question 2 : To create deck of cards as a normal function without using lambda, zip and map
Here we have used list comprehension to create a deck of 52 cards
## Test Cases
1)  README exists
2)  README has at least 500 words
3)  Methods mentioned in README
4)  README file formatting 
5)  Code Indentation and spaces
6)  Function name should be in small letters
7)  If in question 1, keywords are used
8)  If there are only 52 cards in the deck created using the above method
9)  If the 52 cards are unique and no repetition 
10) Manual check if the cards are matching with the deck of 52 cards
11) If in question 2, keywords are not used
12) If there are only 52 cards in the deck created using the above method
13) If the 52 cards are unique and no repetition 
14) Manual check if the cards are matching with the deck of 52 cards
15) Checking if the both the players have got only 3 or 4 or 5 cards
16) Checking if both the players have got equal number of cards
17) Since only one deck of cards is allowed, the cards distributed to players must be unique and among both players also, the cards must be unique
18) Check if docstrings are available for the functions used in question 2 and question 3
19) Check if annotations are available for the function used in question 3 and if the annotation has a return mentioned
20) Check if the correct winner is returned for the particular hand. 20 such combination of hands are tested 
### Poker rules and determining the winner : 
Below is the explanation of rules considered for 3 or 4 or 5 cards : 
1)  FLUSH : If all the cards are from the same suit, then it is a flush 
2)  STRAIGHT : Now, based on the values it can be checked if it is a straight flush or royal flush. A dictionary is created and values are assigned to values of cards. In the beginning, ace is assigned a value of 14. If it is a straight and If the card 2 is present in a player’s hand, then the value of ace is considered to be 1
3)  FOUR OF A KIND : Four of a kind is applicable if the number of cards of a particular hand is greater than 3. If we get all the cards of a same value for 4 cards or if we get 4 cards of same value for 5 cards then it is four of a kind
4)  THREE OF A KIND : Three of a kind is applicable for 3 or 4 or 5 cards. If all three are of same value in 3 cards or if 3 are of same value in 4 and 5 cards, then it is considered as three of a kind
5)  TWO PAIR : Applicable only for 4 or 5 cards. If two pairs have the same value, then it is a two pair
6)  ONE PAIR : If there is one pair, that is two cards with the same value, then it is one pair
7)  FULL HOUSE : Applicable for 5 cards. If 3 cards have the same value and 2 cards have the same value, then it is a full house.
Order : 
Royal Flush 
Straight Flush
Four of a kind
Full house
Flush
Straight
Three of a kind
Two pair
One pair
Any other combination

8)  ANY COMBINATION : For any combination, each card among the two players are considered, using the dictionary and the player with highest card wins. If all the cards are of same value, then the pot is split
The function returns 2, if player 2 wins; 1, if player 1 wins and 0, if pot is split.
