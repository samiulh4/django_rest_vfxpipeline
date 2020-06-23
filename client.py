import requests

URL = 'http://127.0.0.1:8000'

def get_token():
    url =f'{URL}/api/auth/'
    response = requests.post(url, data={'username' : 'rajiv', 'password' : 'vfxpipeline'})
    return response.json()

def get_data():
    url = f'{URL}/api/users_list/'
    token = get_token()
    header = {'Authorization' : f'Token {get_token()}'}
    response = requests.get(url, headers=header)
    emp_data = response.json()
    for e in emp_data:
        print(e)

def create_new(count):
    url = f'{URL}/api/users_list/'
    token = get_token()
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "id": 2,
        "employee_id": f"HQ000{count}",
        "name": "SHABITH BIN TUGRIL",
        "ranking": 5.0,
        "age": 5
    }
    response = requests.post(url, data=data, headers=header)
    print(response.text)

def edit_date(employee_id):
    url = f'{URL}/api/users_list/{employee_id}/'
    token = get_token()
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "name": "MALIHA SULTANA",
        "ranking": 2.1,
        "age": 19
    }
    response = requests.put(url, data=data, headers=header)
    print(response.text, response.status_code)

def delete_date(employee_id):
    url = f'{URL}/api/users_list/{employee_id}/'
    token = get_token()
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.delete(url, headers=header)
    print(response.status_code)

# for e in range(22):
#     if e > 4:
#         delete_date(e)

#create_new(3)
edit_date(25)
get_data()