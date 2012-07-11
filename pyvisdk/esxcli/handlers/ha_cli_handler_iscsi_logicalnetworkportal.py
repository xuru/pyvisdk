
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiLogicalnetworkportal(Base):
    '''
    Operations that can be performed on iSCSI Logical Network Portal (vmknic)
    '''
    moid = 'ha-cli-handler-iscsi-logicalnetworkportal'
    def list(self, adapter=None):
        '''
        List Logical Network Portals for iSCSI Adapter
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.logicalnetworkportal.list.LogicalNetworkPortal[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.logicalnetworkportal.List',
                            adapter=adapter,
                            )   