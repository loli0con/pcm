from multiprocessing import Lock, Value
from multiprocessing.queues import Queue
from abstract import AbstractQueue


class ProcessQueue(AbstractQueue):
    def __init__(self, ctx, sentinel=None, **kwargs):
        self._sentinel = sentinel or Value("b", 0)
        maxsize = kwargs.get("maxsize", 0)
        self.queue = Queue(ctx=ctx, maxsize=maxsize)
        self.lock = Lock()

    def put(self, *args, **kwargs):
        self.queue.put(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.queue.get(*args, **kwargs)

    @property
    def sentinel(self):
        with self.lock:
            return self._sentinel.value

    @sentinel.setter
    def sentinel(self, value):
        with self.lock:
            self._sentinel.value = value
