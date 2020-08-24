
import pytest
import random
import string
import session6
import os
import inspect
import re

CONTENT_CHECK = [
    'lambda',
    'zip',
    'map'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in CONTENT_CHECK:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_normal_function():
    code_lines = inspect.getsource(session6.deck_without_using_keyword)
    for word in CONTENT_CHECK:
        assert word not in code_lines, 'Normal function uses keywords lambda, zip and map'

def test_single_expression():
    code_lines = inspect.getsource(session6.deck_with_single_expression)
    for word in CONTENT_CHECK:
        assert word in code_lines, 'Single expression does not use keywords lambda, zip and map'

def test_deck_without_using_keyword_52_cards():
    assert (len(session6.deck_without_using_keyword()) == 52), f"Deck does not have 52 cards"
    
def test_deck_without_using_keyword_52_unique_cards():
    assert (len(set(session6.deck_without_using_keyword())) == 52), f"Deck should have unique cards"

def test_deck_manual_check():
    cards = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'), ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'), ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'), ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'), ('9', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('10', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'), ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]
    assert (False for i in session6.deck_without_using_keyword() if i not in cards == False), f"Incorrect cards"

def test_deck_with_single_expression_52_cards():
    assert (len(session6.deck_with_single_expression()) == 52), f"Deck does not have 52 cards"

def test_deck_with_single_expression_52_unique_cards():
    assert (len(set(session6.deck_with_single_expression())) == 52), f"Deck should have unique cards"

def test_deck_single_expression_manual_check():
    cards = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'), ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'), ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'), ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'), ('9', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('10', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'), ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]
    assert (False for i in session6.deck_with_single_expression() if i not in cards == False), f"Incorrect cards"

def test_number_of_cards_per_player():
    with pytest.raises(Exception):
            set1 = random.sample(session6.deck_without_using_keyword,6)
            set2 = random.sample(session6.deck_without_using_keyword,6)
            session6.match(set1,set2), 'Number of cards should be 3 or 4 or 5'
    with pytest.raises(Exception):
            set1 = random.sample(session6.deck_without_using_keyword,1)
            set2 = random.sample(session6.deck_without_using_keyword,1)
            session6.match(set1,set2), 'Number of cards should be 3 or 4 or 5'

def test_same_number_of_cards_per_player():
    with pytest.raises(Exception):
            set1 = random.sample(session6.deck_without_using_keyword,3)
            set2 = random.sample(session6.deck_without_using_keyword,5)
            session6.match(set1,set2), 'Players should have same number of cards'
    with pytest.raises(Exception):
            set1 = random.sample(session6.deck_without_using_keyword,5)
            set2 = random.sample(session6.deck_without_using_keyword,4)
            session6.match(set1,set2), 'Players should have same number of cards'

def test_repeating_cards():
    with pytest.raises(Exception):
            set1 = [('5', 'spades'), ('8', 'spades'), ('7', 'spades'), ('3', 'spades'), ('10', 'spades')]
            set2 = [('5', 'clubs'), ('8', 'hearts'), ('7', 'diamonds'), ('10', 'spades'), ('2', 'spades')]
            session6.match(set1,set2), 'Only one deck of cards used. Same card occurance for both players'
    with pytest.raises(Exception):
            set1 = [('ace', 'diamonds'), ('8', 'spades'), ('7', 'spades')]
            set2 = [('5', 'clubs'), ('8', 'hearts'), ('ace', 'diamonds')]
            session6.match(set1,set2), 'Only one deck of cards used. Same card occurance for both players'

def test_docstrings_available():
    assert ((session6.deck_without_using_keyword.__doc__) != None), f"Docstrings missing"
    assert ((session6.match.__doc__) != None), f"Docstrings missing"
    assert ((session6.flush.__doc__) != None), f"Docstrings missing"

def test_annotationss_available():
    assert ((len(session6.match.__annotations__)) != 0), f"Annotations missing"
    assert ('return' in (session6.match.__annotations__.keys())), f"Annotations missing return"

def test_combinations_and_winner():
    #1 straight flush > high card
    set1 = [('ace', 'spades'), ('king', 'spades'), ('7', 'spades'), ('3', 'spades'), ('10', 'spades')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds'), ('10', 'clubs'), ('4', 'spades')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    #2 flush > straight
    set1 = [('ace', 'spades'), ('king', 'diamond'), ('queen', 'clubs'), ('jack', 'hearts'), ('10', 'spades')]
    set2 = [('2', 'clubs'), ('king', 'clubs'), ('6', 'clubs'), ('10', 'clubs'), ('4', 'clubs')]
    assert (session6.match(set1,set2) == 2), f"Wrong winner"
    #3 two pair > one pair
    set1 = [('2', 'spades'), ('2', 'clubs'), ('7', 'spades'), ('3', 'spades'), ('3', 'diamond')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds'), ('ace', 'hearts'), ('4', 'spades')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    #4 four of a kind > full house
    set1 = [('10', 'spades'), ('10', 'diamonds'), ('10', 'clubs'), ('10', 'hearts'), ('8', 'spades')]
    set2 = [('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds'), ('king', 'clubs'), ('king', 'spades')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    #5 royal flush > straight flush
    set1 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    #6 three of a kind > high card
    set1 = [('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('3', 'spades'), ('jack', 'spades')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds'), ('4', 'clubs'), ('4', 'spades')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    #7 same ranks
    set1 = [('10', 'clubs'), ('jack', 'spades'), ('queen', 'hearts'), ('3', 'clubs'), ('9', 'spades')]
    set2 = [('jack', 'clubs'), ('10', 'hearts'), ('3', 'diamonds'), ('9', 'clubs'), ('queen', 'spades')]
    assert (session6.match(set1,set2) == 0), f"Wrong winner. Split the pot"

    set1 = [('ace', 'spades'), ('king', 'spades'), ('7', 'spades')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    
    set1 = [('ace', 'spades'), ('king', 'diamond'), ('queen', 'clubs')]
    set2 = [('2', 'clubs'), ('king', 'clubs'), ('6', 'clubs')]
    assert (session6.match(set1,set2) == 2), f"Wrong winner"
    
    set1 = [('2', 'spades'), ('2', 'clubs'), ('7', 'spades')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    
    set1 = [('10', 'spades'), ('10', 'diamonds'), ('10', 'clubs')]
    set2 = [('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]
    assert (session6.match(set1,set2) == 2), f"Wrong winner"
    
    set1 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    
    set1 = [('10', 'spades'), ('10', 'clubs'), ('10', 'hearts')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    
    set1 = [('10', 'clubs'), ('jack', 'spades'), ('queen', 'hearts')]
    set2 = [('jack', 'clubs'), ('10', 'hearts'), ('3', 'diamonds')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner. Split the pot"

    set1 = [('ace', 'spades'), ('king', 'spades'), ('7', 'spades'), ('3', 'spades')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds'), ('10', 'clubs')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    
    set1 = [('ace', 'spades'), ('king', 'diamond'), ('queen', 'clubs'), ('jack', 'hearts')]
    set2 = [('2', 'clubs'), ('king', 'clubs'), ('6', 'clubs'), ('10', 'clubs')]
    assert (session6.match(set1,set2) == 2), f"Wrong winner"
    
    set1 = [('2', 'spades'), ('2', 'clubs'), ('7', 'spades'), ('3', 'spades')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds'), ('ace', 'hearts')]
    assert (session6.match(set1,set2) == 2), f"Wrong winner"
    
    set1 = [('10', 'diamonds'), ('10', 'clubs'), ('10', 'hearts'), ('8', 'spades')]
    set2 = [('ace', 'hearts'), ('ace', 'diamonds'), ('king', 'clubs'), ('king', 'spades')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    
    set1 = [('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    set2 = [('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    
    set1 = [('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('3', 'spades')]
    set2 = [('ace', 'clubs'), ('king', 'hearts'), ('6', 'diamonds'), ('4', 'clubs')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner"
    
    set1 = [('jack', 'spades'), ('queen', 'hearts'), ('3', 'clubs'), ('9', 'spades')]
    set2 = [('10', 'hearts'), ('3', 'diamonds'), ('9', 'clubs'), ('queen', 'spades')]
    assert (session6.match(set1,set2) == 1), f"Wrong winner. Split the pot"