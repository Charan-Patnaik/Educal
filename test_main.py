from main import add
def test_add_two_numbers():    
    #positive tests
    assert add(2,3) == 5
    assert add(-5 ,-3) == -8
    assert add(-1,1) == 0
    #negative tests
    assert add(2,5) != 9