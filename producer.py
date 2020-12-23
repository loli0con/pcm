import multiprocessing
from abstract import AbstractProducer


class Producer(multiprocessing.Process, AbstractProducer):
    def __init__(self, produce_amount, produce_function, export_queue, after_produce=None):
        super(Producer, self).__init__()
        self.produce_amount = produce_amount
        self.produce_function = produce_function
        self.export_queue = export_queue
        self.after_produce = after_produce
        # print("producer init finish")

    def produce(self):
        for i in range(self.produce_amount):
            _product = self.produce_function()
            self.export_queue.put(_product)

    def run(self):
        self.produce()
        if self.after_produce:
            self.after_produce()
