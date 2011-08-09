
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationUserData(DynamicData):
    '''Personal data pertaining to the owner of the virtual machine.The UserData data
        object type maps to the UserData key in the answer file. These values are
        transferred directly into the file that VirtualCenter stores on the target
        virtual disk. For more detailed information, see the document .
    '''
    
    def __init__(self, computerName, fullName, orgName, productId):
        # MUST define these
        super(CustomizationUserData, self).__init__()
    
        self.data['computerName'] = computerName
        self.data['fullName'] = fullName
        self.data['orgName'] = orgName
        self.data['productId'] = productId
    
    
    @property
    def computerName(self):
        '''The computer name of the (Windows) virtual machine. Computer name may contain
        letters (A-Z), numbers(0-9) and hyphens (-) but no spaces or periods (.).
        The name may not consists entirely of digits. On Vista computer name is
        restricted to 15 characters in length. If the computer name is longer than
        15 characters, it will be truncated to 15 characters.
        '''
        return self.data['computerName']

    @property
    def fullName(self):
        '''User's full name.
        '''
        return self.data['fullName']

    @property
    def orgName(self):
        '''User's organization.
        '''
        return self.data['orgName']

    @property
    def productId(self):
        '''Microsoft Sysprep requires that a valid serial number be included in the answer
        file when mini-setup runs. This serial number is ignored if the original
        guest operating system was installed using a volume-licensed CD.
        '''
        return self.data['productId']

