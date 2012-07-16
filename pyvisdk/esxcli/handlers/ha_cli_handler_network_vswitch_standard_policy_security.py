
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandardPolicySecurity(Base):
    '''
    Commands to manipulate security policy setting for the given virtual switch.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard-policy-security'
    def set(self, vswitchname, allowforgedtransmits=None, allowmacchange=None, allowpromiscuous=None):
        '''
        Set the security policy for a given virtual switch
        :param allowforgedtransmits: boolean, Allow ports on the virtual switch to send packets with forged source information.
        :param allowmacchange: boolean, Allow ports on the virtual switch to change their MAC address.
        :param allowpromiscuous: boolean, Allow ports on the virtual switch to enter promiscuous mode.
        :param vswitchname: string, The name of the virtual switch to use when setting the switch security policy.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.policy.security.Set',
                            allowforgedtransmits=allowforgedtransmits,
                            allowmacchange=allowmacchange,
                            allowpromiscuous=allowpromiscuous,
                            vswitchname=vswitchname,
                            )
    def get(self, vswitchname):
        '''
        Get the Security Policy governing the given virtual switch.
        :param vswitchname: string, The name of the virtual switch to use when fetching the network security policy.
        :returns: vim.EsxCLI.network.vswitch.standard.policy.security.get.VirtualSwitchSecurityPolicy
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.policy.security.Get',
                            vswitchname=vswitchname,
                            )   