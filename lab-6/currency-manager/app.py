from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Конфигурация подключения к PostgreSQL
DB_CONFIG = {
    'dbname': 'currencies_db',   
    'user': 'postgres',         
    'password': 'shjm221b',    
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    """Создаёт и возвращает подключение к PostgreSQL."""
    return psycopg2.connect(**DB_CONFIG)
    

@app.route('/load', methods=['POST'])
def load_currency():
    """Добавление новой валюты в таблицу currencies. Ожидает JSON: {"currency_name": "USD", "rate": 90.5}"""

    # Получаем JSON-данные из запроса
    data = request.get_json()

    # Извлекаем название валюты и курс
    currency_name = data.get('currency_name')
    rate = data.get('rate')

    conn = get_db_connection()
    cur = conn.cursor()

    # Проверяем, существует ли уже такая валюта
    cur.execute('SELECT id FROM currencies WHERE currency_name = %s', (currency_name,))
    # Если валюта уже есть — возвращаем ошибку
    if cur.fetchone():
        cur.close()
        conn.close()
        return jsonify({'error': 'The currency already exists'}), 409

    cur.execute(
        'INSERT INTO currencies (currency_name, rate) VALUES (%s, %s)',
        (currency_name, rate)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Currency added successfully'}), 200

@app.route('/update_currency', methods=['POST'])
def update_currency():
    """Обновление курса существующей валюты. Ожидает JSON: {"currency_name": "USD", "rate": 95.2}"""
    data = request.get_json()
    currency_name = data.get('currency_name')
    new_rate = data.get('rate')

    conn = get_db_connection()
    cur = conn.cursor()

    # Проверяем наличие валюты
    cur.execute('SELECT id FROM currencies WHERE currency_name = %s', (currency_name,))
    # Если валюты нет — ошибка 404
    if not cur.fetchone():
        cur.close()
        conn.close()
        return jsonify({'error': 'Currency not found'}), 404

    # Обновляем курс валюты
    cur.execute(
        'UPDATE currencies SET rate = %s WHERE currency_name = %s', (new_rate, currency_name)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'The exchange rate has been updated'}), 200

@app.route('/delete', methods=['POST'])
def delete_currency():
    """ Удаление валюты по её названию. Ожидает JSON: {"currency_name": "USD"}"""
    data = request.get_json()
    currency_name = data.get('currency_name')

    conn = get_db_connection()
    cur = conn.cursor()
    # Проверяем существование валюты
    cur.execute('SELECT id FROM currencies WHERE currency_name = %s', (currency_name,))
    # Если валюты нет — ошибка
    if not cur.fetchone():
        cur.close()
        conn.close()
        return jsonify({'error': 'Currency not found'}), 404

    cur.execute('DELETE FROM currencies WHERE currency_name = %s', (currency_name,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Currency removed'}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)