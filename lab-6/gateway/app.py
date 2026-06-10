from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Адреса микросервисов
CURRENCY_MANAGER_URL = "http://127.0.0.1:5001"
DATA_MANAGER_URL = "http://127.0.0.1:5002"

@app.route('/')
def index():
    """Главная страница приложения.
    Получает список валют через data-manager
    и отображает HTML-шаблон."""
    try:
        # Отправляем запрос к data-manager
        resp = requests.get(f"{DATA_MANAGER_URL}/currencies")
        # Получаем список валют из JSON
        currencies_data = resp.json().get('currencies', [])
    except:
        # Если сервис недоступен
        currencies_data = []
    
    # Отображаем HTML-страницу
    return render_template('index.html', currencies=currencies_data)

@app.route('/load', methods=['POST'])
def load_currency():
    """Прокси-запрос на currency-manager (/load).
    Получает данные из HTML-формы
    и отправляет JSON в микросервис."""
    
    # Данные формы
    data = request.form
    # Отправка POST-запроса в currency-manager
    resp = requests.post(
        f"{CURRENCY_MANAGER_URL}/load",
        json={
            'currency_name': data.get('currency_name'),
            'rate': data.get('rate')
        }
    )
    return resp.text, resp.status_code

@app.route('/update_currency', methods=['POST'])
def update_currency():
    """Прокси-запрос для обновления курса валюты."""
    data = request.form

    # Отправка запроса в currency-manager
    resp = requests.post(
        f"{CURRENCY_MANAGER_URL}/update_currency",
        json={
            'currency_name': data.get('currency_name'),
            'rate': data.get('rate')
        }
    )
    return resp.text, resp.status_code

@app.route('/delete', methods=['POST'])
def delete_currency():
    """Прокси-запрос для удаления валюты."""
    data = request.form

    # Отправляем запрос на удаление
    resp = requests.post(f"{CURRENCY_MANAGER_URL}/delete", json={
        'currency_name': data.get('currency_name')
    })
    return resp.text, resp.status_code

@app.route('/convert', methods=['POST'])
def convert():
    """Прокси-запрос на data-manager (/convert).
    Принимает данные из формы,
    затем отправляет GET-запрос
    с параметрами currency и amount."""
    if request.method == 'POST':
        # Получаем данные формы
        currency = request.form.get('currency')
        amount = request.form.get('amount')
        # Запрос к data-manager
        resp = requests.get(f"{DATA_MANAGER_URL}/convert", params={
            'currency': currency,
            'amount': amount
        })
        return resp.text, resp.status_code
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)