
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandardPortgroupPolicySecurity(Base):
    '''
    Commands to manipulate security policy setting for the given portgroup.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard-portgroup-policy-security'
    def set(self, portgroupname, allowforgedtransmits=None, allowmacchange=None, allowpromiscuous=None, usevswitch=None):
        '''
        Set the security policy for a given port group
        :param allowforgedtransmits: boolean, Allow ports on the virtual switch to send packets with forged source information.
        :param allowmacchange: boolean, Allow ports on the virtual switch to change their MAC address.
        :param allowpromiscuous: boolean, Allow ports on the virtual switch to enter promiscuous mode.
        :param portgroupname: string, The name of the port group to set security policy for.
        :param usevswitch: boolean, Reset all values for this policy to use parent virtual switch's settings instead of overriding the settings for the port group.   Using this in conjunction with other settings will first reset all of the fields to use the virtual switch setting and then apply the other options after the reset.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.policy.security.Set',
                            allowforgedtransmits=allowforgedtransmits,
                            allowmacchange=allowmacchange,
                            allowpromiscuous=allowpromiscuous,
                            portgroupname=portgroupname,
                            usevswitch=usevswitch,
                            )
    def get(self, portgroupname):
        '''
        Get the Security Policy governing the given port group. 
        :param portgroupname: string, The name of the port group to use when fetching the network security policy.
        :returns: vim.EsxCLI.network.vswitch.standard.portgroup.policy.security.get.PortGroupSecurityPolicy
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.policy.security.Get',
                            portgroupname=portgroupname,
                            )   