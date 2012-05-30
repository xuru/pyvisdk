
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIpConnection(Base):
    '''
    List active tcpip connections
    '''
    moid = 'ha-cli-handler-network-ip-connection'
    def list(self, type=None):
        '''
        List active TCP/IP connections
        :param type: string, Connection type :  [ip, tcp, udp, all]
        :returns: vim.EsxCLI.network.ip.connection.list.IpConnection[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.connection.List',
                            type=type,
                            )   