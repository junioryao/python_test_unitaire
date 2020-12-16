import pytest
import numpy
from First_Part import Exercise_One , Exercise_Two ,Calculate,Anagram

test_output = "1\n2\nThree\n4\nFive\nThree\n7\n8\nThree\nFive\n11\nThree\n13\n14\nThreeFive\n16\n17\nThree\n19\nFive\nThree\n22\n23\nThree\nFive\n26\nThree\n28\n29\nThreeFive\n31\n32\nThree\n34\nFive\nThree\n37\n38\nThree\nFive\n41\nThree\n43\n44\nThreeFive\n46\n47\nThree\n49\nFive\nThree\n52\n53\nThree\nFive\n56\nThree\n58\n59\nThreeFive\n61\n62\nThree\n64\nFive\nThree\n67\n68\nThree\nFive\n71\nThree\n73\n74\nThreeFive\n76\n77\nThree\n79\nFive\nThree\n82\n83\nThree\nFive\n86\nThree\n88\n89\nThreeFive\n91\n92\nThree\n94\nFive\nThree\n97\n98\nThree\nFive\n"


def test_first_exercise(capsys):

    Exercise_One()

    captured = capsys.readouterr()

    assert captured.out == test_output

def test_for_exercise_two():
    #color full 
    assert Exercise_Two(263) == True 
    assert Exercise_Two(236) == False
    assert Exercise_Two(2532) == False

#exercise 3 
def test_for_calculate():
    
    assert Calculate(['4', '3', '-2']) ==  5
    assert Calculate(453) == False
    assert Calculate(['nothing', 3, '8', 2, '1']) == 9
    assert Calculate('54') == False

#exercice 4 
def test_for_anagram():
    
    assert Anagram('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']

    assert Anagram('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']

    assert Anagram('laser', ['lazing', 'lazy',  'lacer']) == []



