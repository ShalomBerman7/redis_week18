from redis_connection import r
from priority_logic import read_json, add_priority


def push_to_redis():
    data = add_priority(read_json())

    for item in data:
        if item['priority'] == 'URGENT':
            key = 'queue_urgent'
            value = item
        else:
            key = 'queue_normal'
            value = item
        r.set(name=key, value=value, ex=600)


if __name__ == '__main__':
    push_to_redis()
