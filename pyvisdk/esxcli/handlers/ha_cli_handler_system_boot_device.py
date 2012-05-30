
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemBootDevice(Base):
    '''
    Display the system boot device
    '''
    moid = 'ha-cli-handler-system-boot-device'
    def get(self):
        '''
        Get the systems boot device.
        :returns: vim.EsxCLI.system.boot.device.get.SystemBootDevice
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.boot.device.Get',
                            )   