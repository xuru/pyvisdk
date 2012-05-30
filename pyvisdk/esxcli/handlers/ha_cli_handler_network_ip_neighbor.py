
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIpNeighbor(Base):
    '''
    Operations that can be performed on arp tables
    '''
    moid = 'ha-cli-handler-network-ip-neighbor'
    def list(self, version=None):
        '''
        List ARP table entries
        :param version: string, IP version :  [4, 6, all]
        :returns: vim.EsxCLI.network.ip.neighbor.list.NetworkNeighbor[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.neighbor.List',
                            version=version,
                            )   