
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkFirewallRulesetRule(Base):
    '''
    Commands to list rules in the ruleset
    '''
    moid = 'ha-cli-handler-network-firewall-ruleset-rule'
    def list(self, rulesetid=None):
        '''
        List the rules of each ruleset in firewall.
        :param rulesetid: string, List rules for specfic ruleset
        :returns: vim.EsxCLI.network.firewall.ruleset.rule.list.FirewallPortRule[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.firewall.ruleset.rule.List',
                            rulesetid=rulesetid,
                            )   