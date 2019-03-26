from abc import ABC, abstractmethod


class LogMapper(ABC):

    @abstractmethod
    def to_model(self, line_content):
        pass
