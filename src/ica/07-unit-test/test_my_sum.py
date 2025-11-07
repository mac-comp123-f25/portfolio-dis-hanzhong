from my_sum import*

def test_sum3_ints():
    assert sum3([1, 2, 3]) == 6
    assert sum3([-1, 0, 5]) == 4
    assert sum3([-2, -3, -4]) == -9
    assert sum3([100, 200, 300]) == 600



def test_sum3_floats():
    assert sum3([1.5, 2.5, 3.5, 8]) == 7.5
    assert sum3([-1.5, 2.0, 3.5]) == 4.0
    assert sum3([0.2, 0.2, 0.3]) == 0.7
    assert sum3([1, 2.5, 3]) == 6.5
    assert sum3([100.75, 200.25, 300.5]) == 601.5





