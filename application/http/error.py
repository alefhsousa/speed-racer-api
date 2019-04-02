
class Error(object):

    def __init__(self, type: str, key: str, message: str):
        self.type = type
        self.key = key
        self.message = message

    @property
    def to_json(self):
        return self.__dict__


class ErrorMapper(object):
    @staticmethod
    def to_definition(message):
        return Error(type=message.category.name, key=message.key, message=message.message())

    @staticmethod
    def to_definitions(messages):
        return list(map(ErrorMapper.to_definition, messages))
