import enum

import i18n


class MessageCategory(enum.Enum):
    INFO = 'INFO'
    ERROR = 'ERROR'
    VALIDATION = 'VALIDATION'
    WARNING = 'WARNING'


class Message(object):
    def __init__(self, category=None, target=None, key=None, args=None):
        self.category = category
        self.target = target
        self.key = key
        if args is None:
            args = []
        self.args = args

    def message(self):
        return self.load_message(self.key, self.args)

    @staticmethod
    def load_message(key, args=None):
        locale = 'en'
        message = i18n.t('messages.' + key, locale=locale)
        if args:
            i18n_args = map(lambda arg: i18n.t('messages.' + str(arg), default=arg, locale=locale), args)
            message = message.format(*i18n_args)
        return message
