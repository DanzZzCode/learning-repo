from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("0/5") == 0
    assert convert("1/5") == 20
    with pytest.raises(ValueError):
        convert("5/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0") 
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat/5")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"