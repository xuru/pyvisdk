
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestScreenInfo(DynamicData):
    '''
    '''
    
    def __init__(self, height, width):
        # MUST define these
        super(GuestScreenInfo, self).__init__()
    
        self.data['height'] = height
        self.data['width'] = width
    
    
    @property
    def height(self):
        '''Height of the screen in pixels.
        '''
        return self.data['height']

    @property
    def width(self):
        '''Width of the screen in pixels.
        '''
        return self.data['width']

