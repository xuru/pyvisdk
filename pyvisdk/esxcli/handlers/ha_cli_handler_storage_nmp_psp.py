
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpPsp(Base):
    '''
    Operations pertaining to the Path Selection Policy Plugins for the VMware Native Multipath Plugin.
    '''
    moid = 'ha-cli-handler-storage-nmp-psp'
    def list(self):
        '''
        List the Path Selection Plugins (PSP) that are currently loaded into the NMP system and display information about those PSPs
        :returns: vim.EsxCLI.storage.nmp.psp.list.PathSelectionPolicy[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.List',
                            )   