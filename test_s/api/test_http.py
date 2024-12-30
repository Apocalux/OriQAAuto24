#pytest -m http -s - запуск теста с текущей меткой, -s выведет в консоль сообщение со страницы
import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    
    body = r.json()
    headers = r.headers

    
    #print(f"Response Body is {r.json()}") - вывод теда респонса
    #print(f"Responce Status code is {r.status_code}") - просто вывод статус кода
    #print(f"Responce Headers are {r.headers}")
    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200 #проверяем, что статус код этого реквеста - 200
    assert headers['Server'] == 'github.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404