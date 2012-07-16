
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpPspGenericDeviceconfig(Base):
    '''
    PSP device configuration operations
    '''
    moid = 'ha-cli-handler-storage-nmp-psp-generic-deviceconfig'
    def set(self, config, device):
        '''
        Allow setting of per device PSP configuration parameters.  This command will set the configuration for the given device with whichever PSP it is currently configurated with.
        :param config: string, The configuration string you wish to set.
        :param device: string, The device you wish to set PSP configuration for.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.generic.deviceconfig.Set',
                            config=config,
                            device=device,
                            )
    def get(self, device):
        '''
        Allow retrieving of per device PSP configuration parameters.
        :param device: string, The device you wish to get PSP configuration for.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.generic.deviceconfig.Get',
                            device=device,
                            )   