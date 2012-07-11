
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePlanningManager(BaseEntity):
    ''''''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ResourcePlanningManager):
        super(ResourcePlanningManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def EstimateDatabaseSize(self, dbSizeParam):
        '''Estimates the database size required to store VirtualCenter data.
        
        :param dbSizeParam: DatabaseSizeParam Contains the summary of an inventory for which the database size requirements are to be computed. It also contains the historic interval setting for which the database computations are to be done. This is an optional parameter and the current virtual center historical settings are used by default. There are many other optional fields in the dbSizeParam structure that are appropriately filled up based on some heuristics.
        
        '''
        return self.delegate("EstimateDatabaseSize")(dbSizeParam)