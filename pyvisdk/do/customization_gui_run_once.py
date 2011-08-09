
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationGuiRunOnce(DynamicData):
    '''The commands listed in the GuiRunOnce data object type are executed when a user
        logs on the first time after customization completes. The logon may be
        driven by the AutoLogon setting.The GuiRunOnce data object type maps to
        the GuiRunOnce key in the answer file. These values are transferred into
        the file that VirtualCenter stores on the target virtual disk. For more
        detailed information, see the document .
    '''
    
    def __init__(self, commandList):
        # MUST define these
        super(CustomizationGuiRunOnce, self).__init__()
    
        self.data['commandList'] = commandList
    
    
    @property
    def commandList(self):
        '''A list of commands to run at first user logon, after guest customization.
        '''
        return self.data['commandList']

