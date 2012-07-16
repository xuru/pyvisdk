
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiPhysicalnetworkportal(Base):
    '''
    Operations that can be performed on iSCSI Physical Network Portal (vmnic)
    '''
    moid = 'ha-cli-handler-iscsi-physicalnetworkportal'
    def list(self, adapter=None):
        '''
        List Physical Network Portal for iSCSI Adapter
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.physicalnetworkportal.list.PhysicalNetworkPortal[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.physicalnetworkportal.List',
                            adapter=adapter,
                            )   