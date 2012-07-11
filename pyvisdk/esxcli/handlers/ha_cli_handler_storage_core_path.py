
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCorePath(Base):
    '''
    Operations pertaining to the pluggable storage architectures' SCSI device paths on the system.
    '''
    moid = 'ha-cli-handler-storage-core-path'
    def set(self, path, state):
        '''
        Provide control to allow a user to modify a single path's state. This efffectively allows a user to enable or disable SCSI paths. The user is not able to change the full range of path states, but can toggle between 'active' and 'off'. Please NOTE changing the Path state on any path that is the only path to a given device is likely to fail. The VMkernel will not change the path's state if changing the state would cause an 'All paths down' state or the device is currently in use.
        :param path: string, Select the path to set path state on. This can be a Runtime Name or Path UID
        :param state: string, Set the SCSI path state for a the specific path given. Valid values are : 
    active: Set the path's state to active. This may be immediately changed by the system to another state if the active state is not appropriate.
    off: Administratively disable this path.

        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.path.Set',
                            path=path,
                            state=state,
                            )
    def list(self, device=None, path=None):
        '''
        List all the SCSI paths on the system.
        :param device: string, Limit the output to paths to a specific device.   This name can be any of the UIDs for a specific device.
        :param path: string, Limit the output to a specific path. This  name can be either the UID or the runtime name of the path.
        :returns: vim.EsxCLI.storage.core.path.list.ScsiPath[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.path.List',
                            device=device,
                            path=path,
                            )   