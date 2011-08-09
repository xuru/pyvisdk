
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineSummary(DynamicData):
    '''The summary data object type encapsulates a typical set of virtual machine
        information that is useful for list views and summary pages.VirtualCenter
        can retrieve this information very efficiently, even for large sets of
        virtual machines.
    '''
    
    def __init__(self, config, customValue, guest, overallStatus, quickStats, runtime, storage, vm):
        # MUST define these
        super(VirtualMachineSummary, self).__init__()
    
        self.data['config'] = config
        self.data['customValue'] = customValue
        self.data['guest'] = guest
        self.data['overallStatus'] = overallStatus
        self.data['quickStats'] = quickStats
        self.data['runtime'] = runtime
        self.data['storage'] = storage
        self.data['vm'] = vm
    
    
    @property
    def config(self):
        '''Basic configuration information about the virtual machine. This information is not
        available when the virtual machine is unavailable, for instance, when it
        is being created or deleted.
        '''
        return self.data['config']

    @property
    def customValue(self):
        '''Custom field values.
        '''
        return self.data['customValue']

    @property
    def guest(self):
        '''Guest operating system and VMware Tools information. See guest for more
        information.
        '''
        return self.data['guest']

    @property
    def overallStatus(self):
        '''Overall alarm status on this node.
        '''
        return self.data['overallStatus']

    @property
    def quickStats(self):
        '''A set of statistics that are typically updated with near real-time regularity.
        This data object type does not support notification, for scalability
        reasons. Therefore, changes in QuickStats do not generate property
        collector updates. To monitor statistics values, use the statistics and
        alarms modules instead.
        '''
        return self.data['quickStats']

    @property
    def runtime(self):
        '''Runtime and state information of a running virtual machine. Most of this
        information is also available when a virtual machine is powered off. In
        that case, it contains information from the last run, if available.
        '''
        return self.data['runtime']

    @property
    def storage(self):
        '''Storage information of the virtual machine. It can be explicitly refreshed with
        the RefreshStorageInfo operation.
        '''
        return self.data['storage']

    @property
    def vm(self):
        '''Reference to the virtual machine managed object.
        '''
        return self.data['vm']

