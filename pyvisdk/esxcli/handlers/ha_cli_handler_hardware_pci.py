
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class HardwarePci(Base):
    '''
    PCI device information and configuration.
    '''
    moid = 'ha-cli-handler-hardware-pci'
    def list(self):
        '''
        List all of the PCI devices on this host.
        :returns: vim.EsxCLI.hardware.pci.list.PciDevice[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.pci.List',
                            )   