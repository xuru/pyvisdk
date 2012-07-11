
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class HardwareCpuCpuid(Base):
    '''
    Information from the CPUID instruction on each CPU.
    '''
    moid = 'ha-cli-handler-hardware-cpu-cpuid'
    def get(self, cpu):
        '''
        Get CPUID fields for the given CPU.
        :param cpu: long, The ID of the CPU to query for CPUID data
        :returns: vim.EsxCLI.hardware.cpu.cpuid.get.CpuCpuId[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.cpu.cpuid.Get',
                            cpu=cpu,
                            )   