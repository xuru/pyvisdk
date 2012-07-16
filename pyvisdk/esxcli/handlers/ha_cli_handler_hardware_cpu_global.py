
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class HardwareCpuGlobal(Base):
    '''
    Information and configuration global to all CPUs.
    '''
    moid = 'ha-cli-handler-hardware-cpu-global'
    def set(self, hyperthreading):
        '''
        Set properties that are global to all CPUs.
        :param hyperthreading: boolean, Enable or disable hyperthreading
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.cpu.global.Set',
                            hyperthreading=hyperthreading,
                            )
    def get(self):
        '''
        Get properties that are global to all CPUs.
        :returns: vim.EsxCLI.hardware.cpu.global.get.Cpu
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.cpu.global.Get',
                            )   