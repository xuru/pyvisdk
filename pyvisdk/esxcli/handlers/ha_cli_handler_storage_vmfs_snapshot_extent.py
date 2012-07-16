
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageVmfsSnapshotExtent(Base):
    '''
    Manage VMFS snapshot extents.
    '''
    moid = 'ha-cli-handler-storage-vmfs-snapshot-extent'
    def list(self, volumelabel=None, volumeuuid=None):
        '''
        List extents of unresolved snapshots/replicas of VMFS volume.
        :param volumelabel: string, The VMFS volume label of the target snapshot to enumerate.
        :param volumeuuid: string, The VMFS volume uuid of the target snapshot to enumerate.
        :returns: vim.EsxCLI.storage.vmfs.snapshot.extent.list.VMFSSnapshotExtent[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.vmfs.snapshot.extent.List',
                            volumelabel=volumelabel,
                            volumeuuid=volumeuuid,
                            )   