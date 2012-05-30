
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterFirmware(Base):
    '''
    Operations that can be performed on iSCSI adapter firmware
    '''
    moid = 'ha-cli-handler-iscsi-adapter-firmware'
    def set(self, adapter, file):
        '''
        Upload the iSCSI firmware for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :param file: string, Path to the firmware file to download.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.firmware.Set',
                            adapter=adapter,
                            file=file,
                            )
    def get(self, adapter, file):
        '''
        Validate the iSCSI firmware for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :param file: string, Path to the firmware file to retrieve information from.
        :returns: vim.EsxCLI.iscsi.adapter.firmware.get.AdapterFirmware[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.firmware.Get',
                            adapter=adapter,
                            file=file,
                            )   