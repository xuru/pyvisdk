
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpSatp(Base):
    '''
    Operations pertaining to the Storage Array Type Plugins for the VMware Native Multipath Plugin.
    '''
    moid = 'ha-cli-handler-storage-nmp-satp'
    def set(self, defaultpsp, satp, boot=None):
        '''
        Set the default Path Selection Policy for a given Storage Array Type Plugin (SATP).
        :param boot: boolean, This is a system default rule added at boot time. Do not modify esx.conf or add to host profile.
        :param defaultpsp: string, The default path selection policy to set for a given --satp 
        :param satp: string, The SATP name for the Storage Array Type Plugin on which this command will operate.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.Set',
                            boot=boot,
                            defaultpsp=defaultpsp,
                            satp=satp,
                            )
    def list(self):
        '''
        List the Storage Array Type Plugins (SATP) that are currently loaded into the NMP system and display information about those SATPs
        :returns: vim.EsxCLI.storage.nmp.satp.list.StorageArrayTypePlugin[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.List',
                            )   