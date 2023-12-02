import pytest


class Test_example:

    def test_one(self):
        print('test one is executing......')
        assert 1 + 1 == 2

    def test_two(self):
        print('test two is executing......')
        assert 4 + 2 == 6

    def test_three(self):
        print("I am from third method..")
        assert 1 + 7 == 8

    def test_four(self):
        print('I m from four method')
        assert 1 + 1 == 2