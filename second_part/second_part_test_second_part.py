import pytest

from second_part_src import div, raise_something, add, ForceToList, random_gen, get_info, CacheDecorator, checkProcess


def test_generator():
    g = random_gen()
    print(g)
    assert isinstance(g, type((x for x in [])))
    a = next(g)
    while a != 15:
        assert 10 <= a <= 20
        a = next(g)
    with pytest.raises(StopIteration):
        next(g)


def test_to_str():
    assert add(5, 30) == '35'
    assert get_info({'info': [1, 2, 3]}) == '[1, 2, 3]'


def test_meta_list():
    test = ForceToList([1, 2])
    assert test[1] == 2
    assert test.x == 4


def test_for_cache_decorator():

    # create an object of cache decorator
    obj = CacheDecorator()

    # passing any desire function
    store_upper_funtion1 = obj.__call__(lambda x: x**2)
    store_upper_funtion2 = obj.__call__(lambda x, y: x*y)

    assert store_upper_funtion1(7) == 49
    assert store_upper_funtion2(3, 4) == 12




# Exercise 6 test

def test_for_checking_a_valid_metaclass_one(capsys):

    class hello(metaclass=checkProcess):
        # has process with 3 inputs args
        def process(self, a, b, c):
            pass

    ss, ii = capsys.readouterr()

    assert ss == "class inherit successfully\n"


def test_for_checking_a_valid_metaclass_two(capsys):

    class hello2(metaclass=checkProcess):
        # has process but not with 3 arguments
        def process(self, a, b):
            pass

    ss, ii = capsys.readouterr()

    assert ss == "Missing function with 3 parameters\n"


def test_for_checking_a_valid_metaclass_three(capsys):

    class hello3(metaclass=checkProcess):
        # do not have process methode
        def water(self):
            pass

    ss, ii = capsys.readouterr()

    assert ss == "Missing function with 3 parameters\n"


def test_ignore_exception():
    assert div(10, 2) == 5
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)