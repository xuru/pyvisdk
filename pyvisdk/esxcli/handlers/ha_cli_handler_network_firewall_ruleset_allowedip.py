
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkFirewallRulesetAllowedip(Base):
    '''
    Commands to list and add/remove allowedip on ruleset
    '''
    moid = 'ha-cli-handler-network-firewall-ruleset-allowedip'
    def add(self, ipaddress, rulesetid):
        '''
        Add allowed ip address/range to the ruleset ruleset.
        :param ipaddress: string, Allowed ip address/range for the ruleset.
        :param rulesetid: string, The label of the ruleset.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.ruleset.allowedip.Add',
                            ipaddress=ipaddress,
                            rulesetid=rulesetid,
                            )
    def list(self, rulesetid=None):
        '''
        list allowed ip addresses for rulesets.
        :param rulesetid: string, The label of the ruleset.
        :returns: vim.EsxCLI.network.firewall.ruleset.allowedip.list.FirewallRulesetAllowedip[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.ruleset.allowedip.List',
                            rulesetid=rulesetid,
                            )
    def remove(self, ipaddress, rulesetid):
        '''
        Remove allowed ip address/range from the ruleset.
        :param ipaddress: string, Allowed ip address/range for the ruleset.
        :param rulesetid: string, The label of the ruleset.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.ruleset.allowedip.Remove',
                            ipaddress=ipaddress,
                            rulesetid=rulesetid,
                            )   