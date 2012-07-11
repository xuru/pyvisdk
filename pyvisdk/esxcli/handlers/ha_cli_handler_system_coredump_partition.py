
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemCoredumpPartition(Base):
    '''
    Operations pertaining to the VMkernel Core dump configuration on VMkernel Diagnostic partitions. 
    '''
    moid = 'ha-cli-handler-system-coredump-partition'
    def set(self, enable=None, partition=None, smart=None, unconfigure=None):
        '''
        Set the specific VMkernel dump partition for this system. This will configure the dump partition for the next boot. This command will change the active dump partition to the partition specified.
        :param enable: boolean, Enable or disable the VMkernel dump partition. This option cannot be specified when setting or unconfiguring the dump partition.
        :param partition: string, The name of the partition to use. This should be a device name with a partition number at the end. Example: naa.xxxxx:1
        :param smart: boolean, This flag can be used only with --enable=true. It will cause the best available partition to be selected using the smart selection algorithm.
        :param unconfigure: boolean, Set the dump partition into an unconfigured state. This will remove the current configured dump partition for the next boot. This will result in the smart activate algorithm being used at the next boot.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.coredump.partition.Set',
                            enable=enable,
                            partition=partition,
                            smart=smart,
                            unconfigure=unconfigure,
                            )
    def list(self):
        '''
        List all of the partitions on the system that have a partition type matching the VMware Core partition type. Also indicate which partition, if any, is being used as the system's dump partition and which is configured to be used at next boot.
        :returns: vim.EsxCLI.system.coredump.partition.list.DumpPartition[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.coredump.partition.List',
                            )
    def get(self):
        '''
        Get one of the dump partition configured values. This command will print either the active dump partition or the configured dump partition depending on the flags passed.
        :returns: vim.EsxCLI.system.coredump.partition.get.KernelDumpParition
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.coredump.partition.Get',
                            )   