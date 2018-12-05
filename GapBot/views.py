from django.shortcuts import render
import json
import redis
from .redis_config import RedisConfig


def dispatcher(request, token=None):
    update_dict = {token: request.body}  # todo: token must be the bot token not the unique url token
    r = redis.Redis(host=RedisConfig.host,
                    port=RedisConfig.port,
                    db=RedisConfig.db)
    r.lpush(RedisConfig.update_queue, json.dumps(update_dict))
