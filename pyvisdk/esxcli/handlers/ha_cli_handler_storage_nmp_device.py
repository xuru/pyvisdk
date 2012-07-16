
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpDevice(Base):
    '''
    Operations pertaining to the devices currently claimed by the VMware Native Multipath Plugin.
    '''
    moid = 'ha-cli-handler-storage-nmp-device'
    def set(self, device, default=None, psp=None):
        '''
        Allow setting of the Path Selection Policy (PSP) for the given device to one of the loaded policies on the system.
        :param default: boolean, The Path selection policy is set back to the default for the assigned SATP for this device.
        :param device: string, The device you wish to set the Path Selection Policy for.
        :param psp: string, The Path selection policy you wish to assign to the given device.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.device.Set',
                            default=default,
                            device=device,
                            psp=psp,
                            )
    def list(self, device=None):
        '''
        List the devices currently controlled by the VMware NMP Multipath Plugin and show the SATP and PSP information associated with that device.
        :param device: string, Filter the output of this command to only show a single device.
        :returns: vim.EsxCLI.storage.nmp.device.list.NmpDevice[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.device.List',
                            device=device,
                            )   