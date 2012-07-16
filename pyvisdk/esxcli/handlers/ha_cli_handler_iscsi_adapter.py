
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapter(Base):
    '''
    Operations that can be performed on iSCSI adapters
    '''
    moid = 'ha-cli-handler-iscsi-adapter'
    def set(self, adapter, alias=None, name=None):
        '''
        Set the iSCSI name and alias for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :param alias: string, The iSCSI initiator alias.
        :param name: string, The iSCSI initiator name.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.Set',
                            adapter=adapter,
                            alias=alias,
                            name=name,
                            )
    def list(self, adapter=None):
        '''
        List all the iSCSI Host Bus Adapters on the system.
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.adapter.list.iScsiAdapter[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.List',
                            adapter=adapter,
                            )
    def get(self, adapter):
        '''
        List the iSCSI information for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.adapter.get.AdapterInfo[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.Get',
                            adapter=adapter,
                            )   