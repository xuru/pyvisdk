
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchDvsVmware(Base):
    '''
    Commands to retrieve VMware vSphere Distributed Switch information
    '''
    moid = 'ha-cli-handler-network-vswitch-dvs-vmware'
    def list(self, vdsname=None):
        '''
        List the VMware vSphere Distributed Switch currently configured on the ESXi host.
        :param vdsname: string, Limit the output of this command to only vDS with the given name.
        :returns: vim.EsxCLI.network.vswitch.dvs.vmware.list.VDS[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.dvs.vmware.List',
                            vdsname=vdsname,
                            )   