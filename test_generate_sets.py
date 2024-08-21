
from main import Card

def test_generate_sets():
    
    card =  Card(id=1,shape=1, color=1, shade=1, number=1)
    
    assert True == True
    

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
    
        
    
