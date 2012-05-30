
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkFence(Base):
    '''
    Commands to list fence information
    '''
    moid = 'ha-cli-handler-network-fence'
    def list(self):
        '''
        Get all fence switch info on the system.
        :returns: vim.EsxCLI.network.fence.list.FenceSwitch[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.fence.List',
                            )   