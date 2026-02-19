from redis import Redis
import os

host = os.getenv('REDIS_HOST', 'localhost')
r = Redis(host=host, port=6379)
