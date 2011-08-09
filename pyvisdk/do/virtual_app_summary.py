
from pyvisdk.do.resource_pool_summary import ResourcePoolSummary
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualAppSummary(ResourcePoolSummary):
    '''This data object type encapsulates a typical set of resource pool information that
        is useful for list views and summary pages.
    '''
    
    def __init__(self, installBootRequired, instanceUuid, product, suspended, vAppState):
        # MUST define these
        super(VirtualAppSummary, self).__init__()
    
        self.data['installBootRequired'] = installBootRequired
        self.data['instanceUuid'] = instanceUuid
        self.data['product'] = product
        self.data['suspended'] = suspended
        self.data['vAppState'] = vAppState
    
    
    @property
    def installBootRequired(self):
        '''Whether one or more VMs in this vApp require a reboot to finish installation.
        '''
        return self.data['installBootRequired']

    @property
    def instanceUuid(self):
        '''vCenter-specific UUID of the vApp
        '''
        return self.data['instanceUuid']

    @property
    def product(self):
        '''Product information. References to properties in the URLs are expanded.
        '''
        return self.data['product']

    @property
    def suspended(self):
        '''Whether a vApp is suspended, in the process of being suspended, or in the process
        of being resumed. A stopped vApp is marked as suspended under the
        following conditions: * All child virtual machines are either suspended or
        powered-off. * There is at least one suspended virtual machine for which
        the stop action is not "suspend". If the vAppState property is "stopped",
        the value is set to true if the vApp is suspended (according the the above
        definition).
        '''
        return self.data['suspended']

    @property
    def vAppState(self):
        '''Whether the vApp is running
        '''
        return self.data['vAppState']

