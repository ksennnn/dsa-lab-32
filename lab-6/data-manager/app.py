from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Настройки подключения к PostgreSQL
DB_CONFIG = {
    'dbname': 'currencies_db',   
    'user': 'postgres',          
    'password': 'shjm221b',      
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/convert', methods=['GET'])
def convert():
    """Конвертация суммы по курсу выбранной валюты. Пример запроса: /convert?currency=USD&amount=100"""
    
    # Получаем параметры из URL
    currency_name = request.args.get('currency')
    amount = float(request.args.get('amount'))

    conn = get_db_connection()
    cur = conn.cursor()

    # Получаем курс валюты
    cur.execute('SELECT rate FROM currencies WHERE currency_name = %s', (currency_name,))
    row = cur.fetchone()
    
    # Если валюта не найдена
    if not row:
        cur.close()
        conn.close()
        return jsonify({'error': 'Currency not found'}), 404

    # Курс валюты
    rate = float(row[0])
    # Выполняем конвертацию
    converted = amount * rate
    # Закрываем соединение
    cur.close()
    conn.close()
    
    # Возвращаем результат
    return jsonify({
        'currency': currency_name,
        'amount': amount,
        'rate': rate,
        'converted_amount': round(converted, 2)
    }), 200

@app.route('/currencies', methods=['GET'])
def get_currencies():
    """Возвращает список всех валют из таблицы currencies."""
    conn = get_db_connection()
    cur = conn.cursor()

    # Получаем все валюты
    cur.execute('SELECT currency_name, rate FROM currencies')
    rows = cur.fetchall()

    currencies_list = [
        {
            'currency_name': row[0],
            'rate': float(row[1])
        }
        for row in rows
    ]
    # Закрываем соединение
    cur.close()
    conn.close()
    # Возвращаем JSON-ответ
    return jsonify({
        'currencies': currencies_list
    }), 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)