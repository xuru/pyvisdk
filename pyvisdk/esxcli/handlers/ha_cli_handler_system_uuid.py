
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemUuid(Base):
    '''
    Get the system UUID
    '''
    moid = 'ha-cli-handler-system-uuid'
    def get(self):
        '''
        Get the system UUID.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.uuid.Get',
                            )   