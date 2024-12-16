import pytest

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None
    
    def create(self):
        self.name = 'Orina'
        self.second_name = 'Orion'
    
    def remove(self):
        self.name = ''
        self.second_name = ''

    def test_change_name():
        user = User()
        user.create()

        assert user.name == 'Orina'


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user
    
    user.remove()
