
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkFenceNetworkBte(Base):
    '''
    Commands to list fence network bte information
    '''
    moid = 'ha-cli-handler-network-fence-network-bte'
    def list(self, fenceid, vdsname):
        '''
        Get all fence network bridge table entries information
        :param fenceid: long, The fence id used to retrieve fence info.
        :param vdsname: string, The vds name used to retrieve fence info.
        :returns: vim.EsxCLI.network.fence.network.bte.list.FenceBteList
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.fence.network.bte.List',
                            fenceid=fenceid,
                            vdsname=vdsname,
                            )   