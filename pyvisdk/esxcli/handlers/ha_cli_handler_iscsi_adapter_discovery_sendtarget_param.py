
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterDiscoverySendtargetParam(Base):
    '''
    Operations that can be performed on iSCSI sendtarget's parameters
    '''
    moid = 'ha-cli-handler-iscsi-adapter-discovery-sendtarget-param'
    def set(self, adapter, address, key, default=None, inherit=None, value=None):
        '''
        Set the iSCSI parameter for the iSCSI Sendtarget.
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI sendtarget address: <ip/dns[:port]>
        :param default: boolean, Resetting iSCSI parameter setting to default.
        :param inherit: boolean, Inheriting iSCSI parameter setting from parent.
        :param key: string, The iSCSI parameter key
        :param value: string, The iSCSI parameter value
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.sendtarget.param.Set',
                            adapter=adapter,
                            address=address,
                            default=default,
                            inherit=inherit,
                            key=key,
                            value=value,
                            )
    def get(self, adapter, address):
        '''
        Get iSCSI parameter on a sendtarget address
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI sendtarget address: <ip/dns[:port]>
        :returns: vim.EsxCLI.iscsi.adapter.discovery.sendtarget.param.get.iScsiParm[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.sendtarget.param.Get',
                            adapter=adapter,
                            address=address,
                            )   