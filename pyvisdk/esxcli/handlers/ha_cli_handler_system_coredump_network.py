
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemCoredumpNetwork(Base):
    '''
    Operations pertaining to the VMkernel Core dump configuration on network dump servers. 
    '''
    moid = 'ha-cli-handler-system-coredump-network'
    def set(self, enable=None, interfacename=None, serveripv4=None, serverport=None):
        '''
        Set the parameters used for network core dump
        :param enable: boolean, Enable network dump. This option cannot be specified when setting the dump parameters below.
        :param interfacename: string, An active interface to be used for the network core dump. Required option when setting dump parameters.
        :param serveripv4: string, IP address of the core dump server. Required option when setting dump parameters.
        :param serverport: long, Port on which the core dump server is listening. (Optional)
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.coredump.network.Set',
                            enable=enable,
                            interfacename=interfacename,
                            serveripv4=serveripv4,
                            serverport=serverport,
                            )
    def get(self):
        '''
        Get the currently configured parameters for network coredump, if enabled.
        :returns: vim.EsxCLI.system.coredump.network.get.NetworkCoredump
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.coredump.network.Get',
                            )   