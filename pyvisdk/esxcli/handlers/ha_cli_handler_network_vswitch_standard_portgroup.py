
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandardPortgroup(Base):
    '''
    Commands to list and manipulate Port Groups on an ESX host.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard-portgroup'
    def add(self, portgroupname, vswitchname):
        '''
        Allows the addition of a standard port group to a virtual switch.
        :param portgroupname: string, The name of the port group to add
        :param vswitchname: string, The virtual switch to add the port group to.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.Add',
                            portgroupname=portgroupname,
                            vswitchname=vswitchname,
                            )
    def set(self, portgroupname, vlanid=None):
        '''
        Set the vlan id for the given port group
        :param portgroupname: string, The name of the port group to set vlan id for.
        :param vlanid: long, The vlan id for this port group. This value is in the range (0 - 4095)
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.Set',
                            portgroupname=portgroupname,
                            vlanid=vlanid,
                            )
    def list(self):
        '''
        List all of the port groups currently on the system.
        :returns: vim.EsxCLI.network.vswitch.standard.portgroup.list.PortGroup[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.List',
                            )
    def remove(self, portgroupname, vswitchname):
        '''
        Remove a port group from the given virtual switch
        :param portgroupname: string,  
        :param vswitchname: string,  
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.Remove',
                            portgroupname=portgroupname,
                            vswitchname=vswitchname,
                            )   