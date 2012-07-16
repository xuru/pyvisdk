
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpSatpGenericDeviceconfig(Base):
    '''
    SATP device configuration operations
    '''
    moid = 'ha-cli-handler-storage-nmp-satp-generic-deviceconfig'
    def set(self, config, device=None):
        '''
        Allow setting of per device SATP configuration parameters. This command will set the configuration for the given device with whichever SATP it is currently configurated with.
        :param config: string, The configuration string you wish to set.
        :param device: string, The device you wish to set SATP configuration for.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.generic.deviceconfig.Set',
                            config=config,
                            device=device,
                            )
    def get(self, device):
        '''
        Allow retrieving of per device SATP configuration parameters.
        :param device: string, The device you wish to get SATP configuration for.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.generic.deviceconfig.Get',
                            device=device,
                            )   