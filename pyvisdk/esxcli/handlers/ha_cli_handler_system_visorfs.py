
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemVisorfs(Base):
    '''
    Operations pertaining to the visorfs memory filesytem.
    '''
    moid = 'ha-cli-handler-system-visorfs'
    def get(self):
        '''
        Obtain status information on the memory filesystem as a whole.
        :returns: vim.EsxCLI.system.visorfs.get.VisorfsStatus
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.visorfs.Get',
                            )   