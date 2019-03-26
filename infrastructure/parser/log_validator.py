from abc import abstractmethod, ABC

from infrastructure.common.either import Either


class LogValidator(ABC):

    @abstractmethod
    def validate(self, line_content, line_number) -> Either:
        pass
