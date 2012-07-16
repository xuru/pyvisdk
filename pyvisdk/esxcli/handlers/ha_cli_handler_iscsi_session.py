
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiSession(Base):
    '''
    Operations that can be performed on iSCSI sessions
    '''
    moid = 'ha-cli-handler-iscsi-session'
    def add(self, adapter, isid=None, name=None):
        '''
        Login sessions on current iSCSI configuration.
        :param adapter: string, The iSCSI adapter name.
        :param isid: string, The isid of a session to duplicate for login.
        :param name: string, The iSCSI target name.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.session.Add',
                            adapter=adapter,
                            isid=isid,
                            name=name,
                            )
    def list(self, adapter=None, isid=None, name=None):
        '''
        List iSCSI Sessions.
        :param adapter: string, The iSCSI adapter name.
        :param isid: string, The iSCSI session identifier.
        :param name: string, The iSCSI target name.
        :returns: vim.EsxCLI.iscsi.session.list.Session[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.session.List',
                            adapter=adapter,
                            isid=isid,
                            name=name,
                            )
    def remove(self, adapter, isid=None, name=None):
        '''
        Logout sessions on current iSCSI configuration.
        :param adapter: string, The iSCSI adapter name.
        :param isid: string, The isid of a session to duplicate for login.
        :param name: string, The name of the target to login to.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.session.Remove',
                            adapter=adapter,
                            isid=isid,
                            name=name,
                            )   