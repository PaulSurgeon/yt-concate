from abc import ABCMeta, abstractmethod


class Step(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):
    pass
