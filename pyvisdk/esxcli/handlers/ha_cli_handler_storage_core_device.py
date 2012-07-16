
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreDevice(Base):
    '''
    Operations pertaining to the pluggable storage architectures' logical devices on the system. The operation currently allowed is to list the available devices on the system and the filters attached to each
    '''
    moid = 'ha-cli-handler-storage-core-device'
    def set(self, device, name=None, nopersist=None, state=None):
        '''
        Provide control to allow a user to modify a SCSI device's state.
        :param device: string, The device you wish to operate upon. This can be any of the UIDs that a device reports.
        :param name: string, The new name to assign the given device.
        :param nopersist: boolean, Set device state non-peristently; state is lost after reboot.
        :param state: string, Set the SCSI device state for a the specific device given. Valid values are : 
    off: Set the device's state to OFF.
    on: Set the device's state to ON.

        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.Set',
                            device=device,
                            name=name,
                            nopersist=nopersist,
                            state=state,
                            )
    def list(self, device=None):
        '''
        For devices currently registered with the PSA, list the filters attached to them.
        :param device: string, Filter the output of this command to only show a single device.
        :returns: vim.EsxCLI.storage.core.device.list.ScsiDevice[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.List',
                            device=device,
                            )
    def setconfig(self, device, detached=None, perenniallyreserved=None):
        '''
        Set device configuration
        :param detached: boolean, Mark device as detached.
        :param device: string, Apply the command to a single device.
        :param perenniallyreserved: boolean, Mark device as perennially reserved.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.Setconfig',
                            detached=detached,
                            device=device,
                            perenniallyreserved=perenniallyreserved,
                            )   