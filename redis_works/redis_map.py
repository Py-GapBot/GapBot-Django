import redis
import json
from .redis_config import RedisConfig


class RedisMap:
    def __init__(self, token):
        self.redis_connection = redis.Redis(host=RedisConfig.host,
                                            port=RedisConfig.port,
                                            db=RedisConfig.db)
        self.token = token

    def get_updates(self):
        raw_updates = self.redis_connection.lrange('updates:'+self.token, 0, -1)
        update_id_list = [x.decode('utf-8') for x in raw_updates]
        updates = [self.redis_connection.hget('bot:'+self.token, trans_id) for trans_id in update_id_list]
