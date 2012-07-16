
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIpDnsServer(Base):
    '''
    Operations pertaining to DNS server configuration.
    '''
    moid = 'ha-cli-handler-network-ip-dns-server'
    def add(self, server):
        '''
        Add a new DNS server to the end of the list of DNS servers to use for this ESXi host.
        :param server: string, The IP address (v4 or v6) of the DNS server to add to the DNS server list.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.dns.server.Add',
                            server=server,
                            )
    def list(self):
        '''
        Print a list of the DNS server currently configured on the system in the order in which they will be used.
        :returns: vim.EsxCLI.network.ip.dns.server.list.NameServerList
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.dns.server.List',
                            )
    def remove(self, server, all=None):
        '''
        Remove a DNS server from the list of DNS servers to use for this ESXi host.
        :param all: boolean,  
        :param server: string,  
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.dns.server.Remove',
                            all=all,
                            server=server,
                            )   