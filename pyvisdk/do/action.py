
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Action(DynamicData):
    '''This data object type defines the action initiated by a scheduled task or
        alarm.This is an abstract type. A client creates a scheduled task or an
        alarm each of which triggers an action, defined by a subclass of this
        type.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(Action, self).__init__()
    

    
    
