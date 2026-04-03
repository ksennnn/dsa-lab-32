from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/number/', methods=['GET'])
def random_number():
    param = request.args.get('param')    
    if param is None:
        return jsonify({'error': 'Параметр "param" не передан'}), 400
    try:
        param = int(param)
    except ValueError:
        return jsonify({'error': 'Параметр "param" должен быть числом'}), 400
    
    random_num = random.randint(1, 100)
    
    result = param * random_num

    return jsonify({
        'original_param': param,
        'random_num': random_num,
        'result': result
    })

@app.route('/number/', methods=['POST'])
def post_number():
    data = request.json
    
    if 'jsonParam' not in data:
        return jsonify({'error': 'Поле jsonParam не передано'}), 400
    
    try:
        json_param = int(data['jsonParam'])
    except (TypeError, ValueError):
        return jsonify({'error': 'jsonParam должен быть числом'}), 400
    
    random_num = random.randint(1, 100)

    operation = random.choice(['sum', 'sub', 'mul', 'div'])
    if operation == 'sum':
        result = random_num + json_param
    elif operation == 'sub':
        result = random_num - json_param
    elif operation == 'mul':
        result = random_num * json_param
    else:
        if json_param == 0:
            return jsonify({'error': 'Не делим на ноль!'}), 400
        result = random_num / json_param

    return jsonify({
        'result': result,
        'operation': operation,
        'random_number': random_num
    })

@app.route('/number/', methods=['DELETE'])
def delete_num():
    number = random.randint(1, 100)
    number2 = random.randint(1, 100)

    operation = random.choice(['sum', 'sub', 'mul', 'div'])
    if operation == 'sum':
        result = number + number2
    elif operation == 'sub':
        result = number - number2
    elif operation == 'mul':
        result = number * number2
    else:
        if number2 == 0:
            return jsonify({'error': 'делить на ноль нельзя!'}), 400
        result = number / number2
    return jsonify({
        'first_number': number,
        'second_number': number2,
        'operation': operation,
        'result': result,
    })

if __name__ == '__main__':
    app.run(debug=True)
