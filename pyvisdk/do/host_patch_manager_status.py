
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPatchManagerStatus(DynamicData):
    '''
    '''
    
    def __init__(self, applicable, id, installed, installState, integrity, prerequisitePatch, reason, reconnectRequired, restartRequired, supersededPatchIds, vmOffRequired):
        # MUST define these
        super(HostPatchManagerStatus, self).__init__()
    
        self.data['applicable'] = applicable
        self.data['id'] = id
        self.data['installed'] = installed
        self.data['installState'] = installState
        self.data['integrity'] = integrity
        self.data['prerequisitePatch'] = prerequisitePatch
        self.data['reason'] = reason
        self.data['reconnectRequired'] = reconnectRequired
        self.data['restartRequired'] = restartRequired
        self.data['supersededPatchIds'] = supersededPatchIds
        self.data['vmOffRequired'] = vmOffRequired
    
    
    @property
    def applicable(self):
        '''Whether or not this update is applicable to this host. An update may not be
        applicable to the ESX host for many reasons--for example, it is obsolete,
        it conflicts with other installed patches or libraries, and so on. The
        reason shows some of the reasons why the update is not applicable. An
        update could be inapplicable with no reason listed. This is because the
        prerequisite install state is not correct. For example, update A is one of
        the prerequisites of update B. B not only requires A to be installed, but
        also requires the host is rebooted after A is installed. When A is
        installed and the host has not been restarted after the installation, B
        will not be applicable. In such a case, the scan on both updates A and B
        would yield a whole picture of the update applicable status.
        '''
        return self.data['applicable']

    @property
    def id(self):
        '''Unique identifier for this update.
        '''
        return self.data['id']

    @property
    def installed(self):
        '''Whether the update is installed on the server.
        '''
        return self.data['installed']

    @property
    def installState(self):
        '''The installation state of the update. Unset if the update is not installed on the
        server.
        '''
        return self.data['installState']

    @property
    def integrity(self):
        '''The integrity status of the update's metadata. The value would be unset if the
        integrity status is unknown to the server.
        '''
        return self.data['integrity']

    @property
    def prerequisitePatch(self):
        '''Prerequisite update.
        '''
        return self.data['prerequisitePatch']

    @property
    def reason(self):
        '''Possible reasons why an update is not applicable to the ESX host.
        '''
        return self.data['reason']

    @property
    def reconnectRequired(self):
        '''Whether or not this update requires caller to reconnect to the host. This is
        usually because the update is on the agent that running on the host, the
        agent would thus be restarted when the update is applied. Caller can
        reconnect (and possibly relogin) to the host after the agent has been
        restarted.
        '''
        return self.data['reconnectRequired']

    @property
    def restartRequired(self):
        '''Whether or not this update requires a host restart to take effect.
        '''
        return self.data['restartRequired']

    @property
    def supersededPatchIds(self):
        '''Patches that are superseded by this update.
        '''
        return self.data['supersededPatchIds']

    @property
    def vmOffRequired(self):
        '''Whether or not this update requires the host in maintenance mode.
        '''
        return self.data['vmOffRequired']

