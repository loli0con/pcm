import math
import random
from process_queue import ProcessQueue
from redis_queue import RedisQueue
from multiprocessing import get_context
import time
from functools import wraps


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


def time_cost(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        s = time.time()
        result = fun(*args, **kwargs)
        e = time.time()
        print("使用" + str(args[0].queue_type) + "," +
              str(args[0].producer_number) + "个生产者,生产" +
              str(args[0].product_number) + "个产品,由" +
              str(args[0].consumer_number) + "个消费者处理"
              , end=",")
        print("耗时为" + str(e - s) + "秒")
        return result

    return wrapper
