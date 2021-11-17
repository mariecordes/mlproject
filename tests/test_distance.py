from mlproject.distance import haversine

# test dtype - not working
def test_type_of_harversine():
    tst = isinstance(haversine(1, 2, 3, 4), float)
    assert tst == True


# test dtype - working
def test_type_of_harversine2():
    test = type(haversine(1, 2, 3, 4)) is float
    assert test == True

def test_zero_harversine():
    zero = haversine(0, 0, 0, 0)
    assert zero == 0
