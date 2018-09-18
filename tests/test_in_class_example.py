import pytest

from click.testing import CliRunner

from example import *

class TestExample(unittest.TestCase):
#@pytest.fixture
        
        

    def TestGreetingStudent(self):
        assert GreetingStudent("2019")
        self.assertEqual("Welcome back seniors",GreetingStudent)
        assert GreetingStudent("2020")
        self.assertEqual("Welcome back juniors",GreetingStudent)
        assert GreetingStudent("2021")
        self.assertEqual("Welcome back sophmors",GreetingStudent)
        assert GreetingStudent("2022")
        self.assertEqual("Welcome to college",GreetingStudent)
