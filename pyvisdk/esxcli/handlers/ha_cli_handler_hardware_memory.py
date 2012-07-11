
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class HardwareMemory(Base):
    '''
    Memory information.
    '''
    moid = 'ha-cli-handler-hardware-memory'
    def get(self):
        '''
        Get information about memory.
        :returns: vim.EsxCLI.hardware.memory.get.Memory
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.memory.Get',
                            )   