# content of test_sample.py
def inc(x):
    return x + 1


def test_case1():
    assert inc(4) == 5
	
def test_case2():
    assert inc(110) == 111

def test_case3():
    assert inc(4) == 5

def test_case4():
    assert inc(8) == 9

def test_case5():
    assert inc(11) == 12