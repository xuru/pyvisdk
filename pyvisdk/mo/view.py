
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class View(BaseEntity):
    '''There are three types of views:
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.View):
        # MUST define these
        super(View, self).__init__(core, name=name, ref=ref, type=type)
    
    
