
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkFirewall(Base):
    '''
    A set of commands for firewall related operations
    '''
    moid = 'ha-cli-handler-network-firewall'
    def load(self):
        '''
        Load firewall module and rulesets configuration.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.Load',
                            )
    def unload(self):
        '''
        Allow unload firewall module.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.Unload',
                            )
    def set(self, defaultaction=None, enabled=None):
        '''
        Set firewall enabled status and default action.
        :param defaultaction: boolean, Set to true to set defaultaction PASS, set to false to DROP.
        :param enabled: boolean, Set to true to enable the firewall, set to false to disable the firewall.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.Set',
                            defaultaction=defaultaction,
                            enabled=enabled,
                            )
    def refresh(self):
        '''
        Load ruleset configuration for firewall.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.Refresh',
                            )
    def get(self):
        '''
        Get the firewall status.
        :returns: vim.EsxCLI.network.firewall.get.Firewall
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.Get',
                            )   