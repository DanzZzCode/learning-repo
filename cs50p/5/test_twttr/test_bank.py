from bank import checkg

def test_zero():
    assert checkg("hello") == 0

def test_twenty():
    assert checkg("hi") == 20

def test_hundred():
    assert checkg("doesn't start with h") == 100