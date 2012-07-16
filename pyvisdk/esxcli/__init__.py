
from .base import Base
from .generator import Generator

class EsxCLI(Base):
    def __init__(self, client, host):
        super(EsxCLI, self).__init__(client, host)

    def _get_init_args(self):
        return self._client, self._host

    def get(self, namespace):
        from .handlers import import_handler
        return import_handler(''.join([item.capitalize() for item in namespace.split('.')]))(*self._get_init_args())
