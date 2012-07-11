
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiSessionConnection(Base):
    '''
    Operations that can be performed on iSCSI connections
    '''
    moid = 'ha-cli-handler-iscsi-session-connection'
    def list(self, adapter=None, cid=None, isid=None, name=None):
        '''
        List iSCSI connections.
        :param adapter: string, The iSCSI adapter name.
        :param cid: string, The iSCSI connection identifier(CID).
        :param isid: string, The iSCSI session identifier(ISID).
        :param name: string, The iSCSI target name.
        :returns: vim.EsxCLI.iscsi.session.connection.list.Connection[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.session.connection.List',
                            adapter=adapter,
                            cid=cid,
                            isid=isid,
                            name=name,
                            )   