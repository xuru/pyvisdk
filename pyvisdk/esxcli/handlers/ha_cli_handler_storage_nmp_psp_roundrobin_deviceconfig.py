
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpPspRoundrobinDeviceconfig(Base):
    '''
    Round robin PSP device configuration operations
    '''
    moid = 'ha-cli-handler-storage-nmp-psp-roundrobin-deviceconfig'
    def set(self, device, bytes=None, iops=None, type=None, useano=None):
        '''
        Allow setting of the Round Robin path options on a given device controlled by the Round Robin Selection Policy.
        :param bytes: long, When the --type option is set to 'bytes' this is the  value that will be assigned to the byte limit value for this device.
        :param device: string, The device you wish to set the Round Robin settings for. This device must be controlled by the Round Roubin Path Selection Policy
        :param iops: long, When the --type option is set to 'iops' this is the  value that will be assigned to the I/O operation limit value for this device.
        :param type: string, Set the type of the Round Robin path switching that should be enabled for this device. Valid values for type are: 
    bytes: Set the trigger for path switching based on the number of bytes sent down a path.
    default: Set the trigger for path switching back to default values.
    iops: Set the trigger for path switching based on the number of I/O operations on a path.

        :param useano: boolean, Set useano to true,to also include non-optimizedpaths in the set of active paths used to issue I/Os on this device,otherwise set it to false
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.roundrobin.deviceconfig.Set',
                            bytes=bytes,
                            device=device,
                            iops=iops,
                            type=type,
                            useano=useano,
                            )
    def get(self, device):
        '''
        Allow retrieving of Round Robin Path Selection Policy settings for a given device.
        :param device: string, The device you wish to get the Round Robin properties for.
        :returns: vim.EsxCLI.storage.nmp.psp.roundrobin.deviceconfig.get.RoundRobinDeviceConfiguration
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.roundrobin.deviceconfig.Get',
                            device=device,
                            )   