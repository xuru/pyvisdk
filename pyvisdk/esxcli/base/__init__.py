class Base(object):
    def __init__(self, client, host):
        super(Base, self).__init__()
        self._client = client
        self._host = host
