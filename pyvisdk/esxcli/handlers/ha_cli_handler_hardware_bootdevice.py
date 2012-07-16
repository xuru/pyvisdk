
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class HardwareBootdevice(Base):
    '''
    Boot device information.
    '''
    moid = 'ha-cli-handler-hardware-bootdevice'
    def list(self):
        '''
        List the boot device order, if available, for this host.
        :returns: vim.EsxCLI.hardware.bootdevice.list.BootDeviceList[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.bootdevice.List',
                            )   