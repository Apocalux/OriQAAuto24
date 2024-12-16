# def test_check_math(): # def создает функции и методы
#     assert 7 * 7 == 49 # проверяет верность заданного условия

# def test_test_check_78():
#     assert 7 * 8 == 56


# class User:
#     def __init__(self) -> None:
#         self.name = 'Oryna'
#         self.second_name = 'Orion'

# @pytest.fixture  # Фикстура user теперь используется для создания нового объекта User для каждого теста.
# def user():
#     return User()
import pytest

# Тестовые функции получают объект user как аргумент, что гарантирует, что каждое тестирование происходит с чистым состоянием объекта.
@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == 'Orina'

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Orion'
