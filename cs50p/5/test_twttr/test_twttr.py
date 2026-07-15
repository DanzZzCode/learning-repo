from twttr import omit_vowels

def test_omit_vowels():
    assert omit_vowels("Twitter") == "Twttr"
    assert omit_vowels("What's your name?") == "Wht's yr nm?"
    assert omit_vowels("cs50") == "cs50"