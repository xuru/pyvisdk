
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIpInterfaceIpv6(Base):
    '''
    Commands to get and set IPv6 settings for vmknic.
    '''
    moid = 'ha-cli-handler-network-ip-interface-ipv6'
    def set(self, interfacename, enabledhcpv6=None, enablerouteradv=None, peerdns=None):
        '''
        Configure IPv6 settings for a given VMkernel network interface.
        :param enabledhcpv6: boolean, Setting this value to true will enable DHCPv6 on this interface and attempt to aquire an IPv6 address from the network 
        :param enablerouteradv: boolean, Setting this value to true will enable IPv6 Router Advertised IPv6 addresses to be added to this interface from any routers broadcasting on the local network.
        :param interfacename: string, The name of the VMkernel network interface to set IPv6 settings for. This name must be an interface listed in the interface list command.
        :param peerdns: boolean, A boolean value to indicate if the system should use the DNS settings published via DHCPv6 for this interface.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.ipv6.Set',
                            enabledhcpv6=enabledhcpv6,
                            enablerouteradv=enablerouteradv,
                            interfacename=interfacename,
                            peerdns=peerdns,
                            )
    def get(self, interfacename=None):
        '''
        Get IPv6 settings for VMkernel network interfaces. This does not include the IPv6 addresses which can be found in the listipv6 command
        :param interfacename: string, The name of the VMkernel network interface to limit the output of this command to.
        :returns: vim.EsxCLI.network.ip.interface.ipv6.get.IPv6Interface[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.interface.ipv6.Get',
                            interfacename=interfacename,
                            )   