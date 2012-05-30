
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterTargetPortal(Base):
    '''
    Operations that can be performed on iSCSI target portal
    '''
    moid = 'ha-cli-handler-iscsi-adapter-target-portal'
    def list(self, adapter=None, name=None):
        '''
        List iSCSI target portals.
        :param adapter: string, The iSCSI adapter name.
        :param name: string, The iSCSI target name.
        :returns: vim.EsxCLI.iscsi.adapter.target.portal.list.TargetPortal[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.target.portal.List',
                            adapter=adapter,
                            name=name,
                            )   