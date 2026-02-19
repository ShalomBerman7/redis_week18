import json


def read_json():
    path = '../data/border_alerts.json'
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def add_priority(data):
    for i in data:
        if (i['weapons_count'] > 0 or
                i['distance_from_fence_m'] <= 50 or
                i['people_count'] >= 8 or
                i['vehicle_type'] == 'truck'):
            i['priority'] = 'URGENT'

        elif i['distance_from_fence_m'] <= 150 and i['people_count'] >= 4:
            i['priority'] = 'URGENT'

        elif i['vehicle_type'] == 'geep' and i['people_count'] >= 3:
            i['priority'] = 'URGENT'

        else:
            i['priority'] = 'NORMAL'

    return data
