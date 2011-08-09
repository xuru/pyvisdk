
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LocalizedMethodFault(DynamicData):
    '''A wrapper class used to pass MethodFault data objects over the wire along with a
        localized display message for the fault.
    '''
    
    def __init__(self, fault, localizedMessage):
        # MUST define these
        super(LocalizedMethodFault, self).__init__()
    
        self.data['fault'] = fault
        self.data['localizedMessage'] = localizedMessage
    
    
    @property
    def fault(self):
        '''
        '''
        return self.data['fault']

    @property
    def localizedMessage(self):
        '''The localized message that would be sent in the faultstring element of the SOAP
        Fault. It is optional so that clients are not required to send a localized
        message to the server, but servers are required to send the localized
        message to clients.
        '''
        return self.data['localizedMessage']

