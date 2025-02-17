import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By #Дает возмонжость искать элементы на странице
import time #Задержка при выполнении тестов


@pytest.mark.ui
def test_check_incorrect_username():
    # Создание объекта для управления браузером
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

    #Открываем страницу https://github.com/login
    driver.get("https://github.com/login")

    #Находим поле, в которое будем вводить invalid data
    login_elem = driver.find_element(By.ID, "login_field") #ID поля с devtools
    pass_elem = driver.find_element(By.ID, "password")

    #Вводим invalid data
    login_elem.send_keys("lalao@somegmail.com")
    # time.sleep(3) #3s delay

    pass_elem.send_keys("wrong")

    #находим кнопку sing in
    btn_elem = driver.find_element(By.NAME, "commit")

    #Эмулируем нажатие лкм
    btn_elem.click()

    #Проверяем заголовок страницы
    assert driver.title == "Sign in to GitHub · GitHub"

    #Закрываем браузер
    driver.close()