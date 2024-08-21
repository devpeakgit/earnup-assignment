
from math import comb
from main import Card, generate_all_sets

def test_generate_sets():
           
    test_data = [
        Card(id=1,shape=1, color=1, shade=1, number=1),
        Card(id=2,shape=2, color=2, shade=2, number=2),
        Card(id=3,shape=3, color=3, shade=3, number=3),    
        Card(id=4,shape=1, color=1, shade=1, number=2),   
        Card(id=5,shape=1, color=1, shade=1, number=3),   
    ]
    #2
    expected_valid = [
        [ 
        Card(id=1,shape=1, color=1, shade=1, number=1),
        Card(id=2,shape=2, color=2, shade=2, number=2),
        Card(id=3,shape=3, color=3, shade=3, number=3)],
        [
        Card(id=1,shape=1, color=1, shade=1, number=1),     
        Card(id=4,shape=1, color=1, shade=1, number=2),
        Card(id=5,shape=1, color=1, shade=1, number=3),   
        ]
    ]
    # We should have about 10 sets in total - 2 valid and 8 invalid
    num_combinations = comb(len(test_data), 3)
    assert(num_combinations) == 10
   
    
    valid, invalid = generate_all_sets(test_data)
    assert len(valid) == len(expected_valid)
    assert len(invalid) == 8
    assert expected_valid == valid
    

def test_no_valid_sets():
    # No valid sets
    test_data = [
        
        Card(id=1,shape=3, color=3, shade=3, number=3),
        Card(id=2,shape=3, color=3, shade=3, number=3),
        Card(id=3,shape=3, color=3, shade=1, number=1),
        
    ]
    expected_valid = [
    ]
    
    expected_invalid = [
        [
            Card(id=1,shape=3, color=3, shade=3, number=3),
            Card(id=2,shape=3, color=3, shade=3, number=3),
            Card(id=3,shape=3, color=3, shade=1, number=1),
        ]  
    ]
    
    valid, invalid  = generate_all_sets(test_data)
    assert valid == expected_valid
    assert valid == []
    
    assert len(invalid) == len(expected_invalid)
    assert invalid == expected_invalid
    
def test_single_card():
    # No valid or invalid sets
    test_data = [
        
        Card(id=1,shape=3, color=3, shade=3, number=3),
        
    ]
    expected_valid = [
    ]
    
    expected_invalid = [
    ]
    
    valid, invalid  = generate_all_sets(test_data)
    assert valid == expected_valid
    assert invalid == expected_invalid
    
        
    
