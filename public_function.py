import math
import random
from process_queue import ProcessQueue
from redis_queue import RedisQueue
from multiprocessing import get_context


def is_prime(num: int):
    if num == 2 or num == 3:
        return True
    if num % 6 != 1 and num % 6 != 5:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def random_number():
    return random.randint(2_000_000_000, 10_000_000_000)


def get_queue(queue_type="process_queue", **kwargs):
    _q = None
    if queue_type == "process_queue":
        kwargs.setdefault("ctx", get_context())
        _q = ProcessQueue(**kwargs)
    elif queue_type == "redis_queue":
        _q = RedisQueue(**kwargs)
    else:
        raise BaseException("do not support this " + queue_type)

    return _q
