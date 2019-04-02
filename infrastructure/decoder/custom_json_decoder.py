import datetime

from flask.json import JSONEncoder

from application.http.error import Error


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

            if isinstance(obj, datetime.timedelta):
                return str(obj)

            if isinstance(obj, Error):
                return obj.to_json

            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
