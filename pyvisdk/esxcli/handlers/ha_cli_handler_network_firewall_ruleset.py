
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkFirewallRuleset(Base):
    '''
    Commands to list and update firewall ruleset configuration
    '''
    moid = 'ha-cli-handler-network-firewall-ruleset'
    def set(self, rulesetid, allowedall=None, enabled=None):
        '''
        Set firewall ruleset status (allowedAll flag and enabled status).
        :param allowedall: boolean, Set to true to allowed all ip, set to false to use allowed ip list.
        :param enabled: boolean, Set to true to enable ruleset, set to false to disable it.
        :param rulesetid: string, The label of the ruleset.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.ruleset.Set',
                            allowedall=allowedall,
                            enabled=enabled,
                            rulesetid=rulesetid,
                            )
    def list(self, rulesetid=None):
        '''
        List the rulesets in firewall.
        :param rulesetid: string, List configuration for specfic ruleset
        :returns: vim.EsxCLI.network.firewall.ruleset.list.Ruleset[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.ruleset.List',
                            rulesetid=rulesetid,
                            )   