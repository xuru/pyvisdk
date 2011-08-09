
from pyvisdk.do.option_value import OptionValue
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaParamValue(OptionValue):
    '''Describes the the value of an iSCSI parameter, and whether the value is being
        inherited.
    '''
    
    def __init__(self, isInherited):
        # MUST define these
        super(HostInternetScsiHbaParamValue, self).__init__()
    
        self.data['isInherited'] = isInherited
    
    
    @property
    def isInherited(self):
        '''Indicates if the value is inherited from some other source. If unset, the value is
        not inheritable. isInherited can be modified only if it has already been
        set. If value is to being modified, isInherited should be set to true.
        Setting isInherited to false will result in the value being once again
        inherited from the source.
        '''
        return self.data['isInherited']

