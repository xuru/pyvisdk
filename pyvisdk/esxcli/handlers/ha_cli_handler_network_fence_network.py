
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkFenceNetwork(Base):
    '''
    Commands to list fence network information
    '''
    moid = 'ha-cli-handler-network-fence-network'
    def list(self, vdsname, fenceid=None):
        '''
        Get all fence network info on the vds.
        :param fenceid: long, The fence id used to retrieve fence info.
        :param vdsname: string, The vds name used to retrieve fence info.
        :returns: vim.EsxCLI.network.fence.network.list.FenceNetworkList
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.fence.network.List',
                            fenceid=fenceid,
                            vdsname=vdsname,
                            )   