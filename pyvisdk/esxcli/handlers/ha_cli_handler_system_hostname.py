
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemHostname(Base):
    '''
    Operations pertaining the network name of the ESX host.
    '''
    moid = 'ha-cli-handler-system-hostname'
    def set(self, domain=None, fqdn=None, host=None):
        '''
        This command allows the user to set the hostname, domain name or fully qualified domain name of the ESX host.
        :param domain: string, The domain name to set for the ESX host. This option is mutually exclusive with the --fqdn option.
        :param fqdn: string, Set the fully qualified domain name of the ESX host.
        :param host: string, The host name to set for the ESX host. This name should not contain the DNS domain name of the host and can only contain letters, numbers and '-'. NOTE this is not the fully qualified name, that can be set with the --fqdn option. This option is mutually exclusive with the --fqdn option.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.hostname.Set',
                            domain=domain,
                            fqdn=fqdn,
                            host=host,
                            )
    def get(self):
        '''
        Get the host, domain or fully qualified name of the ESX host.
        :returns: vim.EsxCLI.system.hostname.get.FullyQualifiedHostName
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.hostname.Get',
                            )   