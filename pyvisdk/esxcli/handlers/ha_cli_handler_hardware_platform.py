
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class HardwarePlatform(Base):
    '''
    Platform information.
    '''
    moid = 'ha-cli-handler-hardware-platform'
    def get(self):
        '''
        Get information about the platform
        :returns: vim.EsxCLI.hardware.platform.get.PlatformGet
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.platform.Get',
                            )   