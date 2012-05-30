
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIpDnsSearch(Base):
    '''
    Operations pertaining to DNS search domain configuration.
    '''
    moid = 'ha-cli-handler-network-ip-dns-search'
    def add(self, domain):
        '''
        Add a search domain to the list of domains to be searched when trying to resolve an host name on the ESXi host.
        :param domain: string, The string name of a domain to add to the list of search domains.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.dns.search.Add',
                            domain=domain,
                            )
    def list(self):
        '''
        List the search domains currently configured on the ESXi host in the order in which they will be used when searching.
        :returns: vim.EsxCLI.network.ip.dns.search.list.DNSSearchList
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.dns.search.List',
                            )
    def remove(self, domain):
        '''
        Remove a search domain from the list of domains to be searched when trying to resolve an host name on the ESXi host.
        :param domain: string, The string name of a domain to remove from the list of search domains.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.dns.search.Remove',
                            domain=domain,
                            )   