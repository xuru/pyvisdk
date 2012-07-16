
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpPspFixedDeviceconfig(Base):
    '''
    Fixed PSP preferred path configuration operations
    '''
    moid = 'ha-cli-handler-storage-nmp-psp-fixed-deviceconfig'
    def set(self, device, default=None, path=None):
        '''
        Allow setting of the perferred path on a given device controlled by the Fixed Path Selection Policy.
        :param default: boolean, Clear the preferred path selection for the given device.
        :param device: string, The device you wish to set the preferred path for. This device must be controlled by the Fixed Path Selection Policy
        :param path: string, The path you wish to set as the preferred path for the given device.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.fixed.deviceconfig.Set',
                            default=default,
                            device=device,
                            path=path,
                            )
    def get(self, device):
        '''
        Allow retrieving of Fixed Path Selection Policy settings for a given device.
        :param device: string, The device you wish to get the Preferred path for.  
        :returns: vim.EsxCLI.storage.nmp.psp.fixed.deviceconfig.get.FixedDeviceConfiguration
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.fixed.deviceconfig.Get',
                            device=device,
                            )   