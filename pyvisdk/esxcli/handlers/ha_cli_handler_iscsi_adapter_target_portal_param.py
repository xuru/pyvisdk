
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterTargetPortalParam(Base):
    '''
    Operations that can be performed on iSCSI target portal parameters
    '''
    moid = 'ha-cli-handler-iscsi-adapter-target-portal-param'
    def set(self, adapter, address, key, name, default=None, inherit=None, value=None):
        '''
        Set the iSCSI parameter for the iSCSI Target.
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI target address: <ip/dns[:port]>
        :param default: boolean, Resetting iSCSI parameter setting to default.
        :param inherit: boolean, Inheriting iSCSI parameter setting from parent.
        :param key: string, The iSCSI parameter key
        :param name: string, The iSCSI target name: <iqn/eui>
        :param value: string, The iSCSI parameter value
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.target.portal.param.Set',
                            adapter=adapter,
                            address=address,
                            default=default,
                            inherit=inherit,
                            key=key,
                            name=name,
                            value=value,
                            )
    def get(self, adapter, address, name):
        '''
        Get iSCSI parameter on a target
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI target address: <ip/dns[:port]>
        :param name: string, The iSCSI target name: <iqn/eui>
        :returns: vim.EsxCLI.iscsi.adapter.target.portal.param.get.iScsiParm[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.target.portal.param.Get',
                            adapter=adapter,
                            address=address,
                            name=name,
                            )   