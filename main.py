from functools import wraps

import public_function
from consumer import Consumer
from producer import Producer
import time
import os


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


class Main:
    def __init__(self,
                 producer_number=2, consumer_number=4, product_number=100,
                 produce_function=public_function.random_number,
                 consume_function=public_function.is_prime,
                 queue_type="process_queue",
                 queue_argument: dict = None,
                 ):
        self.producer_number = producer_number
        self.consumer_number = consumer_number
        self._produce_function = produce_function
        self._consumer_function = consume_function
        self.product_number = product_number
        self.queue_type = queue_type
        self._queue_argument = queue_argument or {}

        self._shared_queue = None
        self._producers = list()
        self._consumers = list()

    def create_queue(self):
        self._shared_queue = public_function.get_queue(self.queue_type, **self._queue_argument)

    def create_producer(self):
        leave_number = self.product_number
        do_every_time = self.product_number // self.producer_number

        for i in range(self.producer_number - 1):
            p = Producer(produce_amount=do_every_time,
                         produce_function=self._produce_function,
                         export_queue=self._shared_queue)
            leave_number -= do_every_time
            self._producers.append(p)

        p = Producer(produce_amount=leave_number,
                     produce_function=self._produce_function,
                     export_queue=self._shared_queue)
        self._producers.append(p)

    def create_consumer(self):
        for i in range(self.consumer_number):
            c = Consumer(consume_function=self._consumer_function,
                         import_queue=self._shared_queue)
            self._consumers.append(c)

    def start_producer(self):
        for p in self._producers:
            p.start()

    def start_consumer(self):
        for c in self._consumers:
            c.start()

    def wait_produce(self):
        for p in self._producers:
            p.join()
        self._shared_queue.sentinel = 1

    def wait_consumer(self):
        for c in self._consumers:
            c.join()

    @time_cost
    def run(self):
        self.create_queue()
        self.create_producer()
        self.create_consumer()

        self.start_producer()
        self.start_consumer()

        self.wait_produce()
        self.wait_consumer()


if __name__ == '__main__':
    m1 = Main(queue_type="redis_queue",
              queue_argument={"host": os.getenv("REDIS_HOST")},
              product_number=200)
    m1.run()

    m2 = Main(queue_type="process_queue",
              product_number=200)
    m2.run()
