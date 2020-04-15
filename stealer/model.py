from enum import unique, Enum


class Result:

    def __init__(self, success: bool, data):
        self._success = success
        self._data = data

    def is_success(self):
        return self._success

    def get_data(self):
        return self._data

    @property
    def ref(self):
        return self._ref

    @ref.setter
    def ref(self, value):
        self._ref = value

    @staticmethod
    def success(data):
        return Result(True, data=data)

    @staticmethod
    def failed(msg):
        return Result(False, data=msg)

    @staticmethod
    def error(err: Exception):
        return Result(False, data=str(err))


@unique
class ErrorResult(Result, Enum):
    URL_NOT_FOUNT = False, 'url not found.'
    VIDEO_ADDRESS_NOT_FOUNT = False, 'video address not found.'

    def __init__(self, *value):
        super().__init__(success=value[0], data=value[1])  # init Song
        # super(Enum, self).__init__()

