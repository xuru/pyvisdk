
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageVmfsSnapshot(Base):
    '''
    Manage VMFS snapshots.
    '''
    moid = 'ha-cli-handler-storage-vmfs-snapshot'
    def resignature(self, volumelabel=None, volumeuuid=None):
        '''
        Resignature a snapshot/replica of a VMFS volume.
        :param volumelabel: string, The VMFS volume label of the snapshot to resignature.
        :param volumeuuid: string, The VMFS volume uuid of the snapshot to resignature.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.vmfs.snapshot.Resignature',
                            volumelabel=volumelabel,
                            volumeuuid=volumeuuid,
                            )
    def mount(self, nopersist=None, volumelabel=None, volumeuuid=None):
        '''
        Mount a snapshot/replica of a VMFS volume.
        :param nopersist: boolean, Mount the volume non-peristently; the volume will not be automounted after a restart.
        :param volumelabel: string, The VMFS volume label of the snapshot to mount.
        :param volumeuuid: string, The VMFS volume uuid of the snapshot to mount.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.vmfs.snapshot.Mount',
                            nopersist=nopersist,
                            volumelabel=volumelabel,
                            volumeuuid=volumeuuid,
                            )
    def list(self, volumelabel=None, volumeuuid=None):
        '''
        List unresolved snapshots/replicas of VMFS volume.
        :param volumelabel: string, The VMFS volume label of the snapshot to list.
        :param volumeuuid: string, The VMFS volume uuid of the snapshot to list.
        :returns: vim.EsxCLI.storage.vmfs.snapshot.list.VMFSSnapshot[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.vmfs.snapshot.List',
                            volumelabel=volumelabel,
                            volumeuuid=volumeuuid,
                            )   