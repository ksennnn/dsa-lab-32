import requests, random

URL = 'http://127.0.0.1:5000/number'

# GET
param = random.randint(1, 10)
get_result = requests.get(URL, params={'param': param}).json()
print('GET запрос:', get_result)

# POST
json_param = random.randint(1, 10)
headers = {'Content-Type': 'application/json'} 
post_result = requests.post(URL, json={'jsonParam': json_param}, headers=headers).json()
print('POST запрос:', post_result)

# DELETE
delete_result = requests.delete(URL).json()
print('DELETE запрос:', delete_result)

# Функция для выполнения операции
def calc(x, y, operation):
    if operation == "sum":
        return x + y
    elif operation == "sub":
        return x - y
    elif operation == "mul":
        return x * y
    elif operation == "div":
        if y == 0:
            return "Делить на ноль нельзя"
        return x / y

# Итоговый результат трех запросов
result = get_result['result']
print(f"Начальное значение (GET): {result}")

result = calc(result, post_result['result'], post_result['operation'])
print(f"После POST ({post_result['operation']} {post_result['result']}): {result}")

result = calc(result, delete_result['result'], delete_result['operation'])
print(f"После DELETE ({delete_result['operation']} {delete_result['result']}): {result}")

print("Итоговый результат:", int(result))
