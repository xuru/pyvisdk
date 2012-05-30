
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIpInterfaceIpv6Address(Base):
    '''
    Commands to list and update IPv6 addresses assigned to the system.
    '''
    moid = 'ha-cli-handler-network-ip-interface-ipv6-address'
    def add(self, interfacename, ipv6):
        '''
        Add a static IPv6 address to a given VMkernel network interface.
        :param interfacename: string, The name of the VMkernel network interface to add a static IPv6 address to. This name must be an interface listed in the interface list command.
        :param ipv6: string, The IPv6 address to add to the given VMkernel network interface. This must be in X:X:X::/X format
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.ipv6.address.Add',
                            interfacename=interfacename,
                            ipv6=ipv6,
                            )
    def list(self):
        '''
        This command will list all of the IPv6 addresses currently assigned to the system
        :returns: vim.EsxCLI.network.ip.interface.ipv6.address.list.IPv6Interface[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.ipv6.address.List',
                            )
    def remove(self, interfacename, ipv6):
        '''
        Remove an IPv6 address from a given VMkernel network interface.
        :param interfacename: string, The name of the VMkernel network interface to remove an IPv6 address from. This name must be an interface listed in the interface list command.
        :param ipv6: string, The IPv6 address to remove from the given VMkernel network interface. This must be in X:X:X::/X format
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.ipv6.address.Remove',
                            interfacename=interfacename,
                            ipv6=ipv6,
                            )   