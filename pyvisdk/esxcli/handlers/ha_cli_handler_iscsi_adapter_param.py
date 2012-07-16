
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterParam(Base):
    '''
    Operations that can be performed on iSCSI adapter parameters
    '''
    moid = 'ha-cli-handler-iscsi-adapter-param'
    def set(self, adapter, key, default=None, value=None):
        '''
        Set the iSCSI parameter for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :param default: boolean, Resetting iSCSI parameter setting to default.
        :param key: string, The iSCSI initiator parameter key.
        :param value: string, The iSCSI initiator parameter value.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.param.Set',
                            adapter=adapter,
                            default=default,
                            key=key,
                            value=value,
                            )
    def get(self, adapter):
        '''
        Get the iSCSI parameters for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.adapter.param.get.iScsiParm[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.param.Get',
                            adapter=adapter,
                            )   