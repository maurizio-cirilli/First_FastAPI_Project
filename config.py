import redis

# HOST = ''
# PORT = 17976
# PASSWORD = ''

HOST = ''
PORT = 17976
PASSWORD = ''


class Config:
    def __init__(self):
        self.redis_conf = redis.Redis(host=HOST, port=PORT, password=PASSWORD)
    def get_redis_config(self):
        return self.redis_conf