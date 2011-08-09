
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineDisplayTopology(DynamicData):
    '''This data object defines a two-dimensional, rectangular display area.
    '''
    
    def __init__(self, height, width, x, y):
        # MUST define these
        super(VirtualMachineDisplayTopology, self).__init__()
    
        self.data['height'] = height
        self.data['width'] = width
        self.data['x'] = x
        self.data['y'] = y
    
    
    @property
    def height(self):
        '''The height of the display rectangle.
        '''
        return self.data['height']

    @property
    def width(self):
        '''The width of the display rectangle.
        '''
        return self.data['width']

    @property
    def x(self):
        '''The x co-ordinate defining the start of the display rectangle.
        '''
        return self.data['x']

    @property
    def y(self):
        '''The y co-ordinate defining the start of the display rectangle.
        '''
        return self.data['y']

