
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkFenceNetworkPort(Base):
    '''
    Commands to list fence network port information
    '''
    moid = 'ha-cli-handler-network-fence-network-port'
    def list(self, fenceid, vdsname):
        '''
        Get all fence port info on the fence network.
        :param fenceid: long, The fence id used to retrieve fence info.
        :param vdsname: string, The vds name used to retrieve fence info.
        :returns: vim.EsxCLI.network.fence.network.port.list.FencePortList
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.fence.network.port.List',
                            fenceid=fenceid,
                            vdsname=vdsname,
                            )   