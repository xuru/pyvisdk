
from pyvisdk.do.host_target_transport import HostTargetTransport
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiTargetTransport(HostTargetTransport):
    '''Internet SCSI transport information about a SCSI target.
    '''
    
    def __init__(self, address, iScsiAlias, iScsiName):
        # MUST define these
        super(HostInternetScsiTargetTransport, self).__init__()
    
        self.data['address'] = address
        self.data['iScsiAlias'] = iScsiAlias
        self.data['iScsiName'] = iScsiName
    
    
    @property
    def address(self):
        '''The IP addresses through which the target may be reached.
        '''
        return self.data['address']

    @property
    def iScsiAlias(self):
        '''The iSCSI alias of the target.
        '''
        return self.data['iScsiAlias']

    @property
    def iScsiName(self):
        '''The iSCSI name of the target.
        '''
        return self.data['iScsiName']

