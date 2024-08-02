class ResponseWrapper:
    def __init__(self, ok, status_code, data, text, cookies):
        self._ok = ok
        self._status_code = status_code
        self._data = data
        self._text = text
        self._cookies = cookies

    @property
    def ok(self):
        return self._ok

    @property
    def status_code(self):
        return self._status_code

    @property
    def data(self):
        return self._data

    @property
    def text(self):
        return self._text

    @property
    def cookies(self):
        return self._cookies
