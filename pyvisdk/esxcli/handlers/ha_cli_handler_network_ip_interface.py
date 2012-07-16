
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIpInterface(Base):
    '''
    Operations having to do with the creation, management and deletion of VMkernel network interfaces (vmknic).
    '''
    moid = 'ha-cli-handler-network-ip-interface'
    def add(self, portgroupname, interfacename=None, macaddress=None, mtu=None):
        '''
        Add a new VMkernel network interface.
        :param interfacename: string, The name of the VMkernel network interface to create. This name must be in the form vmkX, where X is a number 0-99
        :param macaddress: string, Set the MAC address for the newly created VMkernel network interface.
        :param mtu: long, Set the MTU setting for a given VMkernel network interface on creation
        :param portgroupname: string, The name of the port group to add this VMkernel network interface to. This option is required.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.Add',
                            interfacename=interfacename,
                            macaddress=macaddress,
                            mtu=mtu,
                            portgroupname=portgroupname,
                            )
    def set(self, interfacename, enabled=None, mtu=None):
        '''
        This command sets the enabled status and MTU size of a given IP interface 
        :param enabled: boolean, Set to true to enable the interface, set to false to disable it.
        :param interfacename: string, The name of the interface to apply the configurations.
        :param mtu: long, The MTU size of the IP interface. 
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.Set',
                            enabled=enabled,
                            interfacename=interfacename,
                            mtu=mtu,
                            )
    def list(self):
        '''
        This command will list the VMkernel network interfaces currently known to the system.
        :returns: vim.EsxCLI.network.ip.interface.list.NetworkInterface[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.List',
                            )
    def remove(self, interfacename):
        '''
        Remove a new VMkernel network interface from the ESXi host.
        :param interfacename: string, The name of the VMkernel network interface to remove. This name must be in the form vmkX, where X is a number 0-99
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.Remove',
                            interfacename=interfacename,
                            )   