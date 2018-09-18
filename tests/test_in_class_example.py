import pytest

from click.testing import CliRunner

from example import *

class TestExample(unittest.TestCase):
#@pytest.fixture
        
        

    def TestGreetingStudent(self):
        assert GreetingStudent("2019")
        self.assertEqual("Welcome back seniors",GreetingStudent)
