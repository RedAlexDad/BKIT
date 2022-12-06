import json


def write_data(data, title='D:\Python\BKIT\calculate\data'):
    with open(f"{title}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def load_data_all(title="D:\Python\BKIT\calculate\data"):
    with open(f"{title}.json", "r") as file:
        data = json.load(file)
    return data


def merge_data(data_json, id_user='id_user', title="D:\Python\BKIT\calculate\data"):
    # Если файл существует и не пустой
    try:
        with open(f"{title}.json", encoding="utf-8") as file:
            data = json.load(file)
            temp = data[id_user]
            for info_data in data_json[id_user]:
                y = {
                    'id': info_data['id'],
                    'value': info_data['value'],
                    'result': info_data['result']
                }
            temp.append(y)
        write_data(data)
    # Если файл не существует
    except:
        write_data(data_json)

def load_data_for_id_user(id_user, title="D:\Python\BKIT\calculate\data"):
    with open(f"{title}.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        temp = data[id_user]
        for info_data in data[id_user]:
            y = {
                'id': info_data['id'],
                'value': info_data['value'],
                'result': info_data['result']
            }
        temp.append(y)
    return temp

def find_values(id_user, json_data):
    results = []
    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id_user])
        except KeyError:
            pass
        return a_dict

    json.loads(json_data, object_hook=_decode_dict) # Return value ignored.
    return results