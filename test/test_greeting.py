# https://youtu.be/nLRL_NcnK-4?t=25062

from greeting import greeting

def test_default():
    assert greeting() == "hello, world"

def test_argument():
    assert greeting("Alice") == "hello, Alice"

