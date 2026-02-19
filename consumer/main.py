from redis_connection import r
from mongo_connection import collection
import datetime


def get_from_redis():
    result = r.get('queue_urgent')
    if result is not None:
        item = result.decode('utf-8')
        return item
    if result is None:
        result = r.get('queue_normal')
        if result is not None:
            item = result.decode('utf-8')
            return item
        else:
            return
    else:
        return


def add_insert_time(item):
    item['time_insertion'] = datetime.datetime.now()
    return item


def insert_to_mongo():
    while True:
        item = get_from_redis()
        if item is None:
            continue
        item = add_insert_time(item)
        collection.insert_one(item)


if __name__ == '__main__':
    insert_to_mongo()
