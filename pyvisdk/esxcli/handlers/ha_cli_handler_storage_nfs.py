
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNfs(Base):
    '''
    Operations to create, manage and remove Network Attached Storage filesystems.
    '''
    moid = 'ha-cli-handler-storage-nfs'
    def add(self, host, share, volumename, readonly=None):
        '''
        Add a new NAS volume to the ESX Host and mount it with the given volume name.
        :param host: string, The hostname or IP address of the NAS volume to add and mount on the system.
        :param readonly: boolean, If set this flag will set the mount point to be read-only.
        :param share: string, The share name on the remote system to use for this NAS mount point.
        :param volumename: string, The volume name to use for the NAS mount.  This must be a unique volume name and cannot conflict with existing NAS, VMFS or other volume names.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nfs.Add',
                            host=host,
                            readonly=readonly,
                            share=share,
                            volumename=volumename,
                            )
    def list(self):
        '''
        List the NAS volumes currently known to the ESX host.
        :returns: vim.EsxCLI.storage.nfs.list.NasMount[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nfs.List',
                            )
    def remove(self, volumename):
        '''
        Remove an existing NAS volume from the ESX host.
        :param volumename: string, The volume name of the NAS volume to remove from the ESX host.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nfs.Remove',
                            volumename=volumename,
                            )   