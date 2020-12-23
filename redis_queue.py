import redis
import os
from abstract import AbstractQueue


class RedisQueue(AbstractQueue):
    def __init__(self, host="localhost", port=6379,
                 db=0, password='foobared', decode_responses=True,
                 custom_name="xxy",
                 get_timeout=1,
                 **kwargs):
        self._host = host
        self._port = port
        self._db = db
        self._password = password
        self._decode_responses = decode_responses
        self._custom_name = custom_name

        self._r = redis.Redis(host=self._host, port=self._port,
                              db=self._db, password=self._password,
                              decode_responses=self._decode_responses)
        self._queue_name = custom_name + "_queue"
        self._sentinel_name = custom_name + "_sentinel"
        self._get_timeout = get_timeout

        self.init_redis()

    def init_redis(self):
        self._set_sentinel("False")
        self.clear_queue()

    def put(self, value):
        return self._r.rpush(self._queue_name, value)

    def get(self, block=True):
        timeout = 0 if block else self._get_timeout
        result = self._r.blpop(self._queue_name, timeout)
        if result:
            return int(result[1])
        else:
            return None

    def clear_queue(self):
        self._r.delete(self._queue_name)

    def clear_db(self):
        self._r.flushdb()

    def clear_all(self):
        self._r.flushall()

    def _set_sentinel(self, value):
        self._r.set(self._sentinel_name, value)

    def _get_sentinel(self):
        return self._r.get(self._sentinel_name)

    @property
    def sentinel(self):
        s = self._get_sentinel()
        if s == "True":
            return True
        elif s == "False":
            return False
        else:
            print("可能有bug")
            return s

    @sentinel.setter
    def sentinel(self, value):
        if value is True or value == 1:
            value = "True"
        elif value is False:
            value = "False"
        else:
            print("error!")
            return

        self._set_sentinel(value)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_r']  # manually delete
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._r = redis.Redis(host=self._host, port=self._port,
                              db=self._db, password=self._password,
                              decode_responses=self._decode_responses)  # manually update
        return state


if __name__ == '__main__':
    rq = RedisQueue(host=os.getenv("REDIS_HOST"))
    print(rq.sentinel)
    rq.put(1)
    rq.put(2)
    rq.put(3)
    print(rq.get(False))
    print(rq.get(False))
    print(rq.get(False))
    print(rq.get(False))
    rq.sentinel = True
    print(rq.sentinel)
