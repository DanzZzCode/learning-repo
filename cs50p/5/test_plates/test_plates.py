from plates import is_valid

def test_twolet():
    assert is_valid("AA1000") == True
    assert is_valid("100000") == False
    assert is_valid("A10000") == False

def test_twotosix():
    assert is_valid("AA") == True
    assert is_valid("AA1000") == True
    assert is_valid("AA100") == True
    assert is_valid("A") == False
    assert is_valid("AAAA100") == False
    assert is_valid("") == False

def test_endnum():
    assert is_valid("AAAA10") == True
    assert is_valid("AA1000") == True
    assert is_valid("AAAAA1") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AA0000") == False

def test_num_position():
    # CRITICAL ADDITION: Letters cannot follow numbers
    assert is_valid("AAA22A") is False
    assert is_valid("AA10B") is False


def test_nopunc():
    assert is_valid("AA1000") == True
    assert is_valid("AA10.0") == False