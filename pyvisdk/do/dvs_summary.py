
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSSummary(DynamicData):
    '''Summary of the switch configuration.
    '''
    
    def __init__(self, contact, description, host, hostMember, name, numPorts, portgroupName, productInfo, uuid, vm):
        # MUST define these
        super(DVSSummary, self).__init__()
    
        self.data['contact'] = contact
        self.data['description'] = description
        self.data['host'] = host
        self.data['hostMember'] = hostMember
        self.data['name'] = name
        self.data['numPorts'] = numPorts
        self.data['portgroupName'] = portgroupName
        self.data['productInfo'] = productInfo
        self.data['uuid'] = uuid
        self.data['vm'] = vm
    
    
    @property
    def contact(self):
        '''The human operator contact information.
        '''
        return self.data['contact']

    @property
    def description(self):
        '''A description string of the switch.
        '''
        return self.data['description']

    @property
    def host(self):
        '''The hosts with vNICs that connect to the switch.
        '''
        return self.data['host']

    @property
    def hostMember(self):
        '''The names of the hosts that join the switch.
        '''
        return self.data['hostMember']

    @property
    def name(self):
        '''The name of the switch.
        '''
        return self.data['name']

    @property
    def numPorts(self):
        '''Current number of ports, not including conflict ports.
        '''
        return self.data['numPorts']

    @property
    def portgroupName(self):
        '''The names of the portgroups that are defined on the switch.
        '''
        return self.data['portgroupName']

    @property
    def productInfo(self):
        '''The product information for the implementation of the switch.
        '''
        return self.data['productInfo']

    @property
    def uuid(self):
        '''The generated UUID of the switch.
        '''
        return self.data['uuid']

    @property
    def vm(self):
        '''The Virtual Machines with vNICs that connect to the switch.
        '''
        return self.data['vm']

