'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.managedentity import ManagedEntity
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class Datacenter(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these
        self.type = ManagedEntityTypes.Datacenter #IGNORE E1101
        
        # properties for this managed object
        props = [ "datastore", "hostFolder", "network", "networkFolder", 'vmFolder']
        
        # methods for this managed object
        methods = ["PowerOnMultiVM_Task", "QueryConnectionInfo"]
        
        super(Datacenter, self).__init__(core, methods, props, name, ref)
        
