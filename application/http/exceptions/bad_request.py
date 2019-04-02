from application.http.error import ErrorMapper
from domain.model.common.message import Message


class BadRequest(Exception):

    def __init__(self, messages: [Message], status_code=None):
        Exception.__init__(self)
        default_status_code = 400
        self.messages = messages
        self.status_code = status_code or default_status_code

    def to_json(self):
        errors_dict = [err.to_json for err in ErrorMapper.to_definitions(self.messages)]
        return errors_dict
