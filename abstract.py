from abc import ABCMeta, abstractmethod


class AbstractProducer(metaclass=ABCMeta):
    @abstractmethod
    def produce(self):
        pass


class AbstractConsumer(metaclass=ABCMeta):
    @abstractmethod
    def consume(self):
        pass


class AbstractQueue(metaclass=ABCMeta):
    @abstractmethod
    def put(self, value):
        pass

    @abstractmethod
    def get(self):
        pass

    @property
    @abstractmethod
    def sentinel(self):
        pass

    @sentinel.setter
    @abstractmethod
    def sentinel(self, value):
        pass
