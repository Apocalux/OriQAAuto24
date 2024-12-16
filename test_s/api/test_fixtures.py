# import pytest

# class User:

#     def __init__(self) -> None:
#         self.name = None
#         self.second_name = None
    
#     def create(self):
#         self.name = 'Ori'
#         self.second_name = 'Orion'
    
#     def remove(self):
#         self.name = ''
#         self.second_name = ''

#     def test_change_name():
#         user = User()
#         user.create()

#         assert user.name == 'Ori'
import pytest

@pytest.mark.check
def test_change_second_name(user):
   assert user.second_name == 'Orion' # user = User()
    # user.create()

@pytest.mark.check 
def test_change_name(user): # assert user.second_name == 'Orion'
    assert user.name =='Orina' # user.remove()

# @pytest.fixture
# def user():
#     user = User()
#     user.create()

#     yield user
    
#     user.remove()
