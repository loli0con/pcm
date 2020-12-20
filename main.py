from functools import wraps

import public_function
from consumer import Consumer
from producer import Producer
from my_queue import MyQueue
import multiprocessing
import time
from multiprocessing import get_context


def time_cost(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        s = time.time()
        result = fun(*args, **kwargs)
        e = time.time()
        print(str(kwargs.get("p_n")) + "生产者,生产" +
              str(kwargs.get("n")) + "个产品,由" +
              str(kwargs.get("c_n")) + "个消费者处理"
              , end=",")
        print("耗时为" + str(e - s) + "秒")
        return result

    return wrapper


@time_cost
def main(p_n=2, c_n=4, n=1_000_000):
    # 初始化进程队列
    shared_queue = MyQueue(ctx=get_context())

    # 初始化生产者
    producers = list()
    for i in range(p_n):
        p = Producer(n // p_n, public_function.random_number, shared_queue)
        producers.append(p)

    # 初始化消费者
    consumers = list()
    for i in range(c_n):
        c = Consumer(public_function.is_prime, shared_queue)
        consumers.append(c)

    # 启动所有进程
    for p in (producers + consumers):
        p.start()

    # 等待生产完成
    for p in producers:
        p.join()

    # 标注生成过程已经完成
    shared_queue.sentinel = 1

    # 等待消费完成
    for c in consumers:
        c.join()


if __name__ == '__main__':
    main(p_n=1, c_n=1, n=1_000_000)
    main(p_n=1, c_n=2, n=1_000_000)
    main(p_n=2, c_n=4, n=1_000_000)
