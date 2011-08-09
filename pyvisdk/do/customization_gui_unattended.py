
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationGuiUnattended(DynamicData):
    '''The GuiUnattended type maps to the GuiUnattended key in the answer file. These
        values are plugged directly into the file that VirtualCenter stores on the
        target virtual disk. For more detailed information, see the document
    '''
    
    def __init__(self, autoLogon, autoLogonCount, password, timeZone):
        # MUST define these
        super(CustomizationGuiUnattended, self).__init__()
    
        self.data['autoLogon'] = autoLogon
        self.data['autoLogonCount'] = autoLogonCount
        self.data['password'] = password
        self.data['timeZone'] = timeZone
    
    
    @property
    def autoLogon(self):
        '''Flag to determine whether or not the machine automatically logs on as
        Administrator. See also the password property.
        '''
        return self.data['autoLogon']

    @property
    def autoLogonCount(self):
        '''If the AutoLogon flag is set, then the AutoLogonCount property specifies the
        number of times the machine should automatically log on as Administrator.
        Generally it should be 1, but if your setup requires a number of reboots,
        you may want to increase it. This number may be determined by the list of
        commands executed by the GuiRunOnce command.
        '''
        return self.data['autoLogonCount']

    @property
    def password(self):
        '''The new administrator password for the machine. To specify that the password
        should be set to blank (that is, no password), set the password value to
        NULL. Because of encryption, "" is NOT a valid value.
        '''
        return self.data['password']

    @property
    def timeZone(self):
        '''The time zone for the new virtual machine. Numbers correspond to time zones listed
        in sysprep documentation at in Microsoft Technet.
        '''
        return self.data['timeZone']

