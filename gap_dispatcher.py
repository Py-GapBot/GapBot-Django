import redis
import json
from GapBot.redis_config import RedisConfig
from handlers import Handler


class Dispatcher:
    def __init__(self):
        self.bot_token, self.last_update_body = self.get_update_data(self.get_last_update())
        self.redis_connection = redis.Redis(host=RedisConfig.host,
                                            port=RedisConfig.port,
                                            db=RedisConfig.db)
        self.handler = None

    def get_last_update(self):
        return self.redis_connection.brpop(RedisConfig.update_queue, 0)

    def get_update_data(self, value):
        update = json.loads(value)
        for token, received_data in update.items():
            return token, received_data

    def run(self):
        self.handler = Handler(self.last_update_body['type'],
                               self.last_update_body['chat_id'],
                               self.last_update_body['data'],
                               self.bot_token,
                               self.last_update_body)
        self.handler.run()
