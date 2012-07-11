
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageFilesystem(Base):
    '''
    Operations pertaining to filesystems, also known as datastores, on the ESX host.
    '''
    moid = 'ha-cli-handler-storage-filesystem'
    def automount(self):
        '''
        Request mounting of known datastores not explicitly unmounted.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.filesystem.Automount',
                            )
    def mount(self, nopersist=None, volumelabel=None, volumeuuid=None):
        '''
        Connect to and mount an unmounted volume on the ESX host.
        :param nopersist: boolean, Mount the volume non-peristently; the volume will not be mounted after a restart.
        :param volumelabel: string, The label of the volume to mount. This volume must be unmounted for this operation to succeed.
        :param volumeuuid: string, The UUID of the VMFS filesystem to mount. This volume must be unmounted for this operation to succeed.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.filesystem.Mount',
                            nopersist=nopersist,
                            volumelabel=volumelabel,
                            volumeuuid=volumeuuid,
                            )
    def unmount(self, nopersist=None, volumelabel=None, volumepath=None, volumeuuid=None):
        '''
        Disconnect and unmount and existing VMFS or NAS volume. This will not delete the configuration for the volume, but will remove the volume from the list of mounted volumes.
        :param nopersist: boolean, Unmount the volume non-peristently; the volume will be automounted after a restart.
        :param volumelabel: string, The label of the volume to unmount.
        :param volumepath: string, The path of the volume to unmount.
        :param volumeuuid: string, The uuid of the volume to unmount.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.filesystem.Unmount',
                            nopersist=nopersist,
                            volumelabel=volumelabel,
                            volumepath=volumepath,
                            volumeuuid=volumeuuid,
                            )
    def list(self):
        '''
        List the volumes available to the host. This includes VMFS, NAS and VFAT partitions.
        :returns: vim.EsxCLI.storage.filesystem.list.FilesystemVolume[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.filesystem.List',
                            )
    def rescan(self):
        '''
        Issue a rescan operation to the VMkernel to have is scan storage devices for new mountable filesystems.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.filesystem.Rescan',
                            )   