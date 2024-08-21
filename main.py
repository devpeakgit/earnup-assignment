
# Author: Will Mitchell
# Date: August 21, 2024
# Description: Rest Service to return valid and invalid sets based on card input

from typing import List, Tuple
from fastapi import FastAPI
from pydantic import BaseModel, Field, validator

class Card(BaseModel):
    id: int # Added id to allow easier debugging
    shape: int = Field(1, ge=1, le=3)
    color: int = Field(1, ge=1, le=3)
    shade: int = Field(1, ge=1, le=3)
    number: int = Field(1, ge=1, le=3)

    @validator('shape', 'color', 'shade', 'number')
    def value_between_one_and_three(cls, v):
        if not 1 <= v <= 3:
            raise ValueError('Value must be between 1 and 3')
        return v         
app = FastAPI()


@app.get('/')
async def index():
    return {"message": "Hello EarnUp"}

@app.post('/generate_sets')
async def generate_sets(cards: List[Card] ) :
    
    valid, invalid = generate_all_sets(cards)
    # for valid_set in valid_sets:
    #     print(valid_set)
    
    return {
        "valid_sets": valid,
        "invalid_sets":invalid    
    }
    
def all_same_or_all_different(values):
        # do we have a set of 3 (all the same) or a set of 1 (all different)
        return len(set(values)) in [1, 3]

def is_valid_set(cards):
    
    for attribute in ['shape', 'color', 'shade', 'number']:
        # essentially we are going to iterate thru each card 
        # looking at the same attribute and test the values
        values = [getattr(card,attribute) for card in cards]
            
        if not all_same_or_all_different(values):
            return False
    return True

# Big O(n3) - terrible !
# Assumes setsize of s3
# TODO look at using internal combinations lib to improve this treacle nested looping
def generate_all_sets(cards: List[Card]) -> Tuple[List[Card], List[Card]]:

    valid_sets = []
    invalid_sets = []
    n = len(cards)
    # Go thru all the cards
    for i in range(n):
        # compare against the next card
        for j in range(i + 1, n):
            # compare against the next-next card
            for k in range(j + 1, n):
                combo = [cards[i], cards[j], cards[k]]
                if is_valid_set(combo):
                    valid_sets.append(combo)
                else:
                    invalid_sets.append(combo)    
    return valid_sets, invalid_sets
