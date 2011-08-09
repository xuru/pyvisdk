
from pyvisdk.do.customization_name import CustomizationName
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationVirtualMachineName(CustomizationName):
    '''Specifies that VirtualCenter should generate a virtual machine name from a base
        prefix comprising the virtual machine entity name. A number is appended,
        if necessary, to make it unique.Virtual machine names are unique across
        the set of hosts and virtual machines known to the VirtualCenter instance.
        VMware Tools reports the names of existing virtual machines.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(CustomizationVirtualMachineName, self).__init__()
    

    
    
