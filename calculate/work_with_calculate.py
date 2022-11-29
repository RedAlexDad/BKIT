import random

from calculate.json_function import write_data, load_data, merge_data
from calculate.calculate_arifmetic import calculate


def generate_value(id_user='id_user'):
    arifmetic = ['+', '-', '/', '*']

    af = arifmetic[random.randint(0, 3)]
    gen_id = random.randint(0, 100000)
    v1 = random.randint(0, 1000)
    v2 = random.randint(0, 1000)
    result = calculate(str(v1) + ' ' + str(af) + ' ' + str(v2))

    data = {
        str(id_user): [
            {
                "id": gen_id,
                "value": v1,
                "result": result
            }
        ]
    }

    merge_data(data, id_user)

def get_info():
    try:
        data = load_data()
        return data
    except:
        return 'Файл отсутствует'


'''
def change_info_of_id(id_search, new_value):
    data = load_data()
    for id_user in data:
        for data_user_of_id in data[id_user]:
            if(id_search == data_user_of_id['id']):
                data['value'] = new_value
                data['result'] = calculate(new_value)
                break
                
change_info_of_id(6602, '20 + 20')
'''
'''
data = get_info()
for i in data:
    for j in data[i]:
        id = j['id']
        value = j['value']
        result = j['result']
        print_info = f'id: {id}\n{value} = {result}'
        print(print_info, end='\n\n')
'''