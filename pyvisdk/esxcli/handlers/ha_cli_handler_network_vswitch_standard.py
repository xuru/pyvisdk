
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandard(Base):
    '''
    Commands to list and manipulate Legacy Virtual Switches on an ESX host.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard'
    def add(self, vswitchname, ports=None):
        '''
        Add a new virtual switch to the ESXi networking system.
        :param ports: long, The number of ports to to give this newly created virtual switch. Maximum ports per virtual switch is 4096. If no value is given the default value(128) is used. The number of ports is limited by the number of already allocated ports on the host. The system wide port count cannot be greater than 4608.
        :param vswitchname: string, The name of the virtual switch to create.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.Add',
                            ports=ports,
                            vswitchname=vswitchname,
                            )
    def set(self, vswitchname, cdpstatus=None, mtu=None):
        '''
        This command sets the MTU size and CDP status of a given virtual switch.
        :param cdpstatus: string, The CDP status of the given virtual switch. It can be 'down', 'listen', 'advertise' or 'both'
        :param mtu: long, The MTU size of the given virtual switch. 
        :param vswitchname: string, The name of virtual switch to apply the configurations.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.Set',
                            cdpstatus=cdpstatus,
                            mtu=mtu,
                            vswitchname=vswitchname,
                            )
    def list(self, vswitchname=None):
        '''
        List the virtual switches current on the ESXi host.
        :param vswitchname: string, Limit the output of this command to only virtual switches with the given name.
        :returns: vim.EsxCLI.network.vswitch.standard.list.VirtualSwitch[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.List',
                            vswitchname=vswitchname,
                            )
    def remove(self, vswitchname):
        '''
        Remove a virtual switch from the ESXi networking system.
        :param vswitchname: string, The name of the virtual switch to remove.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.Remove',
                            vswitchname=vswitchname,
                            )   