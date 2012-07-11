
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreAdapter(Base):
    '''
    Operations on SCSI Host Bus Adapters on the system.
    '''
    moid = 'ha-cli-handler-storage-core-adapter'
    def rescan(self, adapter=None, all=None, skipclaim=None, skipfsscan=None, type=None):
        '''
        Rescan SCSI HBAs to search for new Devices, remove DEAD paths and update path state. This operation will also run an claim operation equivalent to the claimrule run command and a filesystem rescan.
        :param adapter: string, Select the adapter to use when rescanning SCSI adapters. This must be a SCSI HBA name as shown in the adapter list command. This cannot be used with the --all option
        :param all: boolean, Indicate the rescan should rescan all adapters instead of a specific one.
        :param skipclaim: boolean, By default after an add operation a claiming session is run to find new devices and have them be claimed by the appropriate Multipath Plugin. Passing this flag will skip that claiming session.
        :param skipfsscan: boolean, By default after all rescan operations a filesystem scan is performed to add newly found filesystems and remove any filesystems that are no longer available. Passing this flag will skip that filesystem scan.
        :param type: string, Specify the type of rescan to perform. Available types are 
    add: Perform rescan and only add new devices if any.
    all: Perform rescan and do all opertaions (this is the default action.)
    delete: Perform rescan and only delete DEAD devices.
    update: Rescan existing paths only and update path states.

        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.adapter.Rescan',
                            adapter=adapter,
                            all=all,
                            skipclaim=skipclaim,
                            skipfsscan=skipfsscan,
                            type=type,
                            )
    def list(self):
        '''
        List all the SCSI Host Bus Adapters on the system.
        :returns: vim.EsxCLI.storage.core.adapter.list.ScsiAdapter[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.adapter.List',
                            )   