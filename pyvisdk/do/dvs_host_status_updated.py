
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsHostStatusUpdated(DvsEvent):
    '''A host has it's status or statusDetail updated.
    '''
    
    def __init__(self, hostMember, newStatus, newStatusDetail, oldStatus, oldStatusDetail):
        # MUST define these
        super(DvsHostStatusUpdated, self).__init__()
    
        self.data['hostMember'] = hostMember
        self.data['newStatus'] = newStatus
        self.data['newStatusDetail'] = newStatusDetail
        self.data['oldStatus'] = oldStatus
        self.data['oldStatusDetail'] = oldStatusDetail
    
    
    @property
    def hostMember(self):
        '''The host.
        '''
        return self.data['hostMember']

    @property
    def newStatus(self):
        '''Host's new status.
        '''
        return self.data['newStatus']

    @property
    def newStatusDetail(self):
        '''Comments regarding host's new status.
        '''
        return self.data['newStatusDetail']

    @property
    def oldStatus(self):
        '''Host's old status.
        '''
        return self.data['oldStatus']

    @property
    def oldStatusDetail(self):
        '''Comments regarding host's old status.
        '''
        return self.data['oldStatusDetail']

