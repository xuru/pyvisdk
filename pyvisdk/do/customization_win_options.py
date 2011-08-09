
from pyvisdk.do.customization_options import CustomizationOptions
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationWinOptions(CustomizationOptions):
    '''Optional operations supported by the customization process for Windows.
    '''
    
    def __init__(self, changeSID, deleteAccounts, reboot):
        # MUST define these
        super(CustomizationWinOptions, self).__init__()
    
        self.data['changeSID'] = changeSID
        self.data['deleteAccounts'] = deleteAccounts
        self.data['reboot'] = reboot
    
    
    @property
    def changeSID(self):
        '''The customization process should modify the machine's security identifier (SID).
        For Vista OS, SID will always be modified.
        '''
        return self.data['changeSID']

    @property
    def deleteAccounts(self):
        '''If deleteAccounts is true, then all user accounts are removed from the system as
        part of the customization. Mini-setup creates a new Administrator account
        with a blank password.
        '''
        return self.data['deleteAccounts']

    @property
    def reboot(self):
        '''A value of type SysprepRebootOption specifying the action that should be taken
        after running sysprep. Defaults to "reboot".
        '''
        return self.data['reboot']

