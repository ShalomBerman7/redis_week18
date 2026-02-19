from mongo_connection import collection


def alerts_by_border_and_priority():
    pipeline = [
        {"$group": {
            "_id": {"border": "$border", "priority": "$priority"},
            "count": {"$sum": 1}
        }
        },
        {"$project": {
            "_id": 0,
            "border": "$_id.border",
            "priority": "$_id.priority",
            "count": 1
        }
        }
    ]
    return collection.aggregate(pipeline)


def top_urgent_zones():
    pipeline = [
        {"$match": {"priority": "URGENT"}},
        {
            "$group": {
                "_id": "$zone",
                "urgent_count": {"$sum": 1}
            }
        },
        {"$sort": {"urgent_count": -1}},
        {"$limit": 5},
        {"$project": {"_id": 0, "zone": "$_id", "urgent_count": 1}}
    ]
    return collection.aggregate(pipeline)


def distance_distribution():
    pipeline = [
        {
            "$bucket": {
                "groupBy": "$distance_from_fence_m",
                "boundaries": [0, 301, 801, 1501],
                "default": "very far",
                "output": {"count": {"$sum": 1}}
            }
        }
    ]
    return collection.aggregate(pipeline)


def low_visibility_high_activity():
    pass


def hot_zones():
    pass

print(collection.find_one())