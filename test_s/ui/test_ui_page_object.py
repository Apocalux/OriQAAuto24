from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui
def test_check_incorrect_page_object():
    #Создание объекта страницы
    sign_in_page = SignInPage()

    # Открываем страницу https://github.com/login
    sign_in_page.go_to()

    #Попытка входа в систему
    sign_in_page.try_login("page_object@gmail.com", "password")

    #Проверяем заголовок страницы
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #Закрываем браузер
    sign_in_page.close()