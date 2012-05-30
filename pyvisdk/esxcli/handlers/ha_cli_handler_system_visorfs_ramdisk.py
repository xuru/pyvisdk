
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemVisorfsRamdisk(Base):
    '''
    Operations pertaining to visorfs ramdisks.
    '''
    moid = 'ha-cli-handler-system-visorfs-ramdisk'
    def add(self, maxsize, minsize, name, permissions, target):
        '''
        Add a new Visorfs RAM disk to the ESXi Host and mount it.
        :param maxsize: long, Maximum size (max reservation in MiB)
        :param minsize: long, Minimum size (min reservation in MiB)
        :param name: string, Name for the ramdisk
        :param permissions: string, Permissions for the root of the ramdisk (mode)
        :param target: string, Mountpoint for the ramdisk
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.visorfs.ramdisk.Add',
                            maxsize=maxsize,
                            minsize=minsize,
                            name=name,
                            permissions=permissions,
                            target=target,
                            )
    def list(self):
        '''
        List the RAM disks used by the host.
        :returns: vim.EsxCLI.system.visorfs.ramdisk.list.VisorfsRamdisk[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.visorfs.ramdisk.List',
                            )
    def remove(self, target):
        '''
        Remove a Visorfs RAM disk from the ESXi Host.
        :param target: string, Mountpoint for the ramdisk
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.visorfs.ramdisk.Remove',
                            target=target,
                            )   