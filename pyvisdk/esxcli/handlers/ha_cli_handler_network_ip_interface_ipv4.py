
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIpInterfaceIpv4(Base):
    '''
    Commands to get and set IPv4 settings for vmknic.
    '''
    moid = 'ha-cli-handler-network-ip-interface-ipv4'
    def set(self, interfacename, type, ipv4=None, netmask=None, peerdns=None):
        '''
        Configure IPv4 setting for a given VMkernel network interface.
        :param interfacename: string, The name of the VMkernel network interface to set IPv4 settings for. This name must be an interface listed in the interface list command.
        :param ipv4: string, The static IPv4 address for this interface.
        :param netmask: string, The static IPv4 netmask for this interface.
        :param peerdns: boolean, A boolean value to indicate if the system should use the DNS settings published via DHCP for this interface.
        :param type: string, IPv4 Address type : 
    dhcp: Use DHCP to aquire IPv4 setting for this interface.
    none: Remove IPv4 settings form this interface.
    static: Set Static IPv4 information for this interface. Requires --ipv4 and --netmask options.

        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.ipv4.Set',
                            interfacename=interfacename,
                            ipv4=ipv4,
                            netmask=netmask,
                            peerdns=peerdns,
                            type=type,
                            )
    def get(self, interfacename=None):
        '''
        Get IPv4 settings for VMkernel network interfaces.
        :param interfacename: string, The name of the VMkernel network interface to limit the output of this command to.
        :returns: vim.EsxCLI.network.ip.interface.ipv4.get.IPv4Interface[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.ipv4.Get',
                            interfacename=interfacename,
                            )   