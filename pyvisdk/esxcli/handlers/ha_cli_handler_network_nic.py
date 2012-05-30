
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkNic(Base):
    '''
    Operations having to do with the configuration of Network Interface Card and getting and updating the NIC settings.
    '''
    moid = 'ha-cli-handler-network-nic'
    def down(self, nicname):
        '''
        Bring down the specified network device.
        :param nicname: string, The name of the NIC to configured. This must be one of the cards listed in the nic list command.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.nic.Down',
                            nicname=nicname,
                            )
    def set(self, nicname, auto=None, duplex=None, messagelevel=None, phyaddress=None, port=None, speed=None, transceivertype=None, wakeonlan=None):
        '''
        Set the general options for the specified ethernet device.
        :param auto: boolean, Set the speed and duplexity settings to autonegotiate.
        :param duplex: string, The duplex to set this NIC to. Acceptable values are :  [full, half]
        :param messagelevel: long, Sets the driver message level. Meaning differ per driver.
        :param nicname: string, The name of the NIC to configured. This must be one of the cards listed in the nic list command.
        :param phyaddress: long, Set the PHY address of the device
        :param port: string, Selects device port. Available device ports are 
    aui: Select aui as the device port
    bnc: Select bnc as the device port
    fibre: Select mii as the device port
    mii: Select mii as the device port
    tp: Select tp as the device port

        :param speed: long, The speed to set this NIC to. Acceptable values are :  [10, 100, 1000, 10000]
        :param transceivertype: string, Selects transeiver type. Currently only internal and external can be specified, in the future future types might be added. Available transeiver types are 
    external: Set the transceiver type to external
    internal: Set the transceiver type to internal

        :param wakeonlan: string, Sets Wake-on-LAN options. Not all devices support this. The argument to this option is a string of characters specifying which options to enable. 
p Wake on phy activity
u wake on unicast messages
m Wake on multicast messages
b wake on broadcast messages
a Wake on ARP
g Wake on MagicPacket(tm)
s Enable SecureOn(tm) password for MagicPacket(tm)

        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.nic.Set',
                            auto=auto,
                            duplex=duplex,
                            messagelevel=messagelevel,
                            nicname=nicname,
                            phyaddress=phyaddress,
                            port=port,
                            speed=speed,
                            transceivertype=transceivertype,
                            wakeonlan=wakeonlan,
                            )
    def list(self):
        '''
        This command will list the Physical NICs currently installed and loaded on the system.
        :returns: vim.EsxCLI.network.nic.list.Nic[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.nic.List',
                            )
    def up(self, nicname):
        '''
        Bring up the specified network device.
        :param nicname: string, The name of the NIC to configured. This must be one of the cards listed in the nic list command.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.nic.Up',
                            nicname=nicname,
                            )
    def get(self, nicname):
        '''
        Get the generic configuration of a network device
        :param nicname: string, The name of the NIC to configured. This must be one of the cards listed in the nic list command.
        :returns: vim.EsxCLI.network.nic.get.NICInfo
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.nic.Get',
                            nicname=nicname,
                            )   