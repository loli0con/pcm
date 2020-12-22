import multiprocessing
import time
from queue import Empty


class Consumer(multiprocessing.Process):
    def __init__(self, consume_function, import_queue, after_consume=None):
        super(Consumer, self).__init__()
        self.consume_function = consume_function
        self.import_queue = import_queue
        self.after_consume = after_consume
        # print("consumer init finish")

    def consume(self):
        while True:
            try:
                product = self.import_queue.get(False)
                if product is None:
                    raise Empty
                if self.consume_function(product):
                    # print(product, "is prime")
                    pass
            except Empty:
                if self.import_queue.sentinel:
                    return
                else:
                    # print(self.name, "is waiting...")
                    time.sleep(0.1)

    def run(self):
        self.consume()
        if self.after_consume:
            self.after_consume()
