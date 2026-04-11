from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"