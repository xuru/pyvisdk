
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class HardwareCpu(Base):
    '''
    CPU information.
    '''
    moid = 'ha-cli-handler-hardware-cpu'
    def list(self):
        '''
        List all of the CPUs on this host.
        :returns: vim.EsxCLI.hardware.cpu.list.Cpu[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.cpu.List',
                            )   