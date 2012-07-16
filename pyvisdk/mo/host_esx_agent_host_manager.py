
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostEsxAgentHostManager(BaseEntity):
    '''This managed object type is used to configure agent virtual machine resource
    configuration, such as what network and datastore to use for agent virtual
    machines.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostEsxAgentHostManager):
        super(HostEsxAgentHostManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def configInfo(self):
        '''Configuration of agent virtual machine resources'''
        return self.update('configInfo')

    
    
    def EsxAgentHostManagerUpdateConfig(self, configInfo):
        '''Update the host's ESX agent configuration. The entire configuration must be set
        each time since all values are overwritten. E.g. a field set to null clears the
        value on the host.
        
        :param configInfo: configuration of agent virtual machine resources
        
        '''
        return self.delegate("EsxAgentHostManagerUpdateConfig")(configInfo)